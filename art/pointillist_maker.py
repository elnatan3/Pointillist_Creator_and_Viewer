from graphics import *
import tkinter as tk
from tkinter import filedialog
import random
import os

NUM_CIRCLES = 50000

def convert(imageFileName):
    '''
    This function uses the given image file to create a .art text file
    that contains the data that describes a "Pointillist" version of this image.
    
    Parameter: imageFileName (str): the complete file name of the image with extension gif
    '''
    # converting the image file name to lowercase
    imageFileName = imageFileName.lower()
    
    # using while to produce the error message if the the extension is not gif.
    if imageFileName[-3:] != 'gif':
        raise Exception("Invalid file format. Can only convert '.gif' files")
    imageCreated = Image(Point(0,0),imageFileName)
    slashIndex = imageFileName.rfind('/')
    pointIndex = imageFileName.rfind('.')
    fileExtension = imageFileName[slashIndex + 1: pointIndex]
    newFileExtension = f'{fileExtension}.art'
    
    # creating the folder .art_files if it does not exist
    if not os.path.exists('.art_files'):
        os.makedirs('.art_files')
    
    # saving the .art file in the .art_files folder
    fileName_out = open(f'.art_files/{newFileExtension}', 'w')
    imageWidth = imageCreated.getWidth()
    imageHeight = imageCreated.getHeight()
    
    #since both image width and image height are the same
    fileName_out.write(f'{imageWidth}\n')
    
    # creating a for loop to get the random x and y values and random color in the format(rgb).
    for i in range(NUM_CIRCLES):
        x = random.randrange(0, imageWidth)
        y = random.randrange(0, imageHeight)
        fileName_out.write(f'{x} {y}')
        rdbComponents = imageCreated.getPixel(x,y)
        colorLocation = f' {rdbComponents[0]} {rdbComponents[1]} {rdbComponents[2]}'
        fileName_out.write(f'{colorLocation}\n')

def main():
    # opens file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    initialdir = os.path.abspath("images")
    filePath = filedialog.askopenfilename(initialdir=initialdir)
    print("Converting:", filePath)
    convert(filePath)
    print("Finished. Enjoy your .art file!")
    
if __name__ == '__main__':
    main()
