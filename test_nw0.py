import sys
import re
import socket
import uuid

import networkzero as nw0


def advertise():
    name = f'{socket.gethostname()}-{str(uuid.uuid4())[:8]}'
    address = nw0.advertise(name)  # hostname..uuid
    return address


# wait ip
def wait_for_ip(address):
    print("waiting for ip")
    content = nw0.wait_for_message_from(address)
    pat = re.compile(".*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    test = pat.match(content)
    if not test:
        nw0.send_reply_to(address, "please input ip address")
        print("please input ip address")
        wait_for_ip(address)
    else:
        print("connected!")
        nw0.send_reply_to(address, "connected!")
        return content


address = advertise()
ip = wait_for_ip(address)  # until input ip
print(ip)