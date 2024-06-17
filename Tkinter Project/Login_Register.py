#imports
from tkinter import *
import os

#Main screen
master = Tk()
master.title('Movie Ticketing System')
master.iconbitmap('movies.ico')
master.geometry("200x200")
master.resizable(0,0)

#Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg='red', text="All fields required!!!")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg='red', text= 'Account already exists')
            return
        else:
            new_file=open(name,"w")
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg='green', text='Account created successfully.')
def register():
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif


    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()


    #Register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen.iconbitmap('movies.ico')


    #Labels
    Label(register_screen, text='Please enter your details below to register as an admin:', font=('Calibri', 16)).grid(row=0, sticky=N, pady=10)
    Name=Label(register_screen, text='Name', font=('Calibri', 12)).grid(row=1, sticky=W)
    Age=Label(register_screen, text='Age', font=('Calibri', 12)).grid(row=2, sticky=W)
    Gender=Label(register_screen, text='Gender', font=('Calibri', 12)).grid(row=3, sticky=W)
    Password=Label(register_screen, text='Password', font=('Calibri', 12)).grid(row=4, sticky=W)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password, show="*").grid(row=4,column=0)

    #Buttons
    Button(register_screen, text='Register', font=('Calibri',12), command=finish_reg,bg="black",fg='white').grid(row=5, sticky=N, pady=10,ipadx=20,padx=20)


def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data=file.read()
            file_data=file_data.split('\n')
            password = file_data[3]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                os.system('Ticket_Management_System.py')
                return
            else:
                login_notif.config(fg='red', text='Password incorrect !!!')
                return
    login_notif.config(fg='red', text="No account found !!!")
def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.iconbitmap('movies.ico')

    #Labels
    Label(login_screen, text='Login to your account:', font=('Calibri',16)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text='Username', font=('Calibri',12)).grid(row=1,sticky=W)
    Label(login_screen, text='Password', font=('Calibri',12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4, sticky=N)


    #Entries
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1, padx=5)

    #Button
    Button(login_screen, text='Login' , command=login_session, width=15, font=('Calibri',12),bg="black",fg='white').grid(row=3,sticky=W,pady=5,padx=5)

#Labels
Label(master, text='Welcome to BIG Movies!!!', font=('Forte', 12)).grid(row=0, sticky=N, pady=10)




#Buttons
Button1=Button(master, text='Register Screen', font=('Calibri',12) ,width=20, command=register,bg="black",fg='white').grid(row=3, sticky=N, pady=10)
Button2=Button(master, text='Login Screen', font=('Calibri',12) ,width=20, command=login,bg="black",fg='white').grid(row=4, sticky=N, pady=10)



master.mainloop()

