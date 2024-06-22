import time
import pyautogui
from tkinter import Tk, Checkbutton, IntVar
import keyboard

def click_mouse():
    pyautogui.click()

def on_checkbox_change():
    if var.get() == 1:  # If checkbox is checked
        while var.get() == 1:
            if keyboard.is_pressed('F4'):
                break  # Exit the loop if F4 is pressed
            click_mouse()
            time.sleep(0.0000001)

# Create GUI
root = Tk()
root.title("Mouse Clicker")

# Create checkbox
var = IntVar()
checkbox = Checkbutton(root, text="Auto Click", variable=var, command=on_checkbox_change)
checkbox.pack()

# Run the GUI
root.mainloop()
