#Pyhton mega course project1 source code

from tkinter import *
from tkinter.messagebox import *

font = ('Verdana', 22, 'bold')


def buttonClick(event):
    b = event.widget
    text = b['text']

    if(text == '='):
        try:
            expression = textField.get()
            answer = eval(expression)
            textField.delete(0, END)
            textField.insert(0,  answer)
        except ZeroDivisionError:
            showerror("You can't divide the number by 0.")
        except Exception:
            showerror('Oops! The expression is invalid.')
        return

    textField.insert(END, text)

def allClear():
    textField.delete(0, END)

def clear():
    expression = textField.get()
    expression = expression[0:len(expression) - 1]
    textField.delete(0, END)
    textField.insert(0, expression)

# creating a window

window = Tk()
window.title("Matthew's Calculator")
window.geometry('450x600')


# heading Label
heading = Label(window, text = "Matthew's Calculator", font=font, underline=0)
heading.pack(side=TOP, pady=10)

# textfield

textField = Entry(window, font = font, justify=CENTER)
textField.pack(side=TOP, pady = 20, fill=X, padx = 20)


# buttons
frame = Frame(window)
frame.pack(side=TOP)

#Adding buttons now

btnVlaue = 1
for i in range(3):
    for j in range(3):
        button = Button(frame, text = btnVlaue, font=font, width=5, height=2,
                        relief='sunken', activebackground ='red', activeforeground='white')
        button.grid(row=i, column=j, padx=3, pady=3)
        btnVlaue+=1
        button.bind('<Button-1>', buttonClick)

dotbutton = Button(frame, text=".", font=font, width=5, height=2, relief='sunken')
dotbutton.grid(row=3, column=0, padx=3, pady=3)

zerobutton = Button(frame, text="0", font=font, width=5, height=2, relief='sunken')
zerobutton.grid(row=3, column=1, padx=3, pady=3)

equalbutton = Button(frame, text="=", font=font, width=5, height=2, relief='sunken')
equalbutton.grid(row=3, column=2, padx=3, pady=3)

plusButton = Button(frame, text="+", font=font, width=5, height=2, relief='sunken')
plusButton.grid(row=0, column=3, padx=3, pady=3)

minusButton = Button(frame, text="-", font=font, width=5, height=2, relief='sunken')
minusButton.grid(row=1, column=3, padx=3, pady=3)

multiplyButton = Button(frame, text="*", font=font, width=5, height=2, relief='sunken')
multiplyButton.grid(row=2, column=3, padx=3, pady=3)

divideButton = Button(frame, text="/", font=font, width=5, height=2, relief='sunken')
divideButton.grid(row=3, column=3, padx=3, pady=3)

clearButton = Button(frame, text="C", font=font, width=11, height=2, relief='sunken', command=clear)
clearButton.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

allClearButton = Button(frame, text="AC", font=font, width=11, height=2, relief='sunken', command=allClear)
allClearButton.grid(row=4, column=2, columnspan=2, padx=3, pady=3)


for btn in [dotbutton, zerobutton, equalbutton, plusButton, minusButton, multiplyButton, divideButton]:
    btn.bind('<Button-1>', buttonClick)

# dotbutton.bind('<Button-1>', buttonClick)
# zerobutton.bind('<Button-1>', buttonClick)
# equalbutton.bind('<Button-1>', buttonClick)
# plusButton.bind('<Button-1>', buttonClick)
# minusButton.bind('<Button-1>', buttonClick)
# multiplyButton.bind('<Button-1>', buttonClick)
# divideButton.bind('<Button-1>', buttonClick)

window.mainloop()

