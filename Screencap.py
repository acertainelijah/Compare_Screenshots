from selenium import webdriver
from SeleniumLibrary.base import keyword
from PIL import Image
from io import BytesIO
from robot.libraries.BuiltIn import BuiltIn
#import tinker
from Tkinter import Tk, Label, Button, Frame, LEFT, RIGHT, TOP
from PIL import ImageTk, Image
from SeleniumLibrary.base import keyword
from selenium.webdriver.chrome.options import Options
import shutil
import sys

drivers = {
    "chrome": webdriver.Chrome
}

class Screencap:

    def __init__(self):
        self.driver = None

    @keyword
    def take_screencap(self, element_name, screenshot_name, screenshot_path):
        # element name, sreenshot name, path
        """This function takes a screenshot of an HTML element and saves it to a path"""
        self.driver = BuiltIn().get_library_instance('Selenium2Library')._current_browser()
        # TODO element as an arg (also ***xpath*** or css)



        element = self.driver.find_element_by_id(element_name)  # find part of the page you want image of
        location = element.location
        size = element.size
        png = self.driver.get_screenshot_as_png()  # saves screenshot of entire page
        self.driver.quit()

        im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

        x = location['x']
        y = location['y']
        width = location['x'] + size['width']
        height = location['y'] + size['height']

        # TODO write detailed
        im = im.crop((int(x), int(y), int(width), int(height)))  # defines crop points
        screenshot_file = screenshot_path + screenshot_name
        print "screenshot file : " + screenshot_file
        im.save(screenshot_file, 'PNG')  # saves new cropped image

        # TODO put this in the compare image keyword
        # TODO take result from compare_image. If false, then raise AssertionError.
        base = "youtube_screenshot.png"
        # screenshot = "youtube_screenshot.png"
        #root = tinker.Tk()
        #tink = tinker.Tinker(root, base, screenshot_file)
        #if tink.compare_images(base, screenshot_file):
        #    print("Images are the same!")
        #else:
        #    print("Images are not the same :(")
        #    root.mainloop()




class Compare:

    def __init__(self):
        self.driver = None

    @keyword
    def compare_images(self, base="base_google_screenshot.png", screenshot="base_google_screenshot.png"):
        print "helu wurld"
        if (open(base, "rb").read() == open(screenshot, "rb").read()):
            print("The most recent screenshot is the same as the base!")
        else:
            msg = "Base image is not the same as Screenshot"
            # raise AssertionError(msg)
            print(msg)
        root = Tk()
        my_gui = Compare()
        my_gui.create_interface(root, base, screenshot)
        # my_gui = Tinker(root, base, screenshot)
        root.mainloop()

    def create_interface(self, master, base, screenshot):
        # TODO Just make sure that I init this instead of just keeping an instance of a class
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
        self.greet_button = Button(self.master, text="Fail", command=self.Fail)
        self.greet_button.pack()

        # Passed case
        self.greet_button = Button(self.master, text="Pass", command=self.Pass)
        self.greet_button.pack()

        # Update Base image to Screenshot
        self.greet_button = Button(self.master, text="Update Base", command=self.update_base)
        self.greet_button.pack()

        # Close interface
        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

    def Fail(self):
        print("Fail! There is something unusual...\n")
        msg = "Failed to compare"
        sys.exit(msg)

    def Pass(self):
        print("Pass!")
        msg = "Passed compare!"


    def update_base(self):
        print("Update Base")
        new_base_image = '/Users/marchese/Development/M2020/RobotTests/new_base.png'
        shutil.move(self.screenshot, new_base_image)


