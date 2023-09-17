import tkinter as tk

class DraggableElement(tk.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, relief=tk.RAISED, bd=2)
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_drag_release)

    def on_drag_start(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def on_drag_motion(self, event):
        x = self.winfo_x() - self._drag_data["x"] + event.x
        y = self.winfo_y() - self._drag_data["y"] + event.y
        self.place(x=x, y=y)

    def on_drag_release(self, event):
        self._drag_data = {}

class DropZone(tk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Drop Zone", relief=tk.SUNKEN, bd=2)
        self.config(width=30, height=10)
        self.bind("<Enter>", self.on_drag_enter)
        self.bind("<Leave>", self.on_drag_leave)
        self.bind("<ButtonRelease-1>", self.on_drop)
        self._elements = []

    def on_drag_enter(self, event):
        self.config(bg="lightblue")

    def on_drag_leave(self, event):
        self.config(bg="white")

    def on_drop(self, event):
        element = event.widget
        element.place_forget()
        element.place(in_=self, x=event.x, y=event.y)
        self._elements.append(element)

    def generate_c_code(self):
        c_code = ""
        for element in self._elements:
            c_code += f"{element.c_code}\n"
        return c_code

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drag and Drop C Code Generation")

        self.element_palette = tk.Frame(self)
        self.element_palette.pack(side=tk.LEFT, padx=10, pady=10)

        self.drop_zone = DropZone(self)
        self.drop_zone.pack(side=tk.RIGHT, padx=10, pady=10)

        self.create_elements()

        generate_button = tk.Button(self, text="Generate C Code", command=self.generate_c_code)
        generate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def create_elements(self):
        elements = [
            ("Variable", "int x;"),
            ("Function", "void foo() {\n    // Function body\n}"),
            # Add more elements here
        ]

        for element_text, c_code in elements:
            element = DraggableElement(self.element_palette, element_text)
            element.c_code = c_code
            element.pack(side=tk.TOP, padx=5, pady=5)

    def generate_c_code(self):
        c_code = self.drop_zone.generate_c_code()
        print(c_code)

if __name__ == "__main__":
    app = Application()
    app.mainloop()