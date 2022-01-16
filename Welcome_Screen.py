from tkinter import *  
from PIL import ImageTk, Image 
from tkinter import ttk
import os
import pandas as pd
from tkinter import messagebox
import emai_verification 
import time


def splash_screen():
    # NOTE splash screen
    splash = Tk()
    splash.geometry('370x200')
    splash.title('WELCOME TO BOOKING BROS!')
    splash.resizable(False,False)
    splash.config(bg='#304049')

    pb = ttk.Progressbar(splash,orient='horizontal',mode='determinate',length=360)
    pb.place(x=5,y=150)
    pb.start(30)

    splash_lablel = Label(splash,text='LODING!',width=20,bg='#304049',justify="center",fg='#F9AA33',highlightthickness=0,borderwidth=0,font = "Helvetica 20 bold")
    splash_lablel.place(x=30,y=40)

    splash.after(3010,lambda:splash.destroy())
    splash.mainloop()

splash_screen()

app = Tk() 

app.geometry('1200x600')
app.resizable(False,False)
app.title("Booking Bros 🎥")
app.config(bg='#F3B745')

email = 0
phone = 0
name = 0

# NOTE loacting backgroung image's absolute file path 
script_dir      = os.path.dirname(__file__)
rel_path        = "resources/welcome_screen_.png"
abs_file_path   = os.path.join(script_dir, rel_path)
img             = Image.open(abs_file_path)
bg              = ImageTk.PhotoImage(img)
label           = Label(app, image=bg,borderwidth=0)
label.place(x = 0,y = 0,)

# NOTE seprator
sep = ttk.Separator(app,orient='vertical',)
sep.place(x=750,relheight=1,relwidth=0.00001)

# NOTE login label on top
def login_label():
    
    custom_login_label = Label(app,text='L O G I N ',
                            bg='#F3B745',
                            width=20,
                            justify="center",
                            fg='white',
                            highlightthickness=0,
                            borderwidth=0,
                            font = "Helvetica 20 bold")
    
    custom_login_label.place(x=825,y=20)

login_label() 

# NOTE customized button function
def submit_btnn(cmd):
    
    custom_button = Button(app,width=10,
                        height=2,
                        text='NEXT',
                        fg='#FF398D',
                        font = "Helvetica 10 bold",
                        bg='#0134FF',
                        activeforeground='#F3B745',
                        activebackground='#0134FF',
                        borderwidth=0,
                        highlightthickness=0,
                        command=cmd)

    
    custom_button.place(x=1050,y=510)
# NOTE email entry widget
def email_entry():
    
    global custom_email_entry
    
    def click(_):
        custom_email_entry.config(state=NORMAL)
        custom_email_entry.delete(0,END)

    def on_enter(e):
        custom_email_entry['background'] = 'white'
        custom_email_entry['foreground'] = '#F3B745'   
    
    def on_leave(e):
        custom_email_entry['background'] = '#F3B745'
        custom_email_entry['foreground'] = 'white'    
    
    custom_email_entry = Entry(app,bg='#F3B745',
                            width=25,
                            justify="center",
                            fg='white',
                            highlightthickness=0,
                            borderwidth=0,
                            font = "Helvetica 20 bold")
    
    custom_email_entry.insert(0, 'EMAIL')
    custom_email_entry.config(state=DISABLED)
    custom_email_entry.bind("<Button-1>",click)
    custom_email_entry.bind("<Enter>",on_enter)
    custom_email_entry.bind("<Leave>",on_leave)
    
    custom_email_entry.place(x=800,y=150)

