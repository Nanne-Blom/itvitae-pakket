from tkinter import *

root = Tk()
root.title("Rekenmachine")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_ac():
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "optellen"
    f_num = int(first_number)
    e.delete(0, END)

def button_min():
    first_number = e.get()
    global f_num
    global math
    math = "aftrekken"
    f_num = int(first_number)
    e.delete(0, END)

def button_deel():
    first_number = e.get()
    global f_num
    global math
    math = "delen"
    f_num = int(first_number)
    e.delete(0, END)

def button_keer():
    first_number = e.get()
    global f_num
    global math
    math = "vermenigvuldigen"
    f_num = int(first_number)
    e.delete(0, END)

def button_is():
    second_number = e.get()
    e.delete(0, END)

    if math == "optellen":
        e.insert(0, f_num + int(second_number))

    if math == "aftrekken":
        e.insert(0, f_num - int(second_number))

    if math == "delen":
            e.insert(0, f_num / int(second_number))

    if math == "vermenigvuldigen":
        e.insert(0, f_num * int(second_number))



button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20, command= button_plus)
button_min = Button(root, text="-", padx=41, pady=20, command= button_min)
button_deel = Button(root, text="÷", padx=40, pady=20, command= button_deel)
button_keer = Button(root, text="x", padx=41, pady=20, command= button_keer)
button_ac = Button(root, text="AC", padx=35, pady=20, command= button_ac)
button_is = Button(root, text="=", padx=39, pady=20, command= button_is)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_ac.grid(row=4, column=1)
button_plus.grid(row=1, column=4)
button_min.grid(row=2, column=4)
button_deel.grid(row=3, column=4)
button_keer.grid(row=4, column=4)
button_is.grid(row=4, column=2)

root.mainloop()
