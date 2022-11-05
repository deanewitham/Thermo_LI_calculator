from tkinter import *

# Thermo LI helper

root = Tk()
root.geometry('400x200')
root.title("Linear Interpolation Calculator")


def calculate():
    X1 = float(X_1.get())
    X2 = float(X_2.get())
    X3 = float(X_3.get())
    Y1 = float(Y_1.get())
    Y3 = float(Y_3.get())
    Y2 = Y1 + (((X2 - X1) / (X3 - X1)) * (Y3 - Y1))
    result_message = Label(root, text="The Y2 value is: " + str(round(Y2, 4)))
    result_message.grid(row=7, column=0)


reminder = Label(root, text="Remember - the Y values are what you're solving for")
reminder.grid(row=0, column=0, columnspan=2)

x1 = Label(root, text="Enter the first X value: ").grid(row=1, column=0)
X_1 = Entry(root)
X_1.grid(row=1, column=1)

x2 = Label(root, text="Enter the second X value: ").grid(row=2, column=0)
X_2 = Entry(root)
X_2.grid(row=2, column=1)

x3 = Label(root, text="Enter the third X value: ").grid(row=3, column=0)
X_3 = Entry(root)
X_3.grid(row=3, column=1)

y1 = Label(root, text="Enter the Y value that corresponds to X1: ").grid(row=4, column=0)
Y_1 = Entry(root)
Y_1.grid(row=4, column=1)

y3 = Label(root, text="Enter the Y value that corresponds to X3: ").grid(row=5, column=0)
Y_3 = Entry(root)
Y_3.grid(row=5, column=1)

calc_button = Button(root, text="Calculate", command=calculate).grid(row=6, column=0)

root.mainloop()
