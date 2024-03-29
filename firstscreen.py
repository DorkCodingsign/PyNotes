
from tkinter import *
import os
 

 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="Red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()
 
 

 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login",bg="red").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,bg="red", command = login_verify).pack()
 

def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 

 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()


def login_sucess():
    session()
def session():
    notesscreen=Toplevel(main_screen)
    notesscreen.title("Welcome To Notes")
    notesscreen.geometry("400x400")
    Label(notesscreen,text="Welcome to Dash Board").pack()
    Button(notesscreen,text="Create Notes",command=createnotes).pack()
    Button(notesscreen,text="View Notes",command=view).pack()
    Button(notesscreen,text="Delete Ntes",command=delete).pack()
def delete():
    notesscreen4=Toplevel(main_screen)
    notesscreen4.title("Info")
    notesscreen4.geometry("250x250")
    allfiles=os.listdir()
    Label(notesscreen4,text="Please Select File From Above:").pack()
    Label(notesscreen4,text=allfiles).pack()
    global  rawfilename3
    rawfilename3=StringVar()
    Entry(notesscreen4,textvariable=rawfilename3).pack()
    Button(notesscreen4,text="ok",command=deletenotes1).pack()
def deletenotes1():
    filename3=rawfilename3.get()
    os.remove(filename3)
    notesscreen4=Toplevel(main_screen)
    notesscreen4.title("Notes")
    notesscreen4.geometry("400x4000")
    Label(notesscreen4,text=filename3+"Removed").pack()
def view():
    notesscreen2=Toplevel(main_screen)
    notesscreen2.title("Info")
    notesscreen2.geometry("250x250")
    allfiles=os.listdir()
    Label(notesscreen2,text="Please Select File From Above:").pack()
    Label(notesscreen2,text=allfiles).pack()
    global  rawfilename1
    rawfilename1=StringVar()
    Entry(notesscreen2,textvariable=rawfilename1).pack()
    Button(notesscreen2,text="ok",command=viewnotes1).pack()
def viewnotes1():
    filename1=rawfilename1.get()
    data=open(filename1,"r")
    data1=data.read()
    notesscreen3=Toplevel(main_screen)
    notesscreen3.title("Notes")
    notesscreen3.geometry("400x4000")
    Label(notesscreen3,text=data1).pack()
    Label(notesscreen3,text=allfiles).pack()


def createnotes():
    global  rawfilename
    rawfilename=StringVar()
    global rawnotes
    rawnotes =StringVar()
    notesscreen1=Toplevel(main_screen)
    notesscreen1.title("Info")
    notesscreen1.geometry("300x250")
    Label(notesscreen1,text="Enter Note Name:").pack()
    Entry(notesscreen1,textvariable=rawfilename).pack()
    Label(notesscreen1,text="Enter Note :").pack()
    Entry(notesscreen1,textvariable=rawnotes).pack()
    Button(notesscreen1,text="Save",command=save).pack()
def saved():
    savescr=Toplevel(main_screen)
    savescr.title("Saved")
    savescr.geometry("100x100")
    Label(savescr,text="Saved").pack()
def save():

    filename=rawfilename.get()
    notes=rawnotes.get()
    data=open(filename,"w")
    data.write(notes)
    data.close()
    saved()
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    main_screen.config(bg="yellow")
    Label(text="Select Your Choice", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="",bg="yellow").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="",bg="yellow").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
