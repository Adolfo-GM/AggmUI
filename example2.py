from aggmui import *

view = View(" Window Title", 400, 600)
view.spacer()
view.heading("Heading")
view.spacer()
view.paragraph("paragraph type of text")
view.spacer()
view.button("button", lambda: print("Button Pressed"))
view.spacer()
view.mainloop()
