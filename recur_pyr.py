
from cs1graphics import *
class Pyramid(Drawable):
  """Represent a bullseye with an arbitrary number of bands."""

  def __init__(self, numBands, size, primary='black', secondary='white'):
    """Create a bullseye object with alternating colors.

    The reference point for the bullseye will be its center.

    numBands         the number of desired bands (must be at least 1)
    radius           the total radius for the bullseye (must be positive)
    primary          the color of the outermost band (default black)
    secondary        the color of the secondary band (default white)
    """
    if numBands <= 0:
      raise ValueError('Number of bands must be positive')
    if size <= 0:
      raise ValueError('radius must be positive')

    Drawable.__init__(self)
    size = 12
    centerX = 6.0
    centerY = (numBands + 1) * size
    width = (numBands + 1) * size
    self._outer = Rectangle(width, size)
    self._outer.setFillColor(primary)
    self._outer.move(centerX, centerY)

    if numBands == 1:
      self._rest = None
    else:  # create new bullseye with one less band, reduced radius, and inverted colors
      innerR = float(size) * (numBands-1) / numBands
      self._rest = Pyramid(numBands-1, innerR, secondary, primary)

  def _draw(self):
    self._beginDraw()                                  # required protocol for Drawable
    self._outer._draw()                                # draw the circle
    if self._rest:
      self._rest._draw()                               # recursively draw the rest
    self._completeDraw()                               # required protocol for Drawable
    

paper = Canvas(400, 400)
simple = Pyramid(6, 30)
simple.move(65, 80)
paper.add(simple)

blue = Pyramid(10, 80, 'darkblue', 'skyblue')
paper.add(blue)
blue.move(195,120)


