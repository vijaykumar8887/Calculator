from tkinter import *

font = ('Verdana', 18, 'bold')


# important function

def clearALL():
    textField.delete(0, END)


def clearOne():
    ex = textField.get()
    ex = ex[0: len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)
    pass


def click_btn(event):
    print('btn clicked')
    b = event.widget
    text = b['text']
    print(text)
    if text == '=':
        try:
            ex = textField.get()
            ans = eval(ex)
            textField.delete(0, END)
            textField.insert(0, ans)
        except:
            textField.delete(0, END)
            textField.insert(0, 'Error')
        return
    textField.insert(END, text)


# Creating a root
root = Tk()

root.title('Calculator')
root.geometry('300x400')
root.minsize(300, 400)
root.maxsize(300, 400)

# picture label
pic = PhotoImage(file='image1.png')
headingLabel = Label(root, image=pic)
headingLabel.pack(side=TOP, pady=1)

# heading label
heading = Label(root, text='Calculator', font=font)
heading.pack()

# textField
textField = Entry(root, font=font, justify=RIGHT)
textField.pack(side=TOP, pady=5, fill=X, padx=18)

# Button
buttonFrame = Frame(root)
buttonFrame.pack(side=TOP)

# adding  Numeric Button
num = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(num), font=10, width=5, relief='ridge')
        btn.grid(row=i, column=j, padx=1, pady=1)
        num += 1
        btn.bind('<Button-1>', click_btn)

# symbolic button

ZeroBtn = Button(buttonFrame, text='0', font=10, width=5, relief='ridge')
ZeroBtn.grid(row=3, column=0, padx=1, pady=1)

dotBtn = Button(buttonFrame, text='.', font=10, width=5, relief='ridge')
dotBtn.grid(row=3, column=1, padx=1, pady=1)

EqualBtn = Button(buttonFrame, text='=', font=10, width=5, relief='ridge')
EqualBtn.grid(row=3, column=2, padx=1, pady=1)

plusBtn = Button(buttonFrame, text='+', font=10, width=5, relief='ridge')
plusBtn.grid(row=0, column=3, padx=1, pady=1)

minusBtn = Button(buttonFrame, text='-', font=10, width=5, relief='ridge')
minusBtn.grid(row=1, column=3, padx=1, pady=1)

multiBtn = Button(buttonFrame, text='*', font=10, width=5, relief='ridge')
multiBtn.grid(row=2, column=3, padx=1, pady=1)

deviBtn = Button(buttonFrame, text='/', font=10, width=5, relief='ridge')
deviBtn.grid(row=3, column=3, padx=1, pady=1)

clearBtn = Button(buttonFrame, text='X', font=10, width=12, relief='ridge', command=clearOne)
clearBtn.grid(row=4, column=0, padx=1, pady=1,columnspan=2)

resetBtn = Button(buttonFrame, text='AC', font=10, width=12, relief='ridge', command=clearALL)
resetBtn.grid(row=4, column=2, padx=1, pady=1, columnspan=2,)

# binding all btn
plusBtn.bind('<Button-1>', click_btn)
minusBtn.bind('<Button-1>', click_btn)
multiBtn.bind('<Button-1>', click_btn)
deviBtn.bind('<Button-1>', click_btn)
dotBtn.bind('<Button-1>', click_btn)
ZeroBtn.bind('<Button-1>', click_btn)
EqualBtn.bind('<Button-1>', click_btn)

root.mainloop()
