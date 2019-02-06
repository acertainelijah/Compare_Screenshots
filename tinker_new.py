from Tkinter import *
import PIL.Image
import PIL.ImageTk

root = Toplevel()

#im = PIL.Image.open("youtube_screenshot.png")
im = PIL.Image.open("base_google_screenshot.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

root.mainloop()