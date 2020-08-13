# gameshell node

run codelab adapter node in gameshell.

# 依赖

```bash
sudo apt install python3-pygame
pip3 install requests
```

# 开始

创建`~/games/holleworld.py`

```python
# python3.7
import sys, pygame
import requests

pygame.init()

screen = pygame.display.set_mode((320, 240))
black = (0, 0, 250)

ADAPTER_IP = "192.168.31.148"

def to_adapter(message):
    requests.get(f'https://{ADAPTER_IP}:12358/api/message/eim?message={message}', verify=False)


def handle_key(key):
    if key == pygame.K_DOWN:
        to_adapter("K_DOWN")
    if key == pygame.K_UP:
        to_adapter("K_UP")
    if key == pygame.K_RIGHT:
        to_adapter("K_RIGHT")
    if key == pygame.K_LEFT:
        to_adapter("K_LEFT")
    if key ==  pygame.K_u:
        to_adapter("K_u")
    if key ==  pygame.K_i:
        to_adapter("K_i")
    if key ==  pygame.K_j:
        to_adapter("K_j")
    if key ==  pygame.K_k:
        to_adapter("K_k")
    if key ==  pygame.K_SPACE: # Select
        to_adapter("K_SPACE")
    if key ==  pygame.K_RETURN: # Start
        to_adapter("K_RETURN")
    # PC["LK1"] = pygame.K_h
    # PC["LK5"] = pygame.K_l


    if key == pygame.K_ESCAPE:
        to_adapter("K_ESCAPE")
        sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_key(event.key)

    screen.fill(black)
    pygame.display.flip()
```

创建 `~/launcher/Menu/GameShell/holleworld.sh`

```bash
python3 ~/games/holleworld.py -fullscreen -surf
```

图标: 将`helleworld.png`(80x80)放进 `~/launcher/skin/default/Menu/GameShell/` 文件夹
