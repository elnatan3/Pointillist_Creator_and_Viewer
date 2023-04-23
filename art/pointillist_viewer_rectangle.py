from graphics import *
import tkinter as tk
from tkinter import filedialog
import time
import os

WINDOW_SIZE = 600
DOT_SIZE = 3


def display(artFileName):
    '''
    This function reads from the given .art text file,
    and displays the Pointillist artwork in a window.

    artFileName (str)-- the complete filename of the file with .art extension
    '''
    # While loop to print an error message if the extension is not .art that was created from the art maker
    if artFileName[-3:] != 'art':
        raise Exception("Invalid file format. Can only display '.art' files.")
    window = GraphWin("Magic Art Viewer", WINDOW_SIZE, WINDOW_SIZE)
    window.setBackground("black")
    fileName = open(artFileName, 'r')
    imageSize = fileName.readline()
    
    # for loop to retrieve x, y, and color values of each line
    for eachLine in fileName:
        eachLine = eachLine.split()
        xValue = int(eachLine[0])
        yValue = int(eachLine[1])
        colorRed = int(eachLine[2])
        colorGreen = int(eachLine[3])
        colorBlue = int(eachLine[4])
        
        # if function to scale the x and y values to fit the window
        if int(imageSize) < WINDOW_SIZE or int(imageSize) > WINDOW_SIZE:
            xValue = (xValue / int(imageSize)) * WINDOW_SIZE
            yValue = (yValue / int(imageSize)) * WINDOW_SIZE
            squareDot = Rectangle(Point(xValue,yValue), Point(xValue+10,yValue+10))
            squareDot.setFill(color_rgb(colorRed, colorGreen, colorBlue))
            squareDot.draw(window)
        else:
            squareDot = Rectangle(Point(xValue,yValue), Point(xValue+10,yValue+10))
            squareDot.setFill(color_rgb(colorRed, colorGreen, colorBlue))
            squareDot.draw(window)    
        
def main():
    root = tk.Tk()
    root.withdraw()
    art_folder_path = os.path.abspath("./.art_files")
    if not os.path.exists(art_folder_path):
        os.mkdir(art_folder_path)
    art_file_path = filedialog.askopenfilename(initialdir=art_folder_path, title="Select an art file", filetypes=(("Art files", "*.art"), ("All files", "*.*")))
    if art_file_path:
        display(art_file_path)


if __name__ == '__main__':
    main()

