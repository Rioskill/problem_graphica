import pygame

RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
YELLOW = 200, 200, 0
BLUE = 0, 0, 255

pygame.init()

size = width, height = 800, 500
screen = pygame.display.set_mode(size)

FONT = pygame.font.Font(None, 40)

const = 1040
d = dict()
S = "000 001 11 10001"
#S = input('Введите коды: ')

def get_probables(S):
  def tobin(a, t):
    res = bin(a)[2:]
    return '0' * (t - len(res)) + res

  codes = S.split()
  blocked = list()
  res = list()
  l_max = len(max(codes, key=len))
  for l in range(1, l_max + 1):
    for i in range(2 ** l):
      bn = tobin(i, l)
      if bn in codes or bn[:-1] in blocked:
        blocked.append(bn)
      else:
        res.append(bn)
  return res

for i, letter in enumerate((S).split()):
  d[chr(const + i)] = letter

def draw_path(surface, value, key=None, color=BLACK):
  lx = 200
  ly = 60
  x = width // 2
  y = 50
  px = x
  py = y
  for i in value:
    if i == '0':
      px = x
      nother_x = x - lx
      x -= lx
      surface.blit(FONT.render('0', True, RED), (x - 15, y + ly - 25))
    elif i == '1':
      px = x
      nother_x = x - lx
      x += lx
      surface.blit(FONT.render('1', True, RED), (x, y + ly - 25))
    py = y
    y += ly
    pygame.draw.line(surface, color, (px, py), (x, y), 3)
    lx = lx // 2
  if key is not None:
    surface.blit(FONT.render(key, True, BLACK), (x - 10, y))


def drawl(surface):
  coords = []
  for key, value in d.items():
    draw_path(surface, value, key)

listik = get_probables(S)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
  screen.fill(WHITE)
  for i in listik:
    draw_path(screen, i, color=BLUE)
  drawl(screen)
  pygame.display.update()
