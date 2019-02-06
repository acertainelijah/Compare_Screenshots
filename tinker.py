from Tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP
from PIL import ImageTk, Image
from SeleniumLibrary.base import keyword
import shutil

class Tinker:
    def create_interface(self, master, base, screenshot):
        self.base = base
        self.screenshot = screenshot

        print "Init tinker"
        root = master
        self.master = master
        master.title("A simple GUI")
        self.label = Label(self.master, text="This is our fail test GUI!")

        # Images
        top = Frame(root)
        top.pack(side=TOP)

        # Image display #1
        im = Image.open(base)
        photo = ImageTk.PhotoImage(im)
        label = Label(root, text="Base", image=photo, borderwidth=2, relief="ridge")
        label.image = photo  # keep a reference!
        label.pack(in_=top, side=LEFT)

        # Image display #2
        im = Image.open(screenshot)
        photo = ImageTk.PhotoImage(im)
        label = Label(root, text="Screenshot", image=photo, borderwidth=2, relief="ridge")
        label.image = photo  # keep a reference!
        label.pack(in_=top, side=RIGHT)


        # Failed case
        self.greet_button = Button(self.master, text="Fail", command=self.fail)
        self.greet_button.pack()

        # Change Base image to Screenshot
        self.greet_button = Button(self.master, text="Update Base", command=self.update_base)
        self.greet_button.pack()

        # Close interface
        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

    @keyword
    def compare_images(self, base, screenshot):
        if (open(base, "rb").read() == open(screenshot, "rb").read()):
            print("The most recent screenshot is the same as the base!")
        else:
            msg = "Base image is not the same as Screenshot"
            #raise AssertionError(msg)
            print(msg)
            root = Tk()
            my_gui = Tinker()
            my_gui.create_interface(self, root, base, screenshot)
            #my_gui = Tinker(root, base, screenshot)
            root.mainloop()

    def fail(self):
        print("Fail! There is something unusual...")
        msg = "Failed to compare"
        raise AssertionError(msg)

    def update_base(self):
        print("Update Base")
        shutil.move(screenshot, '/home/user/Documents/useful_name.txt')


#root = Tk()
#my_gui = Tinker(root)
#root.mainloop()