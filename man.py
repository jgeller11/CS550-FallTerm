#Jonathan Geller
#10/30/17

# original code from:
# http://code.activestate.com/recipes/578590-mandelbrot-fractal-using-tkinter/
# all other code is my own

import math
import tkinter 
from tkinter import *


#Function that actually does the mandlebrot set calculations
def iter(z,c,q):
    if abs(z)>2:
        return q
    if q==0:
        return 0
    return iter(z**2+c,c,q-1)

#Function that takes inputs for a region of the complex plane and plots the mandlebrot set in that region
def plot(xmin,xmax,ymin,ymax):    
    for row in range(h): #These loops cycle through each pixel in order to plot it
        for col in range(w):
            q = iter(0,complex(col*(xmax-xmin)/w+xmin,row*(ymax-ymin)/h+ymin),126)
            r = hex(abs(255-4*q)%256)[2:].zfill(2) #function that determines color
            img.put('#' + r + r + r, (col, h-row))
    c.pack()
    c.update()
    name=input('Press enter to begin loading next image, type a name to save image as a file with chosen name.')
    if name!='': #Unless the user didn't type anything in...
        c.postscript(file='Mandlebrot'+name.title()+'.ps', colormode='color') #Save image to the parent folder with name Mandlebrot'Input'.ps

window = tkinter.Tk()

#Gathers data about screen size to size window as correctly as possible
wmax = window.winfo_screenwidth()
hmax = window.winfo_screenheight()

w=(min(wmax,hmax)*9)//10
h=w

#Create a new canvas with an image within it
c = Canvas(window, width = w, height = h, bg = "#000000")
img = PhotoImage(width = w, height = h)
c.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

print('Please wait.') #Just assures the user that the program did indeed start
plot(-0.311634981,-0.311635001,0.63674999,0.63675001) #the four default images
plot(-0.3117,-0.3116,0.6367,0.6368)                   #zoomed out
plot(-0.312,-0.3113,0.6364,0.6371)                    #zoomed out again
plot(-0.311,-0.3103,0.6374,0.6381)                    #shifted a bit

#Plotting user-input regions
rep=False
if input('Would you like to try some regions of your own? ').lower()[0]=='y':
    rep=True
while rep:
    x1=float(input('Lower x value? '))
    x2=float(input('Upper x value? '))
    y1=float(input('Lower y value? '))
    y2=float(input('Upper y value? '))
    print('Loading...')
    if x1>=x2 or y1>=y2 or abs(math.log((x2-x1)/(y2-y1)))>1: #if the region is backwards, or very out of proportion, user retries
        print('It appears there was an error with your entry, please check your values.')
    else:
        if ((x2-x1)/wmax)<((y2-y1)/hmax): #Sets the dimensions of the window to be optimal for the dimensions of the region
            h=hmax 
            w=round(h*(x2-x1)/(y2-y1))
        else:
            w=wmax
            h=round(w*(y2-y1)/(x2-x1))
        c.destroy() #Replacing old canvas in order to resize
        c = Canvas(window, width = w, height = h, bg = "#000000")
        img = PhotoImage(width = w, height = h)
        c.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)
        plot(x1,x2,y1,y2) #Plot user input        
    if input('Another one? ').lower()[0]!='y':
        rep=False