email_entry() 
# NOTE phone entry widget
def phone_entry():
    
    global custom_phone_entry
    
    def click(_):
        custom_phone_entry.config(state=NORMAL)
        custom_phone_entry.delete(0,END)
        
    def on_enter(e):
        custom_phone_entry['background'] = 'white'
        custom_phone_entry['foreground'] = '#F3B745'   
    
    def on_leave(e):
        custom_phone_entry['background'] = '#F3B745'
        custom_phone_entry['foreground'] = 'white'    
    
    custom_phone_entry = Entry(app,bg='#F3B745',
                            width=25,
                            justify="center",
                            fg='white',
                            highlightthickness=0,
                            borderwidth=0,
                            font = "Helvetica 20 bold")
    
    custom_phone_entry.insert(0, 'PHONE no.')
    custom_phone_entry.config(state=DISABLED)
    custom_phone_entry.bind("<Button-1>",click)
    custom_phone_entry.bind("<Enter>",on_enter)
    custom_phone_entry.bind("<Leave>",on_leave)
    
    custom_phone_entry.place(x=800,y=250)

phone_entry()
# NOTE name entry widget
def name_entry():
    
    global custom_name_entry
    
    def click(_):
        custom_name_entry.config(state=NORMAL)
        custom_name_entry.delete(0,END)
        
    def on_enter(e):
        custom_name_entry['background'] = 'white'
        custom_name_entry['foreground'] = '#F3B745'   
    
    def on_leave(e):
        custom_name_entry['background'] = '#F3B745'
        custom_name_entry['foreground'] = 'white'    
    
    custom_name_entry = Entry(app,bg='#F3B745',
                            width=25,
                            justify="center",
                            fg='white',
                            highlightthickness=0,
                            borderwidth=0,
                            font = "Helvetica 20 bold")
    
    custom_name_entry.insert(0, 'NAME')
    custom_name_entry.config(state=DISABLED)
    custom_name_entry.bind("<Button-1>",click)
    custom_name_entry.bind("<Enter>",on_enter)
    custom_name_entry.bind("<Leave>",on_leave)
    
    custom_name_entry.place(x=800,y=350)

name_entry()         

# NOTE entry widget varibles
def get_email():
    global email
    email = custom_email_entry.get()
    
def get_phone():
    global phone
    phone = custom_phone_entry.get()
    
def get_name():
    global name
    name = custom_name_entry.get()


# NOTE when next button is clicked
def button_cmd():
    get_email()
    get_phone()
    get_name()
    
    
    def ask_number():
        global cc_entry, mynum
        
        top = Toplevel()
        top.geometry('400x100')
        top.title('Confirmation code')
        top.config(bg='black')
        mynum = IntVar(top)
        
        def cc_btn_cmd():
            global final_cc
            print(mynum.get())
            final_cc = mynum.get()
            top.destroy()
            top.update()
            
        cc_entry = Entry(top,bg='#F3B745',
                            width=50,
                            justify="center",
                            fg='white',
                            highlightthickness=0,
                            textvariable = mynum,
                            borderwidth=0) 
        cc_entry.place(x=25,y=30)
        
        cc_btn = Button(top,text='Submit confirmation code',width=40,command=cc_btn_cmd)
        cc_btn.place(x=50,y=60)
        top.mainloop()
        
        
    def verify_email():
    
        if emai_verification.email_validater(email):
            emai_verification.send_email(email)
            messagebox.showinfo('EMAIL SENT',f'A email with confirmation code has been sent to your {email}!\nPlease check your spam folder also!')
            ask_number()
            ucc_code = int(emai_verification.cc_code)
            if ucc_code == final_cc:
                messagebox.showinfo('SUCCESS!',f'Your email {email} is added to our system succesfully!')
                emai_verification.user_info(phone, name, email, ucc_code)
                
            elif ucc_code != final_cc:
                messagebox.showerror('ERROR',f'Your code {final_cc} does not match with code sent!\nKindly check your confirmation code again.')
                
            else:
                messagebox.showerror('ERROR',f'Your code {final_cc} does not match with code sent!\nKindly check your confirmation code again.')

        else:
            messagebox.showerror('ERROR','Error! while validating email')
        
    verify_email()  
        
submit_btnn(button_cmd)    

app.mainloop()