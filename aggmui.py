import tkinter
import turtle
from tkinter import ttk

class View:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)
        
    def mainloop(self):
        self.window.mainloop()

    def button(self, text, command):
        button = tkinter.Button(self.window, text=text, command=command)
        button.config(font=("Arial", 12), padx=20, pady=10)
        button.pack_propagate(False)
        button.config(borderwidth=0, relief="flat")
        button.config(width=20, height=2)
        button.pack()
    
    def text(self, text):
        label = tkinter.Label(self.window, text=text, font=("Arial", 12))
        label.pack()
    
    def spacer(self):
        label = tkinter.Label(self.window, text="")
        label.pack()

    def paragraph(self, text):
        label = tkinter.Label(self.window, text=text, font=("Arial", 10), wraplength=self.width, justify="left")
        label.pack()

    def heading(self, text):
        label = tkinter.Label(self.window, text=text, font=("Arial", 15))
        label.pack()

    def input(self, placeholder):
        entry = tkinter.Entry(self.window, font=("Arial", 12), width=30)
        entry.insert(0, placeholder)
        entry.pack()
        return entry

if __name__ == "__main__":

    def buttonPressed():
        print("Button Pressed")
    view = View(" Window Title", 400, 600)
    view.spacer()
    view.text("Text")
    view.spacer()
    view.button("hello", buttonPressed)
    view.spacer()
    view.paragraph("paragraph type of text")
    view.spacer()
    view.heading("Heading")
    view.spacer()
    input_entry = view.input("hello")
    def getInput():
        print(input_entry.get())
    view.spacer()
    view.button("Print Input", getInput)
    view.spacer()

    # It works with regular tkinter widgets too
    label = tkinter.Label(view.window, text="text", font=("Arial", 10))
    label.pack()

    def moveturtle():
        t.forward(100)
        t.left(-90)
        t.forward(100)
      

    view.button("Move turtle", moveturtle)

    # Turtle graphics work too
    canvas = tkinter.Canvas(view.window, width=400, height=400)
    canvas.pack()

    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_screen.bgcolor("white")
    t = turtle.RawTurtle(turtle_screen)
    t.shape("turtle")
    
    view.mainloop()