from tkinter import *
from PIL import ImageTk, Image

root = Tk()

path = ["images/blackbulb.gif", "images/yellowbulb.gif"]

left_idx = 0
center_idx = 0
right_idx = 0

left_bulb = ImageTk.PhotoImage(Image.open(path[left_idx]))
center_bulb = ImageTk.PhotoImage(Image.open(path[center_idx]))
right_bulb = ImageTk.PhotoImage(Image.open(path[right_idx]))

left_panel = Label(root, image=left_bulb)
center_panel = Label(root, image=center_bulb)
right_panel = Label(root, image=right_bulb)

left_panel.pack(side="left", fill="both", expand="yes")
center_panel.pack(side="left", fill="both", expand="yes")
right_panel.pack(side="left", fill="both", expand="yes")


def toggle_left(e):
    global left_idx
    left_idx = 1 - left_idx
    img2 = ImageTk.PhotoImage(Image.open(path[left_idx]))
    left_panel.configure(image=img2)
    left_panel.image = img2

def toggle_center(e):
    global center_idx
    center_idx = 1 - center_idx
    img2 = ImageTk.PhotoImage(Image.open(path[center_idx]))
    center_panel.configure(image=img2)
    center_panel.image = img2

def toggle_right(e):
    global right_idx
    right_idx = 1 - right_idx
    img2 = ImageTk.PhotoImage(Image.open(path[right_idx]))
    right_panel.configure(image=img2)
    right_panel.image = img2

root.bind("<Left>", toggle_left)
root.bind("<Down>", toggle_center)
root.bind("<Right>", toggle_right)
root.mainloop()
