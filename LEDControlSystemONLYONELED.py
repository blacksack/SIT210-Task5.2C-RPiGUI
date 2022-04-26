from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

#CREATE LED VARIABLES AND ASSIGN TO PINOUT ON RASPBERRY PI
greenLED = LED(18)
blueLED = LED(15)
redLED = LED(14)
toggle = IntVar()

#GUI ASSEMBLY 
win = Tk()
win.title("LED Control System")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#FUNCTIONS 
def LEDToggle():
    toggleStage = toggle.get()
    if toggleStage == 1:
       greenLED.on()
       greenLEDButton["text"] = "Turn Green LED Off"
       blueLED.off()
       blueLEDButton["text"] = "Turn Blue LED On"
       redLED.off()
       redLEDButton["text"] = "Turn Red LED On"
      
    elif toggleStage == 2:
       greenLED.off()
       greenLEDButton["text"] = "Turn Green LED On"
       blueLED.on()
       blueLEDButton["text"] = "Turn Blue LED Off"
       redLED.off()
       redLEDButton["text"] = "Turn Red LED On"

     elif toggleStage == 3:
       greenLED.off()
       greenLEDButton["text"] = "Turn Green LED On"
       blueLED.off()
       blueLEDButton["text"] = "Turn Blue LED On"
       redLED.on()
       redLEDButton["text"] = "Turn Red LED Off"
      
     else:
       greenLED.off()
       greenLEDButton["text"] = "Turn Green LED On"
       blueLED.off()
       blueLEDButton["text"] = "Turn Blue LED On"
       redLED.off()
       redLEDButton["text"] = "Turn Red LED On"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


#WIDGET ASSEMBLERS
greenLEDButton = Radiobutton(win, text = 'Turn Green LED On', font = myFont, variable = toggleStage, toggleStage = 1, bg = 'bisque2', height = 1, width = 24)
greenLEDButton.grid(row = 0, column = 1)

blueLEDButton = Radiobutton(win, text = 'Turn Blue LED On', font = myFont, variable = toggleStage, toggleStage = 2, bg = 'bisque2', height = 1, width = 24)
blueLEDButton.grid(row = 1, column = 1)

redLEDButton = Radiobutton(win, text = 'Turn Red LED On', font = myFont, variable = toggleStage, toggleStage = 3, bg = 'bisque2', height = 1, width = 24)
redLEDButton.grid(row = 2, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row = 3, column = 1)

win.protocol("WM DELETE WINDOW", close)                 ##EXIT FROM WINDOW AND CLEAN GPIOS ETC.
win.mainloop()                                          ##FOREVER LOOP 
