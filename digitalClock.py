from tkinter import Label, Tk
import time

# Design the main app window
appWindow = Tk()
appWindow.title('Digi the Clock')
appWindow.geometry('400x150')
appWindow.resizable(0, 0)

# Color and text design
textFont = ('Licorice', 68, 'bold')
backGround = '#03142e'
foreGround = '#c4c4c4'
borderWidth = 25

# Create app using label function
clock = Label(appWindow,
              font=textFont,
              bg=backGround,
              fg=foreGround,
              bd=borderWidth)
clock.grid(row=0,
           column=1)


# Time to display time
def digiClock():
    currentTime = time.strftime('%H:%M:%S')
    clock.config(text=currentTime)
    clock.after(200, digiClock)


# Calling function
digiClock()
appWindow.mainloop()