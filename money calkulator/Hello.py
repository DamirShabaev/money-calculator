from tkinter import *
from tkinter import messagebox
from classes import * 
 
def sum_info():
    messagebox.showinfo("gui Python",
      int(label_1000_entry.get()) * 1000 * float(cur_1000.get())
    + int(label_500_entry.get()) * 500 * float(cur_500.get())
    + int(label_200_entry.get()) * 200 * float(cur_200.get())
    + int(label_100_entry.get()) * 100 * float(cur_100.get())
    + int(label_50_entry.get()) * 50 * float(cur_50.get())
    + int(label_20_entry.get()) * 20 * float(cur_20.get())
    + int(label_5_entry.get()) * 5 * float(cur_5.get()) 
    + int(label_2_entry.get()) * 2 * float(cur_2.get())) 

root = Tk()
root.geometry("600x470")
root.title("money calculator")
# заголовок 
bills_head = Label(text="bills",height=2,relief=GROOVE)
bills_head.grid(row=3,column=0,rowspan=3,sticky="n")
number_head = Label(text="number",height=2,relief=GROOVE)
number_head.grid(row=3,column=1,rowspan=3,sticky="n")
factor_head = Label(text="factor",height=2,relief=GROOVE)
factor_head.grid(row=3,column=2,rowspan=3,sticky="n")
rates_head_e = Entry(relief=GROOVE,width=7)
rates_head_e.grid(padx=5, pady=5,row=4,column=3,sticky="w")
rates_head_l = Label(text="rate",height=2,relief=GROOVE,width=6)
rates_head_l.grid(row=3,column=3,sticky="n")
rates_pointer = Label(text="pointer--->",height=2)
rates_pointer.grid(row=4,column=2,sticky="e")

rates_head_e.insert(0,1)

#Текстовая разметка номинала денег
label_1000 = Label(text="1000",height=2)
label_1000.grid(row=5,column=0,sticky="w")
label_500 = Label(text="500",height=2)
label_500.grid(row=6,column=0,sticky="w")
label_200 = Label(text="200",height=2)
label_200.grid(row=7,column=0,sticky="w")
label_100 = Label(text="100",height=2)
label_100.grid(row=8,column=0,sticky="w")
label_50 = Label(text="50",height=2)
label_50.grid(row=9,column=0,sticky="w")
label_20 = Label(text="20",height=2)
label_20.grid(row=10,column=0,sticky="w")
label_10 = Label(text="10",height=2)
label_10.grid(row=11,column=0,sticky="w")
label_5 = Label(text="5",height=2)
label_5.grid(row=12,column=0,sticky="w")
label_2 = Label(text="2",height=2)
label_2.grid(row=13,column=0,sticky="w")
label_1 = Label(text="1",height=2)
label_1.grid(row=14,column=0,sticky="w")

# Текстовая разметка для указания курса
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=5,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=6,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=7,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=8,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=9,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=10,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=11,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=12,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=13,column=2,sticky="w")
label_x = Label(text="x",height=2,width=5)
label_x.grid(row=14,column=2,sticky="w")

# устанавливаем поля ввода цифр напротив номиналов
label_1000_entry = Entry(width=7)
label_1000_entry.grid(row=5,column=1,sticky="e")
label_500_entry = Entry(width=7)
label_500_entry.grid(row=6,column=1,sticky="e")
label_200_entry = Entry(width=7)
label_200_entry.grid(row=7,column=1,sticky="e")
label_100_entry = Entry(width=7)
label_100_entry.grid(row=8,column=1,sticky="e")
label_50_entry = Entry(width=7)
label_50_entry.grid(row=9,column=1,sticky="e")
label_20_entry = Entry(width=7)
label_20_entry.grid(row=10,column=1,sticky="e")
label_10_entry = Entry(width=7)
label_10_entry.grid(row=11,column=1,sticky="e")
label_5_entry = Entry(width=7)
label_5_entry.grid(row=12,column=1,sticky="e")
label_2_entry = Entry(width=7)
label_2_entry.grid(row=13,column=1,sticky="e")
label_1_entry = Entry(width=7)
label_1_entry.grid(row=14,column=1,sticky="e")


# Устанавливаем поле ввода курса по которому нужно пересчитать 
cur_1000 = Entry(width=7)
cur_1000.grid(row=5,column=3)
cur_500 = Entry(width=7)
cur_500.grid(row=6,column=3)
cur_200 = Entry(width=7)
cur_200.grid(row=7,column=3)
cur_100 = Entry(width=7)
cur_100.grid(row=8,column=3)
cur_50 = Entry(width=7)
cur_50.grid(row=9,column=3)
cur_20 = Entry(width=7)
cur_20.grid(row=10,column=3)
cur_10 = Entry(width=7)
cur_10.grid(row=11,column=3)
cur_5 = Entry(width=7)
cur_5.grid(row=12,column=3)
cur_2 = Entry(width=7)
cur_2.grid(row=13,column=3)
cur_1 = Entry(width=7)
cur_1.grid(row=14,column=3)


#Устанавливаем в полях ввода кол-ва - 0
label_1000_entry.insert(0,0)
label_500_entry.insert(0,0)
label_200_entry.insert(0,0)
label_100_entry.insert(0,0)
label_50_entry.insert(0,0)
label_20_entry.insert(0,0)
label_10_entry.insert(0,0)
label_5_entry.insert(0,0)
label_2_entry.insert(0,0)
label_1_entry.insert(0,0)

# Устанавливаем в полях ввода курса - 1.0
cur_1000.insert(0,1)
cur_500.insert(0,1)
cur_200.insert(0,1)
cur_100.insert(0,1)
cur_50.insert(0,1)
cur_20.insert(0,1)
cur_10.insert(0,1)
cur_5.insert(0,1)
cur_2.insert(0,1)
cur_1.insert(0,1)

def check1():
    if check == 1:
        cur_1000.insert(0,rates_head_e.get()
    

check = IntVar()
check.set(-1)
check1 = Checkbutton(variable=check,onvalue=1,offvalue=0,command=check1)
check1.grid(row=4,column=1)


# здесь будут кнопки
sum_btn = Button(text="Total",command=sum_info)
sum_btn.place(relx=.8, rely=.9, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()

