# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Julkar Naine Reedoy
# Date: Dec. 5, 2021
# Description: Contains all the functions for image manipulation
# Developed and tested on Visual Studio Code and Idle (Python 3.9.8 64-bit)

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120imageProjHelper

#import numpy

# Basic red filter
def applyRedFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            pixel[1] = 0
            pixel[2] = 0
    return img

# Basic green filter
def applyGreenFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            pixel[0] = 0
            pixel[2] = 0
    return img

# Basic blue filter
def applyBlueFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            pixel[0] = 0
            pixel[1] = 0
    return img

# Sepia filter
def applySepiaFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            # Converting r,g,b to float type
            for i in range(3):
                pixel[i] = float(pixel[i])
            # r,g,b value calculations
            sepiaRed = (pixel[0]*0.393) + (pixel[1]*0.769) + (pixel[2]*0.189)
            sepiaGreen = (pixel[0]*0.349) + (pixel[1]*0.686) + (pixel[1]*0.168)
            sepiaBlue = (pixel[0]*0.272) + (pixel[1]*0.534) + (pixel[2]*0.131)
            # Reassign r,g,b values to current pixel
            pixel[0] = int(min(sepiaRed,255))
            pixel[1] = int(min(sepiaGreen,255))
            pixel[2] = int(min(sepiaBlue,255))
    return img

# Warm filter
def applyWarmFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            red = float(pixel[0])
            blue = float(pixel[2])
            
            # Calculation for red value
            if red < 64 :
                red = red/(64*80)
            elif red >= 64 and red < 128:
                red = (red-64)/(128-64)*(160-80)+80
            else:
                red = (red-128)/(255-128)*(255-160)+160
            pixel[0] = int(red)
            
            # Calculation for blue value
            if blue < 64:
                blue = blue/(64*50)
            elif blue >= 64 and blue < 128:
                blue = (blue-64)/(128-64)*(100-50)+50
            else:
                blue = (blue-128)/(255-128)*(255-100)+100
            pixel[2] = int(blue)

    return img

