#import modules
from tkinter import *
import os

# registration window design

# defining global variables
register_screen=NONE
username= NONE
username_entry=NONE
password=NONE
password_entry=NONE
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1000x900")

    global username
    global password
    global username_entry
    global password_entry
    #takes in the inouts as string variables
    username = StringVar()
    password = StringVar()
    #user instruction lables
    Label(register_screen, text="Please enter a secure username and password", bg="blue").pack()
    Label(register_screen, text="").pack()
    #username lable
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    #setting password
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    #hiding password input
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=15, height=2, bg="green", command = register_user).pack()


# Designing window for login 

login_screen=NONE
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1000x900")
    Label(login_screen, text="Please check for authenication", bg="red").pack()
    Label(login_screen, text="").pack()



    global verifacation
    global checkpassword

    verifacation = StringVar()
    checkpassword = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=verifacation)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=checkpassword, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Registering a first time user

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("Arial", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = verifacation.get()
    password1 = checkpassword.get()
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

# Designing popup for login success
login_success_screen=NONE
password_not_recog_screen=NONE
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
user_not_found_screen=NONE
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Main window design

main_screen=NONE
def themainscreen():
    global main_screen
    main_screen = Tk()
    main_screen.title("KAIF'S LOGIN SYSTEM")
    main_screen.geometry("1000x900")
    Label(text="LOGIN OR REGISTER", bg="green", width="300", height="3", font=("Arial", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="6", width="35", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="6", width="35", command=register).pack()

    main_screen.mainloop()


themainscreen()


# for faang interview question find the repeating letter use a hash to have a count and recording on letter to solve the problem.