import tkinter as tk
from PIL import Image, ImageTk


class myWindow:
    window = tk.Tk()

    def __init__(self, w, h, title, bg_hex_color, text_color):
        self.w = w
        self.h = h
        self.title = title
        self.bg_hex_color = bg_hex_color
        self.text_color = text_color
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

    def get_window_position(self):
        pos_w = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        pos_h = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        return pos_w, pos_h

    def add_image(self, image_path):
        # tk.Label(self.window, text="Username").place(x=40, y=60)
        data = Image.open(image_path)
        image = ImageTk.PhotoImage(data)
        my_label = tk.Label(self.window, image=image, bg=self.bg_hex_color)
        my_label.image = image
        my_label.pack()

    def add_text(self, some_text, anchor):  # anchor? align text: 'w' => right 'e' => left 'center' => center
        my_text = tk.Label(self.window, text=some_text, bg=self.bg_hex_color, fg=self.text_color,
                           font=("Arial", 12, "bold"), anchor=anchor)
        my_text.pack(fill='both')
        return my_text

    def add_dropdown(self, my_list, width, command=None):
        var = tk.StringVar(self.window)
        var.set(my_list[0])
        dropdown = tk.OptionMenu(self.window, var, *my_list)
        dropdown.config(bg=self.bg_hex_color, fg=self.text_color, font=("Arial", 10, "bold"),
                        activeforeground=self.bg_hex_color, width=width, direction='right')
        if command is not None:
            dropdown.config(command=command)

        dropdown["menu"].configure(bg=self.bg_hex_color, activebackground='#4c1b45', fg=self.text_color)
        dropdown.pack()
        return dropdown, var

    def add_input_field(self, width):
        field = tk.Entry(self.window, width=width, font=("Arial", 12, "bold"), fg='#4c1b45')
        field.pack()
        return field

    def add_button(self, button_text):
        button = tk.Button(self.window, text=button_text, bg=self.bg_hex_color, font=("Arial", 10, "bold"),
                           fg=self.text_color, activeforeground=self.bg_hex_color, relief="groove", bd=5)
        button.pack()
        return button


def set_position(my_object, x, y):
    my_object.place(x=x, y=y)


def add_padding(my_object, padx, pady):
    my_object.config(padx=padx, pady=pady)


def disable_object(my_object):
    my_object.config(state="disabled")
