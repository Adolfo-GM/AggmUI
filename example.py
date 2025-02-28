from aggmui import *

def buttonPressed():
        print("Button Pressed")

view = View(" Window Title", 400, 600)
view.spacer()
view.text("Text")
view.spacer()
view.button("hello", buttonPressed)
view.mainloop()