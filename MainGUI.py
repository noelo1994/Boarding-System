from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import webbrowser


root = Tk()
root.title("On/Off boarding system")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#005ff9")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
HOUSE_NUM = StringVar()
POSTCODE = StringVar()
SALARY = StringVar()
TAX_CODE = StringVar()
NATIONAL_INSURANCE = StringVar()
STILL_EMPLOYED = StringVar()
SEARCH = StringVar()


# ========================================METHODS==========================================

def database():
    global conn, cursor
    conn = sqlite3.connect("onoffbdatabase.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
        " username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `employee` (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT"
        ", last_name, house_num TEXT, postcode TEXT, salary TEXT, tax_code TEXT, national_insurance TEXT,"
        " still_employed TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def exit():#function to exit program
    result = tkMessageBox.askquestion('On/Off Boarding System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def showLoginForm():#finction to set properties of the window
    global loginform
    loginform = Toplevel()#brins window to front
    loginform.title("On/Offboarding Database Login")#set title of window
    width = 600
    height = 500#set dimentions
    screen_width = root.winfo_screenwidth()#saving the width of the screen
    screen_height = root.winfo_screenheight()#save width of the screen
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)#stop window from being resieable
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginForm()

def loginForm():##function to se properties of the content on the window
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)#call frame widget to work with sizing and scaling
    TopLoginForm.pack(side=TOP, pady=20)#organising wigets before placing them in parent
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)#label for the title of the window
    lbl_text.pack(fill=X)#scale it to the width of screen
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)

    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=login)
    btn_login.focus()
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', login)



def home():
    global home
    home = Tk()
    home.title("On/Off Boarding System/Home")
    width = 1024
    height = 720
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    home.resizable(0, 0)
    Title = Frame(home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="On/Off Boarding System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Account", menu=filemenu)#first drop down
    menubar.add_cascade(label="Database", menu=filemenu2)#second drop down
    menubar.add_cascade(label="Policies", menu=filemenu3)#third drop down
    menubar.add_cascade(label="Document Manager", menu=filemenu4)  # fourth drop down


    filemenu.add_command(label="Logout", command=logout)  #first drop down option
    filemenu.add_command(label='Change Password')#first drop down option
    filemenu.add_command(label="Exit", command=exit)#first drop down option

    filemenu2.add_command(label="Add new", command=showAddNew)#second drop down option
    filemenu2.add_command(label="View", command=ShowView)#second drop down option

    filemenu3.add_command(label="View", command = showpolicies)#third drop down option

    filemenu4.add_command(label="Show Documents", command = showdocuments)#fourth drop down option


    home.config(menu=menubar)
    home.config(bg="#005ff9")

    lbl_messageofday=Label(text="Message of the day: MONDAYS ARE GOOD", font=('arial',25))
    lbl_messageofday.pack()



def showdocuments():
    global viewdocuments
    viewdocuments = Toplevel()
    viewdocuments.title("Select a Document")
    width = 300
    height = 300
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewdocuments.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewdocuments.resizable(0, 0)
    viewdocumentsform()

