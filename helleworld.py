# python3.7
import sys
import re
import socket
import uuid
import queue

import pygame
import requests
import networkzero as nw0
from codelab_adapter_client.utils import threaded

pygame.init()
adapter_message_q = queue.Queue()

screen = pygame.display.set_mode((320, 240))
black = (0, 0, 250)

# ADAPTER_IP = "192.168.31.148"


def _to_adapter(ip, message):
    if ip:
        try:
            requests.get(f'https://{ip}:12358/api/message/eim?message={message}',
                 verify=False, timeout=2)
        except:
            pass


def handle_key(ip, key):
    if key == pygame.K_DOWN:
        _to_adapter(ip, "K_DOWN")
    if key == pygame.K_UP:
        _to_adapter(ip, "K_UP")
    if key == pygame.K_RIGHT:
        _to_adapter(ip, "K_RIGHT")
    if key == pygame.K_LEFT:
        _to_adapter(ip, "K_LEFT")
    if key == pygame.K_u:
        _to_adapter(ip, "K_u")
    if key == pygame.K_i:
        _to_adapter(ip, "K_i")
    if key == pygame.K_j:
        _to_adapter(ip, "K_j")
    if key == pygame.K_k:
        _to_adapter(ip, "K_k")
    if key == pygame.K_SPACE:  # Select
        _to_adapter(ip, "K_SPACE")
    if key == pygame.K_RETURN:  # Start
        _to_adapter(ip, "K_RETURN")
    # PC["LK1"] = pygame.K_h
    # PC["LK5"] = pygame.K_l


# 线程
class AdapterHelper:
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # 114.114.114.114
            ip = s.getsockname()[0]
            return ip
        except Exception as e:
            str(e)

    def advertise(self):
        name = f'{socket.gethostname()}-gameshell-key'
        # 默认广播出去的是 usb的ip，不是wifi的ip ： https://github.com/clockworkpi/launcher/blob/e22a3286f3/sys.py/libs/DBUS/__init__.py
        address = nw0.advertise(name, address=self.get_local_ip())  
        return address

    # wait ip
    def wait_for_ip(self, address):
        print("waiting for ip")
        content = nw0.wait_for_message_from(address)
        pat = re.compile(".*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        test = pat.match(content)
        if not test:
            nw0.send_reply_to(address, "please input ip address")
            print("please input ip address")
            self.wait_for_ip(address)
        else:
            print("connected!")
            nw0.send_reply_to(address, "connected!")
            return content

    @threaded
    def run(self):
        address = self.advertise()
        ip = self.wait_for_ip(address)  # 多线程
        adapter_message_q.put(ip)


helper = AdapterHelper()
helper.run()

ip = None
while True:
    if not adapter_message_q.empty():
        ip = adapter_message_q.get()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            try:
                handle_key(ip, event.key)
            except:
                pass
            
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_RETURN:
                # 接受新的ip连接
                helper.run()

    screen.fill(black)
    pygame.display.flip()
