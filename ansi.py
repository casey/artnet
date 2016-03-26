from cp437 import *

from lib import *

class ANSI:
  def __init__(self, data):
    self.data       = data
    self.cells      = []
    self.x          = 0
    self.y          = 0
    self.fg         = 7
    self.bg         = 0
    self.bold       = False
    self.blink      = False
    self.italic     = False
    self.underlined = False
    self.overdraws  = 0

  for b in data:

  def set(self, n):
    i = self.y * 80 + self.x
    if i > 80 * 100000:
      die('i out of range:', i)
 
    self.cells.extend(None for _ in range((i + 1) - len(self.cells)))
    
    if self.cells[i]:
      self.overdraws += 1

    self.cells[i] = Cell(n, self.fg, self.bg, self.bold, self.italic, self.blink)

  def extend(self, l):
    self.cells.extend(None for _ in range(l + (80 - l % 80) % 80 - len(self.cells)))

  def string():
    return ''.join(yield_characters())

  def yield_characters():
    x = 0
    for cell in self.cells:
      yield cell.glyph if cell else ' '
      x += 1
      if x > 0 and x % 80 == 0:
        yield '\n'

class Cell:
  def __init__(self, n, fg, bg, bold, italic, blink):
    if n < 0 or n > 255:
      die('n out of range:', n)
    self.n         = n
    self.fg        = fg
    self.bg        = bg
    self.bold      = bold
    self.italic    = italic
    self.blink     = blink
    self.codepoint = cp437.codepoints[n]
    self.glyph     = cp437.characters[n]
