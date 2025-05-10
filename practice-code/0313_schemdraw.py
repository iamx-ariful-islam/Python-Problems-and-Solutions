# pip install schemdraw

import schemdraw
import schemdraw.elements as elm


d = schemdraw.Drawing()
d.add(elm.Resistor().label('R1'))
d.add(elm.Line())
d.draw()