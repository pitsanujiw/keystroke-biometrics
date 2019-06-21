from tkinter import *
import time

def keyup(e):
    now = int(round(time.time() * 1000))
    # print('up', e.char)
    # print(now - start)
    KeyReleased.append(now - start)
    keyCode.append(e.char)

def keydown(e):
    now = int(round(time.time() * 1000))
    # print('down', e.char)
    # print(now - start)
    first_keyPressed.append(now - start)

def clear():
    first_text.delete(0, END) # clear the entry field

def submit():
    first_text.config(state='disabled')

root = Tk()
root.title("Keystroke Biometrics Demo")
root.minsize(width=100, height=100)

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# print("Width",windowWidth,"Height",windowHeight)
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

Label(root, text="First Text").grid(row=0)
clear_button = Button(root, text="Clear", command=clear)
submit_button = Button(root, text="Submit", command=submit)
# Label(root, text="Second Text").grid(row=1)

first_text = Entry(root)
# second_text = Entry(root)

first_text.grid(row=0, column=1)
clear_button.grid(row = 0, column = 2)
submit_button.grid(row = 0, column = 3)
# second_text.grid(row=1, column=1)

first_keyPressed = []
KeyReleased = []
keyCode = []

first_text.bind("<KeyPress>", keydown)
first_text.bind("<KeyRelease>", keyup)
# second_text.bind("<KeyRelease>", keyup)

# frame = Frame(root, width=100, height=100)
# frame.bind("<KeyPress>", keydown)
# frame.bind("<KeyRelease>", keyup)
# frame.pack()
# frame.focus_set()

start = int(round(time.time() * 1000))
root.mainloop()

print(first_keyPressed)
print(KeyReleased)
print(keyCode)