import tkinter as tk
from PIL import Image, ImageTk

class myWindow:
    window = tk.Tk()

    def __init__(self, w, h, title,bg_hex_color):
        self.w = w
        self.h = h
        self.title = title
        self.bg_hex_color = bg_hex_color
        self.create_window()

    def start_window(self):
        self.window.mainloop()

    def create_window(self):
        pos_w = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        pos_h = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        size_and_pos = str(self.w) + 'x' + str(self.h) + '+' + str(pos_w) + '+' + str(pos_h)
        self.window.geometry(size_and_pos)
        self.window.title(self.title)
        self.window.resizable(False, False)
        self.window['background'] = self.bg_hex_color

    def add_image(self, image_path):
        # tk.Label(self.window, text="Username").place(x=40, y=60)
        data = Image.open(image_path)
        image = ImageTk.PhotoImage(data)
        my_label = tk.Label(self.window, image=image, bg=self.bg_hex_color)
        my_label.image = image
        my_label.pack()
