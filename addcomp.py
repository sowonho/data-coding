import turtle
t = turtle.Turtle()
s = turtle.Shape('compound')
poly1 = ((0,0),(0,15),(-10,-4))
poly2 = ((0,0),(0,15),(10,-4))
poly3 = ((0,0),(10,-4),(-10,-4))
s.addcomponent(poly1,'white', 'black')
s.addcomponent(poly2,'gray', 'black')
s.addcomponent(poly3,'black', 'black')

turtle.register_shape('p-51', s)
turtle.getshapes()
t.shape('p-51')
turtle.register_shape('man1.gif')
