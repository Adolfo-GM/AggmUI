## How it works
### AggmUI

When you import AggmUI using `import aggmui`, python automatically imports turtle and tkinter. 
AggmUI has many ` prefabs ` that you can use to create your UI.

### Code example

```python

from aggmui import *

def buttonPressed():
        print("Button Pressed")

view = View(" Window Title", 400, 600)
view.spacer()
view.text("Text")
view.spacer()
view.button("hello", buttonPressed)
view.mainloop()

```

### Explanation

- ` text ` creates a text label.
- ` button ` creates a button.
- ` spacer ` creates a space between elements. 
- ` mainloop ` is a function that runs the UI.

There are many other `prefabs` that you can use to create your UI.


- `paragraph` creates a paragraph.
- `input` creates an input field.
- `heading` creates a heading.


