from tkinter import *
import random
import pyperclip
import threading
import time

def createWindow():
    global receiver
    global receiverTwo
    global confirmed
    window = Tk()
    window.title("Secret maker")

    #empty is a empty space to make the programm better looking


    Title = Label(window, text="Encoder side", font=("calibri", 13))
    Title.grid(row = 0, column = 0)

    empty = Label(window, height = 2)
    empty.grid(row = 1, column = 0)

    receiver = Text(window, height = 10)
    receiver.grid(row = 2, column = 0)

    empty = Label(window, height = 2)
    empty.grid(row = 3, column = 0)

    encodeMe = Button(window, text="Encode and copy", command=lambda receiver = receiver: createEncoded(receiver.get('1.0','end'))
                      ,width = 15, height = 3, bg="Cyan")
    encodeMe.grid(row = 4, column = 0)

    sideLine = Label(window, text="-----------------------"*5)
    sideLine.grid(row = 5, column = 0)

    TitleTwo = Label(window, text="Decoder side", font=("calibri", 13))
    TitleTwo.grid(row = 6, column = 0)

    empty = Label(window, height = 2)
    empty.grid(row = 7, column = 0)

    receiverTwo = Text(window, height = 10)
    receiverTwo.grid(row = 8, column = 0)

    empty = Label(window, height = 2)
    empty.grid(row = 9, column = 0)

    decodeMe = Button(window, text="Decode", command=lambda receiverTwo = receiverTwo: createDecoded(receiverTwo.get('1.0','end'))
                      ,width = 15, height = 3, bg="Cyan")
    decodeMe.grid(row = 10, column = 0)

    confirmed = Label(window, text="")
    confirmed.grid(row = 11, column = 0)

    window.geometry("650x700")
    window.mainloop()

def createEncoded(textToEncode):
    global receiverTwo
    result = ""
    #substraction, multiplication, addition
    stringManipulator = [random.randint(2, 99), random.randint(2, 99), random.randint(2, 99)]
    for eachLetter in textToEncode:
        result += chr(((ord(eachLetter) + stringManipulator[0]) * stringManipulator[1]) - stringManipulator[2])
    result += chr(200 + stringManipulator[0]) + chr(300 + stringManipulator[1]) + chr(500 + stringManipulator[2])
    receiverTwo.delete('1.0','end')
    receiverTwo.insert('1.0', result)
    pyperclip.copy(result)
    confirmedTimer = threading.Thread(target = confirmedCommand)
    confirmedTimer.start()

def createDecoded(textToDecode):
    global receiver
    result = ""
    endKey = []
    #substraction, multiplication, addition
    content = textToDecode[:-4]
    codedShit = textToDecode[-4:-1]

    for Key in codedShit:
        endKey.append(int(str(ord(Key))[1:]))
    
    for eachLetter in content:
        result += str(chr(((ord(eachLetter) + endKey[2]) // endKey[1]) - endKey[0]))

    receiver.delete('1.0','end')
    receiver.insert('1.0', result)

def confirmedCommand():
    global confirmed
    confirmed.configure(text="Copied to keyboard")
    time.sleep(2)
    confirmed.configure(text="")

createWindow()
