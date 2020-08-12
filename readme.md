# gameshell node
run codelab adapter node in gameshell.

创建`~/games/holleworld.py`

```python
# https://zhuanlan.zhihu.com/gameshell-python
import sys, pygame
pygame.init()

screen = pygame.display.set_mode((320, 240))
black = (0, 0, 250)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

	screen.fill(black)
	pygame.display.flip()
```

创建 `launcher/Menu/GameShell/holleworld.sh`

```bash
python3 ~/games/holleworld.py -fullscreen -surf
```

图标: 将`holleworld.png`(80x80)放进~/launcher/skin/sefault/Menu/GameShell文件夹