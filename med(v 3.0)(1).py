#Program for managing stock in medical store

import tkinter
import os, time

import MySQLdb
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import MySQLdb

mydb=MySQLdb.connect(host="localhost",\
user="root",\
passwd="sarthakjain")
c=mydb.cursor()


c=mydb.cursor()

try:
    c.execute("create database temps")
except:
    pass
c.execute("use temps")
try:
    c.execute("create table item(Batchno integer primary key, name varchar(25), No_of_items integer(10),Expiry date)")
    mydb.commit()
except:
    pass

try:
    c.execute("create table passwd(user varchar(20) primary key, passwd varchar(20))")
    mydb.commit()
except:
    c.execute("use temps")

try:
    sql="insert into passwd values (%s,%s)"
    c.execute(sql,("Admin","Admin"))
    mydb.commit()
except:
    pass

c.execute("use temps")

root = Tk()

root.title("Medical store Management System")
root.state("zoomed")
root.geometry("1920x1080")
root.iconbitmap(r'Icon.ico')

state1='disabled'
state2='disabled'
state3='disabled'
num=0


#############################################################Delete#########################################################


def delete(): 
    
    global en1, lb1, SubmitBtn,lb,num

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass

    lb = Label(displayFrame,text='Delete Medicine',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.37,rely=0)
        
    lb1 = Label(displayFrame,text="Batch : ",font=("arial",12,'bold'), bg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    en1 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(displayFrame,text="SUBMIT", font=("arial",12,'bold'),bg='white',command=deleteMedicine)
    SubmitBtn.place(relx=0.6,rely=0.75, relwidth=0.18,relheight=0.08)

    num=2

def deleteMedicine():
    
    batch = en1.get()
    
    sql_Delete_query = """Delete from item where batchno= %s"""
    
    if batch=='':
        messagebox.showinfo("","Please enter Batch no")

    else:
        try:
            c.execute(sql_Delete_query, (batch,))
            mydb.commit()
            messagebox.showinfo("Success","Medicine Deleted Successfully") 
        except:
            messagebox.showinfo("Check Credentials","Please check Batch no")
    

    en1.delete(0, END)

    
##########################################################Menu#############################################################


def Menu():

    global state1,state2,btn1,btn2,btn3,btn4,btn5,btn6,photoimage1, photoimage2, photoimage3, photoimage4, photoimage5, photoimage6
    
    photo1 = PhotoImage(file =r"icons\add.png")
    photoimage1 = photo1.subsample(3, 3)
    btn1 = Button(moduleFrame,text="Add New Medicine",font=("arial",12,'bold'),image=photoimage1,compound = LEFT, command=addMedicine, state=state1)
    btn1.place(relx=0,rely=0.17, relwidth=1,relheight=0.12)
    
    photo2 = PhotoImage(file =r"icons\delete.png")
    photoimage2 = photo2.subsample(3,3)
    btn2 = Button(moduleFrame,text="Delete Medicine",font=("arial",12,'bold'),image=photoimage2, compound= LEFT, command=delete,state=state1)
    btn2.place(relx=0,rely=0.31, relwidth=1,relheight=0.12)
    
    photo3 = PhotoImage(file =r"icons\view.png")
    photoimage3 = photo3.subsample(3,3)
    btn3 = Button(moduleFrame,text="View Medicines List",font=("arial",12,'bold'),image=photoimage3, compound= LEFT, command=View,state=state2)
    btn3.place(relx=0, rely=0.44, relwidth=1,relheight=0.12)
    
    photo4 = PhotoImage(file =r"icons\search.png")
    photoimage4 = photo4.subsample(3,3)
    btn4 = Button(moduleFrame,text="Search Medicine",font=("arial",12,'bold'),image=photoimage4, compound= LEFT, command=searchMedicine,state=state2)
    btn4.place(relx=0,rely=0.58, relwidth=1,relheight=0.12)
    
    photo5 = PhotoImage(file =r"icons\modify.png")
    photoimage5 = photo5.subsample(3,3)
    btn5 = Button(moduleFrame,text="Modify",font=("arial",12,'bold'),image=photoimage5, compound = LEFT, command = ModifyMedicine,state=state1)
    btn5.place(relx=0,rely=0.72, relwidth=1,relheight=0.12)
    
    photo6 = PhotoImage(file =r"icons\exit.png")
    photoimage6 = photo6.subsample(3,3)
    btn6 = Button(moduleFrame, text="Exit",font=("arial",12,'bold'), image=photoimage6, compound = LEFT, command=Exit,state=state1)
    btn6.place(relx=0,rely=0.86, relwidth=1,relheight=0.12)

    logoutBtn=Button(headingFrame, text="LOGOUT", font=('arial',10,'bold'), command=logout, state=state3)
    logoutBtn.place(relx=0.87, rely=0.7, relwidth=0.1)


#######################################################View##############################################################


def View():
    global scroll_y, medicine_table,num,headingLabel

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass
        
    
    scroll_y=Scrollbar(displayFrame,orient=VERTICAL)
    medicine_table=ttk.Treeview(displayFrame,columns=("batchno","name","No_of_items","expiry"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=medicine_table.yview)
    medicine_table.heading("batchno",text="Batch no")
    medicine_table.heading("name",text="Name")
    medicine_table.heading("No_of_items",text="No of items")
    medicine_table.heading("expiry",text="Expiry")
    medicine_table["show"]="headings"
    medicine_table.column("batchno",width=50)
    medicine_table.column("name",width=50)
    medicine_table.column("No_of_items",width=50)
    medicine_table.column("expiry",width=50)
    medicine_table.pack(fill=BOTH,expand=1)

    num=8

    sqlite_select_query = """SELECT * from item"""
    try:
        c.execute(sqlite_select_query)
        mydb.commit()
        rows=c.fetchall()
        for row in rows:
            medicine_table.insert('',END,values=row)
    except:
        messagebox.showinfo("Error","Can't fetch data from database")



####################################################Search################################################################


def searchMedicine(): 
    
    global en1,SearchBtn,lb1, headingLabel,num

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass
        
    headingLabel = Label(displayFrame, text="Search Medicine",font=("Times New Roman",26,'bold'), bg='white')
    headingLabel.place(relx=0.35,rely=0.05)   
        
    lb1 = Label(displayFrame,text="Enter Name : ",font=("arial",12,'bold'), bg='white')
    lb1.place(relx=0.05,rely=0.4)
        
    en1 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    #Submit Button
    SearchBtn = Button(displayFrame,text="Search",font=('arial',12,'bold'),bg='white',command=search)
    SearchBtn.place(relx=0.66,rely=0.55, relwidth=0.18,relheight=0.08)

    

    num=6


def search():
    
    global SearchBtn,labelFrame,lb1,en1,scroll_y, books_table,num
    
    Name_ = en1.get()

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass
    
   
    
    scroll_y=Scrollbar(displayFrame,orient=VERTICAL)
    medicine_table=ttk.Treeview(displayFrame,columns=("batchno","name","No_of_items","expiry"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=medicine_table.yview)
    medicine_table.heading("batchno",text="Batch no")
    medicine_table.heading("name",text="Name")
    medicine_table.heading("No_of_items",text="No of Items")
    medicine_table.heading("expiry",text="Expiry")
    medicine_table["show"]="headings"
    medicine_table.column("batchno",width=50)
    medicine_table.column("name",width=50)
    medicine_table.column("No_of_items",width=50)
    medicine_table.column("expiry",width=50)
    medicine_table.pack(fill=BOTH,expand=1)

    num=7

    sqlite_select_query = """SELECT * from item WHERE name = %s"""
    
    #for row in records:
    #    if row[0]=="Admin":

    try:
        c.execute(sqlite_select_query,(Name_))
        mydb.commit()
        rows = c.fetchall()
        for row in rows:
            medicine_table.insert('',END,values=row)
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

        
    
###################################################Modify####################################################################    



def ModifyMedicine(): 
    
    global en1,en2,en3,issueBtn,lb1,lb2,lb3,en1,en2,en3,lb,num

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass
   
    lb = Label(displayFrame,text="Modify Medicine", font=('Times New Roman',26,'bold'), bg='white')
    lb.place(relx=0.27,rely=0)
    
    lb1 = Label(displayFrame,text="Batch no : ",font=('arial', 12,'bold'), bg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Entry(displayFrame,font=('arial', 12,'bold'),bg='#FFDFA4')
    en1.place(relx=0.4,rely=0.2, relwidth=0.55)
    
    lb2 = Label(displayFrame,text="Enter no of items to add/remove : ",font=('arial', 12,'bold'),bg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    en2 = Entry(displayFrame,font=('arial', 12,'bold'),bg='#FFDFA4')
    en2.place(relx=0.5,rely=0.4, relwidth=0.45)

    rem_Btn = Button(displayFrame,text="Remove",bg='white',font=("arial",12,'bold'), command=remove_)
    rem_Btn.place(relx=0.7,rely=0.75, relwidth=0.18,relheight=0.08)

    add_Btn = Button(displayFrame,text="Add",bg='white',font=("arial",12,'bold'), command=append_)
    add_Btn.place(relx=0.1,rely=0.75, relwidth=0.18,relheight=0.08)

    num=3

def append_():
    batch = en1.get()
    number = en2.get()

    sqlite_select_query = """SELECT No_of_items from item WHERE Batchno = %s"""
    c.execute(sqlite_select_query,(batch,))
    records = c.fetchall()

    sql = "UPDATE item SET No_of_items = %s WHERE batchno = %s"
    val = (int(records[0][0])+int(number),batch)

    if not records:
        messagebox.showinfo("Error 404","Item not found")
        return

    if batch=='':
        messagebox.showinfo("","Please enter Batch no")

    else:
        try:
            c.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success","Medicine Added Successfully") 
        except:
            messagebox.showinfo("Check Credentials","Please check batch number")
    

    en1.delete(0, END)

    
    
def remove_():
    batch = en1.get()
    number = en2.get()

    sqlite_select_query = """SELECT No_of_items from item WHERE Batchno = %s"""
    c.execute(sqlite_select_query,(batch,))
    records = c.fetchall()

    print(records)

    if not records:
        messagebox.showinfo("Error 404","Item not found")
        return
    
    if (int(records[0][0])-int(number)) <0:
        messagebox.showinfo("Out of Stock","Specified no of items not availaible")
        return
    
    val = (int(records[0][0])-int(number),batch)
    sql = "UPDATE item SET No_of_items = %s WHERE batchno = %s"

    if batch=='':
        messagebox.showinfo("","Please enter Batch no")

    else:
        try:
            c.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success","Medicine Removed Successfully") 
        except:
            messagebox.showinfo("Check Credentials","Please check batch number")
    

    en1.delete(0, END)
    


#########################################################Exit####################################################################


    
def Exit():
    messagebox.showinfo("Exit","Thank you for using our software :)")
    root.destroy()    


###########################################################Add###########################################################


def addMedicine(): 
    
    global en1,en2,en3,en4,lb1,lb2,lb3,lb4,SubmitBtn,lb,num

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass

    lb=Label(displayFrame,text='Add Medicine',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)


    lb1 = Label(displayFrame,text="Batch no : ",font=("arial",12,'bold'),bg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)
        

    lb2 = Label(displayFrame,text="Name : ",font=("arial",12,'bold'),bg='white')
    lb2.place(relx=0.09,rely=0.35)
        
    en2 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)

        
    lb3 = Label(displayFrame,text="No of items :",font=("arial",12,'bold'),bg='white')
    lb3.place(relx=0.05,rely=0.5)
        
    en3 = Entry(displayFrame, font=("arial",12,'bold'), bg='#FFDFA4')
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
        

    lb4 = Label(displayFrame,text="Expiry in(yy/mm/dd) : ",font=("arial",12,'bold'),bg='white')
    lb4.place(relx=0.05,rely=0.65)
        
    en4 = Entry(displayFrame,font=("arial",12,'bold'), bg='#FFDFA4')
    en4.place(relx=0.3,rely=0.65, relwidth=0.62)
        
    #Submit Button
    SubmitBtn = Button(displayFrame,text="SUBMIT",font=("arial",12,'bold'),bg='white',command=_add_)
    SubmitBtn.place(relx=0.65,rely=0.8, relwidth=0.18,relheight=0.08)

    num=1

def _add_():

    global en1,en2,en3,en4
    
    batch = en1.get()
    
    name = en2.get()
    
    No_of_items = en3.get()
    
    expiry = en4.get()
    
    sql="insert into item values (%s,%s,%s,%s)"
    

    try:
        if (type(int(batch)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Batch no should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Batch no should be an integer")
        return
        
    if batch=="" or name=="" or No_of_items=="" or expiry=="":
        messagebox.showinfo("Error", "Please fill all the details")

    else:
        try:
            c.execute(sql,(batch,name,No_of_items,expiry))
            mydb.commit()
            messagebox.showinfo("Sucess","Medicine added")
        
        except:
            messagebox.showinfo("Error","Can't add data into Database")
    
    
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)

def gettingLoginDetails():

    global role,state1,state2,btn1,btn2,btn3,btn4,btn5,btn6,state3


    name = ent2.get()
    password = ent3.get()
    role=ent4.get()
    
    if role=='Admin':
        sqlite_select_query = """SELECT * from passwd"""
        c.execute(sqlite_select_query)
        records = c.fetchall()
        
        
        try:
            Username_=False
            Password_=False
            
            for row in records:
                if row[0]==name:
                    Username_=True
            for row in records:
                if row[1]==password:
                    Password_=True

            
            if(Username_ and Password_):
                messagebox.showinfo("SUCCESS","You have successfully logged in")
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
                btn4.destroy()
                btn5.destroy()
                btn6.destroy()
                
                state1='normal'
                state2='normal'
                state3='normal'
                Menu()
                
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")
            
    else:
        sqlite_select_query = """SELECT * from passwd"""
        c.execute(sqlite_select_query)
        records = c.fetchall()

        
        try:
            Username_=False
            Password_=False
            
            for row in records:
                if row[0]==name:
                    Username_=True
            for row in records:
                if row[1]==password:
                    Password_=True

            
            if(Username_ and Password_):
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
                btn4.destroy()
                btn5.destroy()
                btn6.destroy()
                
                state2='normal'
                state3='normal'
                Menu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")
        


def gettingDetails():
    
    name = ent2.get()
    password = ent3.get()
    role=ent4.get()
    
    if role=="Admin":
        
    
        sql="insert into passwd values (%s,%s)"
        try:
            c.execute(sql,(name,password))
            mydb.commit()
            messagebox.showinfo("Success", "Successfully registered")
        except:
            messagebox.showinfo("Error inserting","Cannot add data to Database")

    else:

        
        sql="insert into passwd values (%s,%s)"
        try:
            c.execute(sql,(name,password))
            mydb.commit()
            messagebox.showinfo("Success", "Successfully registered")
        except:
            messagebox.showinfo("Error inserting","Cannot add data to Database")

        
    #ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)


###############################################################Logout####################################################



def logout():
    global num,state1,state2,state3

    
    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        rem_Btn.destroy()
        add_Btn.destroy()

    elif num==5:
        en1.destroy()
        en2.destroy()
        ReturnBtn.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()

    elif num==6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        medicine_table.destroy()

    else:
        pass



    state1="disabled"
    state2="disabled"
    state3="disabled"
    Menu()
    messagebox.showinfo("Logged out", "You have Successfully logged out")
    

###################################### Frames ############################################################################
       
headingFrame = Frame(root,bd=20, relief=RIDGE)
headingFrame.place(relx=0,rely=0,relwidth=1,relheight=0.2)

heading=Label(headingFrame,font=('Times New ROman', 40, 'bold'), text="Medical Store Management System")
heading.place(relx=0, rely=0.2)

moduleFrame = Frame(root,bd=20, relief=RIDGE)
moduleFrame.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)

headingLabel = Label(moduleFrame, text="MENU",font=("Times New Roman",26,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.15)

dFrame= Frame(root,bd=20, relief=RIDGE)
dFrame.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)

displayFrame=Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.2,rely=0.05, relwidth=0.6, relheight=0.9)

########################################### Interface for login and registration ############################################

#Name
lb2=Label(headingFrame,text='Name:',font=('arial', 12,'bold'))
lb2.place(relx=0.63, rely=0.25)

ent2=Entry(headingFrame, font=('arial', 12,'bold'))
ent2.place(relx=0.7, rely=0.25, relwidth=0.15)

#Password
lb3=Label(headingFrame,text='Password:',font=('arial', 12,'bold'))
lb3.place(relx=0.63, rely=0.48)

ent3=Entry(headingFrame, font=('arial', 12,'bold'),show="\u2022")
ent3.place(relx=0.7, rely=0.48, relwidth=0.15)

#Role Combobox
lb4=Label(headingFrame,text='Role:',font=('arial', 12,'bold'))
lb4.place(relx=0.63, rely=0.73)

ent4=ttk.Combobox(headingFrame, font=('arial', 12, 'bold'), state='readonly', width=23)
ent4['value']=('','Admin', 'User')
ent4.current(0)
ent4.place(relx=0.7,rely=0.73,relwidth=0.15)

loginBtn = Button(headingFrame,text="LOGIN", font=("arial",10,'bold'),command=gettingLoginDetails)
loginBtn.place(relx=0.87,rely=0.4, relwidth=0.1)

regBtn=Button(headingFrame,text="REGISTER", font=("arial",10,'bold'),command=gettingDetails)
regBtn.place(relx=0.87,rely=0.1, relwidth=0.1)



Menu()
root.mainloop()
