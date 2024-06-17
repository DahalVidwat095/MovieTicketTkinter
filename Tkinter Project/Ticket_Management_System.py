#import python libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#Function to create and call database
def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT, EMAIL TEXT, MOVIES TEXT)")


def show_database_result(first_name, last_name):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM REGISTRATION WHERE FNAME = ? and LNAME = ?", (first_name, last_name))
    check = cursor.fetchall()
    if check:
        return "Pass"
    else:
        return "Fail"

def show_database_result1(gender, address):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM REGISTRATION WHERE GENDER = ? and ADDRESS = ?", (gender, address))
    check = cursor.fetchall()
    if check:
        return "Pass"
    else:
        return "Fail"

def show_database_result2(phone, email):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM REGISTRATION WHERE CONTACT = ? and EMAIL = ?", (phone, email))
    check = cursor.fetchall()
    if check:
        return "Pass"
    else:
        return "Fail"


#defining function for creating GUI Layout
def DisplayForm():
    #creating main window
    display_screen = Tk()
    #determining geometry of main window
    display_screen.geometry("1200x420")
    display_screen.resizable(0,0)
    #setting title for main window
    display_screen.title("Big Movies")
    #setting icon for main window
    display_screen.iconbitmap('movies.ico')
    global tree
    global SEARCH
    global fname,lname,gender,address,contact,email,movies
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    email = StringVar()
    movies = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopFrame = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopFrame.pack(side=TOP, fill=X)
    #first left frame for registration form
    L1frame = Frame(display_screen, width="350",bg="gray")
    L1frame.pack(side=LEFT, fill=Y)
    #second left frame for various buttons
    L2frame = Frame(display_screen, width=500,bg="gray")
    L2frame.pack(side=LEFT, fill=Y)
    #right frame for displaying  records of database
    Rframe = Frame(display_screen, width=600)
    Rframe.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopFrame, text="Movie Ticket Management System", font=('Forte', 18), width=700,bg="black",fg='white')
    lbl_text.pack(fill=X)
    #creating registration form in the first left frame
    Label(L1frame, text="First Name  ", font=("Arial", 12),bg="gray",fg="white").pack(side=TOP)
    Entry(L1frame,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(L1frame, text="Last Name ", font=("Arial", 12),bg="gray",fg="white").pack(side=TOP)
    Entry(L1frame, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(L1frame, text="Gender ", font=("Arial", 12),bg="gray",fg="white").pack(side=TOP)
    gender.set("Select Gender")
    content={'Male','Female','Other'}
    OptionMenu(L1frame,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(L1frame, text="Address ", font=("Arial", 12),bg="gray",fg="white").pack(side=TOP)
    Entry(L1frame, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(L1frame, text="Phone", font=("Arial", 12),bg="gray",fg="white").pack(side=TOP)
    Entry(L1frame, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(L1frame, text="Email", font=("Arial", 12), bg="gray", fg="white").pack(side=TOP)
    Entry(L1frame, font=("Arial", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(L1frame, text="Movies ", font=("Arial", 12), bg="gray", fg="white").pack(side=TOP)
    movies.set("Select Movies")
    content1 = {'Men in Black', 'Endgame', 'Godfather', 'Dark Knight'}
    OptionMenu(L1frame, movies, *content1).pack(side=TOP, padx=10, fill=X)
    Button(L1frame,text="Register",font=("Calibri", 18, "bold"),command=register,bg="black",fg="white").pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(L2frame, text="Enter Seat no. to search", font=('Calibri', 18),bg='black',fg='white')
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(L2frame, textvariable=SEARCH, font=('verdana', 15), width=8)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(L2frame, text="Search", command=SearchRecord,bg="black",fg='white')
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(L2frame, text="Show All", command=DisplayData,bg="black",fg='white')
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(L2frame, text="Clear all", command=Reset,bg="black",fg='white')
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(L2frame, text="Delete", command=Delete,bg="black",fg='white')
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_update = Button(L2frame, text="Update", command=Update,bg="black",fg='white')
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar( Rframe, orient=HORIZONTAL)
    scrollbary = Scrollbar( Rframe, orient=VERTICAL)
    tree = ttk.Treeview( Rframe,columns=("A","B","C","D","E","F","G","H"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('A', text="Seat Number", anchor=W)
    tree.heading('B', text="First Name", anchor=W)
    tree.heading('C', text="Last Name", anchor=W)
    tree.heading('D', text="Gender", anchor=W)
    tree.heading('E', text="Address", anchor=W)
    tree.heading('F', text="Phone", anchor=W)
    tree.heading('G', text="Email", anchor=W)
    tree.heading('H', text="Movie", anchor=W)

    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)


    tree.pack()
    DisplayData()
#function to update data into database
def Update():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    email1=email.get()
    movie1=movies.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1==''or email1==''or movie1=='':
        tkMessageBox.showinfo("Warning","Double click the data you want to update!!!")
    else:
        #getting selected data
        current_item = tree.focus()
        contents = (tree.item(current_item))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=?,EMAIL=?,MOVIES=? WHERE RID = ?',(fname1,lname1,gender1,address1,contact1,email1,movie1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully!!!")
        #clear all data from form
        Reset()
        #refreshed table data is shown
        DisplayData()
        conn.close()

def register():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    email1=email.get()
    movie1=movies.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1==''or email1==''or movie1=='':
        tkMessageBox.showinfo("Warning","Fill the required empty entries!!!")
    else:
        #execute query
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT,EMAIL,MOVIES) \
              VALUES (?,?,?,?,?,?,?)',(fname1,lname1,gender1,address1,contact1,email1,movie1));
        conn.commit()
        tkMessageBox.showinfo("Message","Your ticket is confirmed!!!")
        #clear data
        Reset()
        #refresh table data
        DisplayData()
        conn.close()
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
    email.set("")
    movies.set("")
def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            current_Item = tree.focus()
            contents = (tree.item(current_Item))
            selecteditem = contents['values']
            tree.delete(current_Item)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE RID LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    #getting focused item from treeview
    current_item = tree.focus()
    contents = (tree.item(current_item))
    selecteditem = contents['values']
    #set values in the fields all done 
    # all done
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])
    email.set(selecteditem[6])
    movies.set(selecteditem[7])

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()

