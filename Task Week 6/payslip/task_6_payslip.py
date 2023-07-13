from tkinter import *
from tkinter import messagebox
import tempfile
import os

root = Tk()
root.title('Payment Slip')
root.iconbitmap(r"C:\Users\yatim\Documents\YoShop\Task Week 6\payslip\banner_logo_40.ico")
root.configure(background='#2D9290')

text_label = Label(root,text='Payslip for the Employees',fg='white',bg='black',relief=GROOVE,justify=CENTER)
text_label.pack(pady=(10,10))
text_label.config(font=('times new roman',32,'bold'))

F1 = LabelFrame(root, text='Employee Details', font=('times new romon', 18, 'bold'), fg='black',bg='#2D9290',bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=900,height=650)

Name_label = Label(F1,text = 'Name',fg='white',bg='teal')
# Name_label.pack(pady=(20,10))
Name_label.config(font=('times new rommon',20))
Name_label.grid(row=0,column=0,padx=30,pady=30)

Name_input = Entry(F1,width=20,bg='black',fg='white')
# Name_input.pack(pady=(30,10))
Name_input.config(font=('verdana',20))
Name_input.grid(row=1,column=0,padx=30,pady=25)


basic_salary = Label(F1,text = 'Basic Salary',fg='white',bg='teal')
# basic_salary.pack(pady=(20,10))
basic_salary.config(font=('times new rommon',20))
basic_salary.grid(row=0,column=1,padx=30,pady=30)

basic_salary_input = Entry(F1,width=20,bg='black',fg='white')
# basic_salary_input.pack(pady=(30,10))
basic_salary_input.config(font=('verdana',20))
basic_salary_input.grid(row=1,column=1,padx=30,pady=25)

Allowance = Label(F1,text = 'Allowance',fg='white',bg='teal')
# Allowance.pack(pady=(20,10))
Allowance.config(font=('times new rommon',20))
Allowance.grid(row=2,column=0,padx=30,pady=30)

Allowance_input = Entry(F1,width=20,bg='black',fg='white')
# Allowance_input.pack(pady=(30,10))
Allowance_input.config(font=('verdana',20))
Allowance_input.grid(row=3,column=0,padx=30,pady=25)

Total_Leave = Label(F1,text = 'Total Leave',fg='white',bg='teal')
# Total_Leave.pack(pady=(20,10))
Total_Leave.config(font=('times new rommon',20))
Total_Leave.grid(row=2,column=1,padx=30,pady=30)

Total_Leave_input = Entry(F1,width=20,bg='black',fg= 'white')
# Total_Leave_input.pack(pady=(30,10))
Total_Leave_input.config(font=('verdana',20))
Total_Leave_input.grid(row=3,column=1,padx=30,pady=25)

Balance_Leave = Label(F1,text = 'Balance Leave',fg='white',bg='teal')
# Balance_Leave.pack(pady=(20,10))
Balance_Leave.config(font=('times new rommon',20))
Balance_Leave.grid(row=4,column=0,padx=30,pady=30)

Balance_Leave_input = Entry(F1,width=20,bg='black', fg='white' )
# Balance_Leave_input.pack(pady=(30,10))
Balance_Leave_input.config(font=('verdana',20))
Balance_Leave_input.grid(row=5,column=0,padx=30,pady=25)

Total = Label(F1,text = 'Total',fg='white',bg='teal')
# Total_Leave.pack(pady=(20,10))
Total.config(font=('times new rommon',20))
Total.grid(row=4,column=1,padx=30,pady=30)

Total_input = Entry(F1,width=20,bg='black',fg= 'white')
# Total_Leave_input.pack(pady=(30,10))
Total_input.config(font=('verdana',20))
Total_input.grid(row=5,column=1,padx=30,pady=25)



def generate_payslip():
    # label_fun = Label(root,text=(Name_input.get(),basic_salary_input.get()))
    # label_fun.pack()
    # Name_input.config(font=('verdana',18))
    textarea.delete(1.0,END)
    # textarea.insert(END,' \tNumber of Items\t  \n')
    textarea.insert(END,f'\n\n   Name :             \t\t{Name_input.get()}\t')
    textarea.insert(END,f'\n\n   Balance Leave :    \t\t{Balance_Leave_input.get()}\t')
    textarea.insert(END,f'\n\n   Allowance :        \t\t{Allowance_input.get()}\t')
    textarea.insert(END,f'\n\n   Total Leave :      \t\t{Total_Leave_input.get()}\t ')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\n     Balance Leave :    \t\t{Balance_Leave_input.get()}\t')
    textarea.insert(END, f"\n================================")

def reset():
    textarea.delete(1.0,END)
    Name_input.set(0)
    Balance_Leave_input.set(0)
    Allowance_input.set(0)
    Total_Leave_input.set(0)
    Balance_Leave_input.set(0)

def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

F2 =Frame(root,bg='#2D9290',bd=15,relief=RIDGE)
F2.place(x=5, y=740,width=900,height=100)

Button_payslip = Button(F2,text='Generate Payslip', bg='white',fg='black' ,width=15,height=1,command=generate_payslip)
# Button_payslip.pack(pady=(5,5))
Button_payslip.config(font=('Helvetica',20,'bold'))
Button_payslip.grid(row=0,column=0,padx=5,pady=5)

Button_reset = Button(F2, text='Reset', font=('Helvetica',20,'bold'), bg='white',fg='black',width=15,height=1,command=reset)
Button_reset.grid(row=0,column=1,padx=5,pady=5)

Button_exit = Button(F2, text='Exit', font=('Helvetica',20,'bold'), bg='white',fg='black',width=15,height=1,command=exit)
Button_exit.grid(row=0,column=2,padx=5,pady=5)


F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=905,y=90,width=500,height=650)
payslip_title=Label(F3,text='Pay Slip',font=('Helvetica',20,'bold'),bd=7,relief=GROOVE).pack(fill=X)
# scrol_y=Scrollbar(F2,orient=VERTICAL)
# scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F3,font='arial 15')
textarea.pack(fill=BOTH)
# scrol_y.config(command=textarea.yview)

F4 = Frame(root,relief=GROOVE,bd=10,bg='#2D9290')
F4.place(x=905,y=740,width=500,height=100)

Button_print = Button(F4, text='Print', font=('Helvetica',20,'bold'), bg='white',fg='black',width=15,height=1,command=print)
Button_print.grid(padx=5,pady=5)







root.mainloop()