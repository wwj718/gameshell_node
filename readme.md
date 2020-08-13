# gameshell node

run codelab adapter node in gameshell.

# 依赖

```bash
sudo apt install python3-pygame
pip3 install requests
```

# 开始

将该仓库下的 `helloworld.py` 复制到 `~/games/`。

创建 `~/launcher/Menu/GameShell/helloworld.sh`

```bash
python3 ~/games/helloworld.py -fullscreen -surf
```

图标: 将`helloworld.png`(80x80)放进 `~/launcher/skin/default/Menu/GameShell/` 文件夹
