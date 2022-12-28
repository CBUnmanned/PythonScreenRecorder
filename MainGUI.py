import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

# this is the function called when the button is clicked
def btnClickFunctionStartRecording():
    global activatecycle
    global framerate
    global root
    global latestDIR
    global FrameNameNumber

# Reset Frame Number
    FrameNameNumber = 0

# Get current directory
    latestDIR = str(getInputBoxValuePrefix())

# Make a new directory
    os.mkdir(latestDIR)

# Allow Looping of screen grabs
    activatecycle = 1

# Set framerate from tet box
    framerate = int(float(getInputBoxValueFrameInterval()) * 1000)

# Start looping
    TakeScreenshottest()

# Check auto off
    for i in getListboxValuelistBoxOne():
        print(i)
        if   i == 0:
            root.after( 10 * 60 * 1000, StopRecording)
        elif i == 1:
            root.after( 20 * 60 * 1000, StopRecording)
        elif i == 2:
            root.after( 60 * 60 * 1000, StopRecording)
        elif i == 3:
            root.after( 120 * 60 * 1000, StopRecording)

    print('Started Recording')


# this is the function called when the button is clicked
def btnClickFunctionStopRecording():
    StopRecording()
    pass

def StopRecording():
    global activatecycle
    global LatestFilename

    activatecycle = 0
    LatestFilename.config(text = "Recording Stopped")


    #print(activatecycle)
    #print('Stopped Recording')


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValueAutoOff():
    checkedOrNot = AutoOff.get()
    return checkedOrNot


# this is a function to get the selected list box value
def getListboxValuelistBoxOne():
    itemSelected = listBoxOne.curselection()
    return itemSelected


# this is a function to get the user input from the text input box
def getInputBoxValuePrefix():
    userInput = Prefix.get()
    return userInput

# this is a function to get the user input from the text input box
def getInputBoxValueFrameInterval():
    userInput = FrameInterval.get()
    return userInput


root = Tk()

#this is the declaration of the variable associated with the checkbox
AutoOff = tk.IntVar()

# This is the section of code which creates the main window
root.geometry('300x500')
root.configure(background='#FFFFFF')
root.title('Screen Recorder')

# This is the section of code which creates a button
Button(root, text='Stop Recording', bg='#FF4040', font=('arial', 12, 'normal'), command=btnClickFunctionStopRecording).place(x=10, y=306)

# This is the section of code which creates a button
Button(root, text='Start Recording', bg='#7FFFD4', font=('arial', 12, 'normal'), command=btnClickFunctionStartRecording).place(x=10, y=271)

# This is the section of code which creates a checkbox
CheckBoxOne=Checkbutton(root, text='Auto Off After:', variable=AutoOff, bg='#FFE4C4', font=('arial', 12, 'normal'))
CheckBoxOne.place(x=10, y=134)

# This is the section of code which creates a listbox
listBoxOne=Listbox(root, bg='#FFE4C4', font=('arial', 12, 'normal'), width=0, height=0)
listBoxOne.insert('0', '10 Minutes')
listBoxOne.insert('1', '30 Minutes')
listBoxOne.insert('2', '60 Minutes')
listBoxOne.insert('3', '120 Minutes')
listBoxOne.place(x=10, y=169)

# First, we create a canvas to put the picture on
LatestCapture = Canvas(root, height=100, width=100)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
LatestCapture.create_image(100, 0, anchor=NE, image=picture_file)
LatestCapture.place(x=150, y=82)

# This is the section of code which creates the a label
Label(root, text='File Name Prefix', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=10, y=86)

# This is the section of code which creates the a label
LatestFilename = Label(root, text='Latest Filename', bg='#FFFFFF', font=('arial', 12, 'normal'))
LatestFilename.place(x=10, y=345)

# This is the section of code which creates a text input box
Prefix=Entry(root)
Prefix.place(x=10, y=108)

# This is the section of code which creates a text input box
FrameInterval=Entry(root)
FrameInterval.place(x=10, y=250)

# First, we create a canvas to put the picture on
worthAThousandWords= Canvas(root, height=30, width=100)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
worthAThousandWords.create_image(30, 0, anchor=NE, image=picture_file)
worthAThousandWords.place(x=10, y=374)


# -------------------------------------------------------------

import mss
import time

# Setup variables
activatecycle = 1
FrameNameNumber = 0
framerate = 1000
latest_filename = ""
latestDIR = ""
currentDIR = os.path.dirname(os.path.realpath(__file__)) + "\\"

def TakeScreenshot():
    global LatestFilename
    global latest_filename
    global latestDIR
    global currentDIR
    global FrameNameNumber



    with mss.mss() as sct:

        # Save the screenshot of both monitors
        latest_filename = '{}.png'.format(FrameNameNumber)

        # Increment number for file naming
        FrameNameNumber += 1

        # Debug Info
        # print(latest_filename)

        # Save screenshot to selected folder
        filename = sct.shot(mon=-1, output='{}\{}.png'.format(currentDIR + latestDIR, FrameNameNumber))

        # Debug Info
        #print('Taken ScreenShot {}'.format(latest_filename))

        # Update GUI with last filename saved
        LatestFilename.config(text = latest_filename)



# Main looping function
def TakeScreenshottest():
    global latest_filename
    global LatestCapture

    print(latest_filename)

# while cycle activated, take screenshots
    if activatecycle:
        TakeScreenshot()
        #LatestCapture.PhotoImage = PhotoImage(file=latest_filename)

        root.after(framerate, TakeScreenshottest)

#root.after(1000, TakeScreenshot)
#root.after(1000, TakeScreenshottest)

root.mainloop()

