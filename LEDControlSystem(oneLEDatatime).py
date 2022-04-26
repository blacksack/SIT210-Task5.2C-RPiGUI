from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

#CREATE LED VARIABLES AND ASSIGN TO PINOUT ON RASPBERRY PI
greenLED = LED(18)
blueLED = LED(15)
redLED = LED(14)

#GUI ASSEMBLY 
win = Tk()
win.title("LED Control System")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#FUNCTIONS 
def greenLEDToggle():
  
    if greenLED.is_lit:
        greenLED.off()
        greenLEDButton["text"] = "Turn Green LED On"
  
    else:
        greenLED.on()
        blueLED.off()
        redLED.off()
        greenLEDButton["text"] = "Turn Green LED Off"
        blueLEDButton["text"] = "Turn Blue LED On"
        redLEDButton["text"] = "Turn Red LED On"
        

def blueLEDToggle():
    if blueLED.is_lit:
        blueLED.off()
        blueLEDButton["text"] = "Turn Blue LED On"
        
    else:
        blueLED.on()
        greenLED.off()
        redLED.off()
        
        blueLEDButton["text"] = "Turn Blue LED Off"
        greenLEDButton["text"] = "Turn Green LED On"
        redLEDButton["text"] = "Turn Red LED On"

def redLEDToggle():
    if redLED.is_lit:
        redLED.off()
        redLEDButton["text"] = "Turn Red LED On"
        
    else:
        redLED.on()
        greenLED.off()
        blueLED.off()
        
        redLEDButton["text"] = "Turn Red LED Off"
        greenLEDButton["text"] = "Turn Green LED On"
        redLEDButton["text"] = "Turn Red LED On"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


#WIDGET ASSEMBLERS
greenLEDButton = Button(win, text = 'Turn Green LED On', font = myFont, command = greenLEDToggle, bg = 'bisque2', height = 1, width = 24)
greenLEDButton.grid(row = 0, column = 1)

blueLEDButton = Button(win, text = 'Turn Blue LED On', font = myFont, command = blueLEDToggle, bg = 'bisque2', height = 1, width = 24)
blueLEDButton.grid(row = 1, column = 1)

redLEDButton = Button(win, text = 'Turn Red LED On', font = myFont, command = redLEDToggle, bg = 'bisque2', height = 1, width = 24)
redLEDButton.grid(row = 2, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row = 3, column = 1)

win.protocol("WM DELETE WINDOW", close)                 ##EXIT FROM WINDOW AND CLEAN GPIOS ETC.
win.mainloop()                                          ##FOREVER LOOP 
