# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Julkar Naine Reedoy
# Date: Dec. 5, 2021
# Description: Contains the program and the interface functions
# Python 3.9.8 64-bit was used

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
import os
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]

# list of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions" 
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") 
    menuString.append("Choose the following options:")
    menuString.append("") 
    menuString += system
    menuString.append("") 

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """

    # get current working directory
    directory = os.getcwd()
 
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        if userInput == "Q": 
            print("Log: Doing system functionalities " + userInput)
            print("Log: Quitting...")
        elif userInput == "O":
            print("Log: Doing system functionalities " + userInput)
            print("Log: Opening Image...")
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename(initialdir=directory)
            appStateValues["lastOpenFilename"] = openFilename
            img = cmpt120imageProjHelper.getImage(openFilename)
            cmpt120imageProjHelper.showInterface(img, "New Image", generateMenu(appStateValues))
        elif userInput == "S":
            print("Log: Doing system functionalities " + userInput)
            print("Saving Current Image...")
            tkinter.Tk().withdraw()
            saveFileName = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProjHelper.saveImage(img,saveFileName)
            cmpt120imageProjHelper.showInterface(img, "Saving Image", generateMenu(appStateValues))
        elif userInput == "R":
            print("Log: Doing system functionalities " + userInput)
            print("Reloading Original Image...")
            tkinter.Tk().withdraw()
            img = cmpt120imageProjHelper.getImage(appStateValues["lastOpenFilename"])
            cmpt120imageProjHelper.showInterface(img, "Original Image", generateMenu(appStateValues))
        else:
           print("Log: Unrecognized user input: " + userInput)

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        if state["mode"] == "basic":
            if userInput == "7":
                print("Log: Performing " + basic[int(userInput)-1])
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(img, "Advanced ", generateMenu(state))
            elif int(userInput) > 0 and int(userInput) < 7:
                print("Log: Doing manipulation functionalities " + userInput)
                print("Log: Performing " + basic[int(userInput)-1])
                if int(userInput) == 1:
                    img = cmpt120imageManip.applyRedFilter(img)
                    cmpt120imageProjHelper.showInterface(img,"Apply Red Filter ", generateMenu(state))
                elif int(userInput) == 2:
                    img = cmpt120imageManip.applyGreenFilter(img)
                    cmpt120imageProjHelper.showInterface(img, "Apply Green Filter ", generateMenu(state))
                elif int(userInput) == 3:
                    img = cmpt120imageManip.applyBlueFilter(img)
                    cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter ", generateMenu(state))
                elif int(userInput) == 4:
                    img = cmpt120imageManip.applySepiaFilter(img)
                    cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter ", generateMenu(state))
                elif int(userInput) == 5:
                    img = cmpt120imageManip.applyWarmFilter(img)
                    cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter ", generateMenu(state))
                elif int(userInput) == 6:
                    img = cmpt120imageManip.applyColdFilter(img)
                    cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter ", generateMenu(state))
            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)

        elif state["mode"] == "advanced":
            if userInput ==  "6":
                print("Log: Performing " + advanced[int(userInput)-1])
                state["mode"] = "basic"
                cmpt120imageProjHelper.showInterface(img, "Basic ", generateMenu(state))
            elif int(userInput) > 0 and int(userInput) < 6:
                print("Log: Doing manipulation functionalities " + userInput)
                print("Log: Performing " + advanced[int(userInput)-1])  
                if int(userInput) == 1:
                    img = cmpt120imageManip.rotateLeft(img)
                    cmpt120imageProjHelper.showInterface(img, "Rotate Left ", generateMenu(state))  
                elif int(userInput) == 2:
                    img = cmpt120imageManip.rotateRight(img)
                    cmpt120imageProjHelper.showInterface(img, "Rotate Right ", generateMenu(state))    
                elif int(userInput) == 3:
                    img = cmpt120imageManip.doubleSize(img)
                    cmpt120imageProjHelper.showInterface(img, "Double Size ", generateMenu(state))
                elif int(userInput) == 4:
                    img = cmpt120imageManip.halfSize(img)
                    cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))
                elif int(userInput) == 5:
                    img = cmpt120imageManip.locateFish(img)
                    cmpt120imageProjHelper.showInterface(img, "Locate Fish ", generateMenu(state))
            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image

cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) 

# ***this is the event-loop of the application. ***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: 
            keepRunning = False
            
pygame.quit()

print("Log: Program Quit")