def viewdocumentsform():
    frame = Frame(viewdocuments)
    listbox = Listbox(frame)
    listbox.insert(1,"New Starter Form")
    listbox.insert(2, "Welcome Email")
    listbox.insert(3, "Fire Training")


    def opendoc():
        selection = listbox.curselection()
        for i in selection:
           docselection = listbox.get(i)

        if docselection == 'New Starter Form':
            webbrowser.open_new(r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\New Starter Form.odt")
        if docselection == 'Welcome Email':
            webbrowser.open_new(
                r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\Welcome Email.docx")
        if docselection == 'Fire Training':
            webbrowser.open_new(
                r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\UFIX Fire Training.doc")



    btn = Button(frame,text='Open', command=opendoc)
    btn.pack(padx=5,side=RIGHT)
    listbox.pack(side=LEFT)
    frame.pack(padx=3,pady=30)
    viewdocuments.mainloop()






def showpolicies():
    global viewpolicies
    viewpolicies = Toplevel()
    viewpolicies.title("Select a policy to view")
    width = 300
    height = 300
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewpolicies.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewpolicies.resizable(0, 0)
    viewpoliciesform()

def viewpoliciesform():
    frame = Frame(viewpolicies)
    listbox = Listbox(frame)
    listbox.insert(1,"Data Protection act")
    listbox.insert(2, "Comuter misuse act")
    listbox.insert(3, "Fire Training")


    def opendoc():
        selection = listbox.curselection()
        for i in selection:
           polselection = listbox.get(i)

        if polselection == 'New Starter Form':
            webbrowser.open_new(r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\New Starter Form.odt")
        if polselection == 'Welcome Email':
            webbrowser.open_new(
                r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\Welcome Email.docx")
        if polselection == 'Fire Training':
            webbrowser.open_new(
                r"C:\Users\Noel\Google Drive\Uni\Year 2 v2\Professional Practice\Onboarding\UFIX Fire Training.doc")



    btn = Button(frame,text='Open', command=opendoc)
    btn.pack(padx=5,side=RIGHT)
    listbox.pack(side=LEFT)
    frame.pack(padx=3,pady=30)
    viewdocuments.mainloop()



def showAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("On/Off Boarding System/Add new")
    width = 600
    height = 550
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addNewForm()

def addNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Employee", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=2)
    lbl_firstname = Label(MidAddNew, text="First Name:", font=('arial', 15), bd=10)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(MidAddNew, text="Last Name:", font=('arial', 15), bd=10)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_housenum = Label(MidAddNew, text="House Number/Name:", font=('arial', 15), bd=10)
    lbl_housenum.grid(row=2, sticky=W)
    lbl_postcode = Label(MidAddNew, text="Postcode:", font=('arial', 15), bd=10)
    lbl_postcode.grid(row=3, sticky=W)
    lbl_salary = Label(MidAddNew, text="Salary:", font=('arial', 15), bd=10)
    lbl_salary.grid(row=4, sticky=W)
    lbl_taxcode = Label(MidAddNew, text="Tax Code:", font=('arial', 15), bd=10)
    lbl_taxcode.grid(row=5, sticky=W)
    lbl_nationalinsuance = Label(MidAddNew, text="National Insurance:", font=('arial', 15), bd=10)
    lbl_nationalinsuance.grid(row=6, sticky=W)
    lbl_stillemployed = Label(MidAddNew, text="Still Employed:", font=('arial', 15), bd=10)
    lbl_stillemployed.grid(row=7, sticky=W)

    firstname = Entry(MidAddNew, textvariable=FIRST_NAME, font=('arial', 15), width=15)
    firstname.grid(row=0, column=1)
    lastname = Entry(MidAddNew, textvariable=LAST_NAME, font=('arial', 15), width=15)
    lastname.grid(row=1, column=1)
    housenum = Entry(MidAddNew, textvariable=HOUSE_NUM, font=('arial', 15), width=15)
    housenum.grid(row=2, column=1)
    postcode = Entry(MidAddNew, textvariable=POSTCODE, font=('arial', 15), width=15)
    postcode.grid(row=3, column=1)
    salary = Entry(MidAddNew, textvariable=SALARY, font=('arial', 15), width=15)
    salary.grid(row=4, column=1)
    taxcode = Entry(MidAddNew, textvariable=TAX_CODE, font=('arial', 15), width=15)
    taxcode.grid(row=5, column=1)
    nationalinsuance = Entry(MidAddNew, textvariable=NATIONAL_INSURANCE, font=('arial', 15), width=15)
    nationalinsuance.grid(row=6, column=1)
    stillemployed = Entry(MidAddNew, textvariable=STILL_EMPLOYED, font=('arial', 15), width=15)
    stillemployed.grid(row=7, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=addNew)
    btn_add.grid(row=8, columnspan=2, pady=20)

def addNew():
    database()
    cursor.execute("INSERT INTO `employee` (first_name, last_name, house_num,"
                   " postcode, salary,tax_code, national_insurance, still_employed)"
                   " VALUES( ?, ?, ?, ?, ?, ?, ?, ?)",
                   (str(FIRST_NAME.get()),
                    str(LAST_NAME.get()),
                    str(HOUSE_NUM.get()),
                    str(POSTCODE.get()),
                    int(SALARY.get()),
                    str(TAX_CODE.get()),
                    str(NATIONAL_INSURANCE.get()),
                    str(STILL_EMPLOYED.get())))
    conn.commit()
    FIRST_NAME.set("")
    LAST_NAME.set("")
    HOUSE_NUM.set("")
    POSTCODE.set("")
    SALARY.set("")
    TAX_CODE.set("")
    NATIONAL_INSURANCE.set("")
    STILL_EMPLOYED.set("")
    cursor.close()
    conn.close()

def viewForm():
    global tree
    topViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    topViewForm.pack(side=TOP, fill=X)
    leftViewForm = Frame(viewform, width=600)
    leftViewForm.pack(side=LEFT, fill=Y)
    midViewForm = Frame(viewform, width=600)
    midViewForm.pack(side=RIGHT)

    lbl_text = Label(topViewForm, text="View Employees", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(leftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(leftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(leftViewForm, text="Search", command=search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(leftViewForm, text="Reset", command=reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(leftViewForm, text="Delete", command=delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(midViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(midViewForm, orient=VERTICAL)
    tree = ttk.Treeview(midViewForm, columns=("EmployeeID", "First Name", "Last Name", "House Num/Name", "Postcode",
                                              "Salary", "Tax Code", "National Insurance", "Still Employed"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('EmployeeID', text="EmployeeID", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('House Num/Name', text="House Num/Name", anchor=W)
    tree.heading('Postcode', text="Postcode", anchor=W)
    tree.heading('Salary', text="Salary", anchor=W)
    tree.heading('Tax Code', text="Tax Code", anchor=W)
    tree.heading('National Insurance', text="National Insurance", anchor=W)
    tree.heading('Still Employed', text="Still Employed", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    tree.column('#8', stretch=NO, minwidth=0, width=120)
    tree.column('#9', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayData()


def displayData():
    database()
    cursor.execute("SELECT * FROM `employee`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()

def search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute("SELECT * FROM `employee` WHERE `first_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()



def reset():
    tree.delete(*tree.get_children())
    displayData()
    SEARCH.set("")


def delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('On/Off Boarding System', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            database()
            cursor.execute("DELETE FROM `employee` WHERE `employee_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("On/Off Boarding System/View Employee")
    width = 600
    height = 400
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    viewForm()

def logout():
    result = tkMessageBox.askquestion('On/Off Boarding System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        home.destroy()

def login(event=None):
    global admin_id
    database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            showHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()

def showHome():
    root.withdraw()
    home()
    loginform.destroy()


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=showLoginForm)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="On/Off Boarding System", font=('arial', 45))
lbl_display.pack()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