# Cold filter
def applyColdFilter(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            red = float(pixel[0])
            blue = float(pixel[2])
            
            # Calculation for blue
            if blue < 64 :
                blue = blue/(64*80)
            elif blue >= 64 and blue < 128:
                blue = (blue-64)/(128-64)*(160-80)+80
            else:
                blue = (blue-128)/(255-128)*(255-160)+160
            pixel[2] = int(blue)

            # Calculation for red
            if red < 64:
                red = red/64*50
            elif red >= 64 and red < 128:
                red = (red-64)/(128-64)*(100-50)+50
            else:
                red = (red-128)/(255-128)*(255-100)+100
            pixel[0] = int(red)

    return img

# Rotate right function
def rotateRight(img):
    height = len(img)
    width = len(img[0])
    # Gets new black image
    newImage = cmpt120imageProjHelper.getBlackImage(height, width)
    # For loop to copy over pixels
    for row in range(height):
        for col in range(width):
            newImage[-col][row] = img[-row][-col]
    return newImage

# Rotate left function
def rotateLeft(img):
    height = len(img)
    width = len(img[0])
    # Gets new black image
    newImage = cmpt120imageProjHelper.getBlackImage(height,width)
    # For loop to copy over pixels
    for row in range(height):
        for col in range(width):
            newImage[col][-row] = img[-row][-col]
    return newImage

# Double size function
def doubleSize(img):
    height = len(img)
    width = len(img[0])
    # Gets new black image
    newImage = cmpt120imageProjHelper.getBlackImage(width*2,height*2) 
    for row in range(height):
        for col in range(width):
            # For loop to copy over pixels to new image
            pixel = img[row][col]
            newImage[row*2][col*2] = pixel
            newImage[(row*2)+1][(col*2)] = pixel
            newImage[(row*2)][(col*2)+1] = pixel
            newImage[(row*2)+1][(col*2)+1] = pixel
    return newImage

# Half size function
def halfSize(img):
    height = len(img)
    width = len(img[0])
    # Gets new black image
    newImage = cmpt120imageProjHelper.getBlackImage((width//2),(height//2))
    for row in range(height):
        for col in range(width):
            # For loop to assign pixels to variables
            pixel1 = img[row][col]
            pixel2 = img[row][col-1]
            pixel3 = img[row-1][col]
            pixel4 = img[row-1][col-1]
            # Calculation to find average of r,g,b values
            red = float((pixel1[0]+pixel2[0]+pixel3[0]+pixel4[0])/4)
            green = float((pixel1[1]+pixel2[1]+pixel3[1]+pixel4[1])/4)
            blue = float((pixel1[2]+pixel2[2]+pixel3[2]+pixel4[2])/4)
            # Assigns r,g,b values to the pixel in the new image
            newImage[int(row/2)][int(col/2)] = [int(red), int(green), int(blue)]
    return newImage

# Huge function to find the fish
def locateFish(img):
    height = len(img)
    width = len(img[0])
    # Two lists to contain row and column values
    col_num = []
    row_num = []
    # Boolean variable use to break out of loops in the function
    found = False

    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            # Use of provided hsv function
            hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)

            if (hsv[0] > 41 and hsv[0] < 71) and (hsv[1] > 9 and hsv[1] < 101) and (hsv[2] > 91 and hsv[2] < 101):
                # Finds and stores top of the fish in a row value
                row_num.append(row)
                found = True
                # Iterates the rows on the same column from bottom to up until bottom of fish is found
                for i in range((height-1),row,-1):
                    pixel = img[i][col]
                    r = pixel[0]
                    g = pixel[1]
                    b = pixel[2]
                    hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)

                    if (hsv[0] > 41 and hsv[0] < 71) and (hsv[1] > 9 and hsv[1] < 101) and (hsv[2] > 91 and hsv[2] < 101):
                        # Stores the bottom of the fish in a bottom value
                        row_num.append(i)
                        break
                # These break statements are used to break out of these loops
                break
            else:
                continue
        if found == True:
            # Boolean value used to break out of loop
            break
    
    # Assigns list values to variables used later to draw the box
    row_min = int(row_num[0])
    row_max = int(row_num[1])
    
    # Resets boolean variable which will be used once more
    found = False
    for col in range(width):
        for row in range((row_min),(row_max)):
            pixel = img[row][col]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)

            if (hsv[0] > 41 and hsv[0] < 71) and (hsv[1] > 9 and hsv[1] < 101) and (hsv[2] > 91 and hsv[2] < 101):
                # Finds and stores left end of the fish in a column value
                col_num.append(col)
                found  = True

                for i in range((width-1),col,-1):
                    pixel = img[row][i]
                    r = pixel[0]
                    g = pixel[1]
                    b = pixel[2]
                    hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)

                    if (hsv[0] > 41 and hsv[0] < 71) and (hsv[1] > 9 and hsv[1] < 101) and (hsv[2] > 91 and hsv[2] < 101):
                        # The column value for the right end of the fish
                        col_num.append(i)
                        break
                # More break statements
                break
            else:
                continue
        if found == True:
            # Final use of boolean value
            break
    
    # Assigns list values to variables used later to draw the box
    col_max = int(col_num[1])
    col_min = int(col_num[0])

    # Was used to check if code above works properly
    # print(col_min,col_max)
    # print(row_max,row_min)
    
    # Two for loops
    # One draw vertical lines and the other draws horizontal lines
    for a in range(col_min,col_max):
        pixel = img[row_min][a]
        pixel2 = img[row_max][a]

        # Changes r,g,b values to turn pixel green
        pixel[0] = 0
        pixel[1] = 255
        pixel[2] = 0

        pixel2[0] = 0
        pixel2[1] = 255
        pixel2[2] = 0

    # Second for loop
    for b in range(row_min,row_max):
        pixel = img[b][col_min]
        pixel2 = img[b][col_max]

        pixel[0] = 0
        pixel[1] = 255
        pixel[2] = 0

        pixel2[0] = 0
        pixel2[1] = 255
        pixel2[2] = 0
    
    return img
    # End of very large function






            




        
