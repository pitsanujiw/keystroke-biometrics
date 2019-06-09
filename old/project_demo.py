# use "1gram" for compare
# use dtw

from tkinter import *
from tkinter import messagebox
import time
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import json
import random

def first_submit():
    first_text.config(state='disabled')
    first_text.config(state='disabled')
    first_data.update({"keyPressed": first_keyPressed})
    first_data.update({"keyReleased": first_keyReleased})
    first_data.update({"keyCode": first_keyCode})

def first_clear():
    first_text.delete(0, END)
    first_keyPressed.clear()
    first_keyReleased.clear()
    first_keyCode.clear()

def first_keyup(e):
    now = int(round(time.time() * 1000))
    first_keyReleased.append(now - start)
    first_keyCode.append(ord(e.char))

def first_keydown(e):
    now = int(round(time.time() * 1000))
    first_keyPressed.append(now - start)

def second_submit():
    second_text.config(state='disabled')
    second_data.update({"keyPressed": second_keyPressed})
    second_data.update({"keyReleased": second_keyReleased})
    second_data.update({"keyCode": second_keyCode})

def second_clear():
    second_text.delete(0, END)
    second_keyPressed.clear()
    second_keyReleased.clear()
    second_keyCode.clear()

def second_keyup(e):
    now = int(round(time.time() * 1000))
    second_keyReleased.append(now - start)
    if e.char == '\x08':
        second_keyCode.append(8)
    else:
        second_keyCode.append(ord(e.char))

def second_keydown(e):
    now = int(round(time.time() * 1000))
    second_keyPressed.append(now - start)

def keep_data():
    if check_keyCode():
        sys.exit()

    first_data.update({"keyCode": first_keyCode})
    first_data.update({"keyPressed": first_keyPressed})
    first_data.update({"keyReleased": first_keyReleased})

    second_data.update({"keyCode": second_keyCode})
    second_data.update({"keyPressed": second_keyPressed})
    second_data.update({"keyReleased": second_keyReleased})

    for i in range(1, 6):
        first_data.update({str(i)+"gram":cal_ngram(i, first_keyPressed, first_keyReleased)})
        second_data.update({str(i)+"gram":cal_ngram(i, second_keyPressed, second_keyReleased)})
    first_data.update({"duration": cal_duration(first_keyPressed, first_keyReleased)})
    second_data.update({"duration": cal_duration(second_keyPressed, second_keyReleased)})

    write_path = "keep_data\\"
    number = random.randint(1,100001)
    write2json(first_data, write_path + str(number) + ".json")
    write2json(second_data, write_path + str(number) + "_1.json")

    calculate(first_data["1gram"], second_data["1gram"])

def calculate(trainingSet, testSet):
    dist, path = fastdtw(testSet, trainingSet, dist=euclidean)
    if dist < 200:
        messagebox.showinfo("Information","Status: Pass\nSimilarity is: " + str(dist))
        print("Information","Status: Pass\nSimilarity is: " + str(dist))
        print("--------------------------------------------------------------------------")
        sys.exit()
    else:
        messagebox.showerror("Error","Status: Failed\nSimilarity is: " + str(dist))
        print("Status: Failed\nSimilarity is: " + str(dist))
        print("--------------------------------------------------------------------------")
        sys.exit()

def cal_ngram(ngram, pressed, released):
    length = len(pressed)
    result = []
    for i in range(0, length-ngram, ngram):
        result.append(abs(released[i]-pressed[i+ngram]))
    return result

def cal_duration(pressed, released):
    length = len(pressed)
    result = []
    for i in range(length):
        result.append(abs(released[i]-pressed[i]))
    return result

def check_keyCode():
    if first_string.get() != second_string.get():
        messagebox.showerror("Error", "Text does not same!!")
        print("Error", "Text does not same!!")
        print("--------------------------------------------------------------------------")
        return True
    elif first_string.get() == "" and second_string.get() == "":
        messagebox.showerror("Error", "You must put some text!!")
        print("Error", "You must put some text!!")
        print("--------------------------------------------------------------------------")
        return True
    return False

def write2json(write_data, path):
    with open(path, "w") as files:
        json.dump(write_data, files)
        print(path + " -> write success")

print("--------------------------------------------------------------------------")

root = Tk()
root.title("Keystroke Biometrics(Demo Version)")
root.minsize(width=400, height=100)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

Label(root, text="Pleas enter first text", font=("Helvetica", 10)).grid(row=0)
Label(root, text="Pleas enter second text", font=("Helvetica", 10)).grid(row=1)

first_string = StringVar()
first_text = Entry(root, textvariable=first_string)
first_clear = Button(root, text="Clear", command=first_clear)
first_submit = Button(root, text="Submit", command=first_submit)

second_string = StringVar()
second_text = Entry(root, textvariable=second_string)
second_clear = Button(root, text="Clear", command=second_clear)
second_submit = Button(root, text="Submit", command=second_submit)

cal = Button(root, text="Calculate", command=keep_data)

first_text.grid(row=0, column=1)
first_clear.grid(row=0, column=2)
first_submit.grid(row=0, column=3)

second_text.grid(row=1, column=1)
second_clear.grid(row=1, column=2)
second_submit.grid(row=1, column=3)

cal.grid(row=2, column=1)

first_keyPressed = []
first_keyReleased = []
first_keyCode = []
second_keyPressed = []
second_keyReleased = []
second_keyCode = []

first_data = {}
second_data = {}

first_text.bind("<KeyPress>", first_keydown)
first_text.bind("<KeyRelease>", first_keyup)
second_text.bind("<KeyPress>", second_keydown)
second_text.bind("<KeyRelease>", second_keyup)

start = int(round(time.time() * 1000))

root.mainloop()

# tkMessageBox.showwarning("Warning","Could not start service")