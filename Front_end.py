import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image 
import email_verification 
import tkinter.messagebox as mbox
import pandas
import user_selection
import Main_screen

# splash screen when app starts
class SplashScreen():
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.x = int((self.root.winfo_screenwidth()/2) - (370/2))
        self.y = int((self.root.winfo_screenheight()/2) - (200/2))
        self.root.geometry(f'370x200+{self.x}+{self.y}')
        
        self.root.title('BOOKING BROS!')
        self.root.overrideredirect(True)
        self.root.resizable(False,False)
        
        self.root.config(bg='#455a64')
        
        self.progress_bar = tk.ttk.Progressbar(self.root,orient='horizontal',mode='determinate',length=360)
        self.progress_bar.place(x=5,y=150)
        self.progress_bar.start(30)
        
        self.splash_lablel = tk.Label(self.root,text='WELCOME !',width=20,bg='#455a64',justify="center",fg='#F9AA33',highlightthickness=0,borderwidth=0,font = "Helvetica 20 bold")
        self.splash_lablel.place(x=30,y=40)
        
        self.root.after(3020,self.exit_splash)
        
        self.root.mainloop()
        
    def exit_splash(self):
        self.root.destroy()
        
# when email valid or not        
class Email_pop_up(object):
    
    def __init__(self,master,email):
        
        self.email_pop = tk.Tk()
        
        self.email = email
        
        self.email_pop.geometry('350x100')
        self.email_pop.resizable(False,False)
        
    def valid_email(self):
        
        self.email_pop.title('EMAIL SENT!')
        
        lbl = tk.Label(self.email_pop,justify="center",
                    font = "Helvetica 10 bold",
                    text=f'A email with confirmation code has been sent to your\n"{self.email}"!\nPlease check your spam folder also!')
        lbl.place(x=2,y=0)
        
        btn  = tk.Button(self.email_pop,text='Ok',command=self.email_pop.destroy)
        btn.place(x=160,y=68)
        
    def not_valid_email(self):
        
        self.email_pop.title('EMAIL ERROR!')
        
        lbl = tk.Label(self.email_pop,justify="center",
                    font = "Helvetica 10 bold",
                    text=f'Email entered "{self.email}" is not valid!.\nPlease check your email again')
        lbl.place(x=2,y=0)
        
        btn  = tk.Button(self.email_pop,text='Ok',command=self.email_pop.destroy)
        btn.place(x=160,y=68)
     
# password and info to database        
class Ask_pswd(object):
    
    def __init__(self,email,name,phone,uid):
        
        self.email = email
        self.name = name
        self.phone = phone
        self.original_cc_code = uid
        
        self.pswd_window = tk.Tk()
        self.pswd_window.title('Generate password!')
        self.pswd_window.geometry('350x100')
        self.pswd_window.resizable(False,False)
        self.pswd_window.config(bg='black')
        
        self.paswd_entry = tk.Entry(self.pswd_window,bg='#F3B745',
                                                width=40,
                                                justify="center",
                                                fg='white',
                                                highlightthickness=0,
                                                borderwidth=0)
        self.paswd_entry.place(x=33,y=30)
        
        self.pswd_btn = tk.Button(self.pswd_window,text='Ok',width=40,command=self.password_submit)
        self.pswd_btn.place(x=25,y=60)
        
        self.password = self.paswd_entry.get()
        
        self.pswd_window.mainloop()
        
    
    
    def password_submit(self):
        self.password = str(self.paswd_entry.get())
        email_verification.user_info(self.phone, self.name, self.email, self.original_cc_code,self.password)
        self.pswd_window.destroy()
        Main_screen.Main_window(self.email,self.password)
        
         
# if code valid or not
class C_code_match(object):
    
    def __init__(self,email,final_cc):
        
        self.cc_code_matcher = tk.Tk()
        # self.dest = des_main
        
        self.email = email
        self.final_cc = final_cc
        
        self.cc_code_matcher.geometry('350x100')
        self.cc_code_matcher.resizable(False,False)
       
                
    def if_matched(self):
        
        
        
        self.cc_code_matcher.title('Sucess!')
        
        lbl = tk.Label(self.cc_code_matcher,justify="center",
                    font = "Helvetica 10 bold",
                    text=f'Your email\n{self.email}\nis added to our system succesfully!')
        
        lbl.place(x=50,y=0)
        
        btn  = tk.Button(self.cc_code_matcher,text='Ok',command=self.cc_code_matcher.destroy)
        btn.place(x=180,y=70)
        
        
    def not_matched(self):
        
        self.cc_code_matcher.title('Error!')
        
        lbl = tk.Label(self.cc_code_matcher,justify="center",
                                        font = "Helvetica 10 bold",
                                        text=f'Your confirmation code\n{self.final_cc}\nis not valid\nPlease check again')
        lbl.place(x=2,y=0)
        
        btn  = tk.Button(self.cc_code_matcher,text='Ok',command=self.cc_code_matcher.destroy)
        btn.place(x=180,y=70)

# ask user for confiramtion sent to thier mail
class Confirmation_code(object):
    
    def __init__(self,master,email,name,phone,des_main):
        
        self.cc_code_window = tk.Tk()
        self.master = master
        self.dest = des_main
        
        self.email = email
        self.name = name
        self.phone = phone
        
        self.cc_code_window.geometry('400x100')
        
        self.cc_code_window.title('Confirmation code')
        
        self.cc_code_window.config(bg='black')
        
        self.cc_entry = tk.Entry(self.cc_code_window,bg='#F3B745',
                                        width=50,
                                        justify="center",
                                        fg='white',
                                        highlightthickness=0,
                                        borderwidth=0) 
        self.cc_entry.place(x=25,y=30)
        
        # print(email_verification.cc_code) -> verification code
        
        self.cc_btn = tk.Button(self.cc_code_window,text='Submit confirmation code',width=40,command=self.cc_btn_cmd)
        self.cc_btn.place(x=50,y=60)
        
    def cc_btn_cmd(self):
        
        self.ask_cc_code = int(self.cc_entry.get())
        self.original_cc_code = email_verification.cc_code
        
        if self.ask_cc_code == self.original_cc_code:
            
            self.dest.destroy()
            self.cc_code_window.destroy()
            
            C_code_match(self.email,self.ask_cc_code).if_matched()
            Ask_pswd(self.email,self.name,self.phone,self.original_cc_code)
            # email_verification.user_info(self.phone, self.name, self.email, self.original_cc_code)
            
           
        elif self.ask_cc_code != self.original_cc_code:
            
            C_code_match(self.email,self.ask_cc_code).not_matched()
            
        else:
            
            None
            pass
   
# sign window        
class Signin_window(object):
    
    def __init__(self,des_main):
        
        self.root = tk.Tk()
        
        self.dest = des_main
        
        self.dest.destroy()
        
        self.root.title('sign in ')
        self.root.geometry('400x400')
        
        self.root.config(bg='#F3B745')
        
        # sign in label
        self.custom_signin_label = tk.Label(self.root,text='S I G N  I N ',
                                                    bg='#F3B745',
                                                width=20,
                                                justify="center",
                                                fg='white',
                                                highlightthickness=0,
                                                borderwidth=0,
                                                font = "Helvetica 20 bold")
        self.custom_signin_label.place(x=50,y=10)
        
        # ask email to sign in
        def email_click(_):
            self.signin_email_entry.config(state='normal')
            self.signin_email_entry.delete(0,tk.END)

        def email_on_enter(e):
            self.signin_email_entry['background'] = 'white'
            self.signin_email_entry['foreground'] = '#F3B745'   
        
        def email_on_leave(e):
            self.signin_email_entry['background'] = '#F3B745'
            self.signin_email_entry['foreground'] = 'white'    
        
        self.signin_email_entry = tk.Entry(self.root,bg='#F3B745',
                                width=25,
                                justify="center",
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
        
        self.signin_email_entry.insert(0, 'EMAIL')
        self.signin_email_entry.config(state='disabled')
        self.signin_email_entry.bind("<Button-1>",email_click)
        self.signin_email_entry.bind("<Enter>",email_on_enter)
        self.signin_email_entry.bind("<Leave>",email_on_leave)
        
        self.signin_email_entry.place(x=10,y=90)
        
        # ask password to sign in
        def password_click(_):
            self.signin_pswd_entry.config(state='normal')
            self.signin_pswd_entry.delete(0,tk.END)

        def password_on_enter(e):
            self.signin_pswd_entry['background'] = 'white'
            self.signin_pswd_entry['foreground'] = '#F3B745'   
        
        def password_on_leave(e):
            self.signin_pswd_entry['background'] = '#F3B745'
            self.signin_pswd_entry['foreground'] = 'white'    
        
        self.signin_pswd_entry = tk.Entry(self.root,bg='#F3B745',
                                width=25,
                                justify="center",
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                show='*',
                                font = "Helvetica 20 bold")
        
        self.signin_pswd_entry.insert(0, 'PASSWORD')
        self.signin_pswd_entry.config(state='disabled')
        self.signin_pswd_entry.bind("<Button-1>",password_click)
        self.signin_pswd_entry.bind("<Enter>",password_on_enter)
        self.signin_pswd_entry.bind("<Leave>",password_on_leave)
        
        self.signin_pswd_entry.place(x=10,y=170)
        
        # sign in button
        self.custom_sign_in_button = tk.Button(self.root,width=10,
                                                height=2,
                                                text='Sign-in',
                                                fg='#FF398D',
                                                font = "Helvetica 10 bold",
                                                bg='#0134FF',
                                                activeforeground='#F3B745',
                                                activebackground='#0134FF',
                                                borderwidth=0,
                                                highlightthickness=0,
                                                command=self.signin_button_cmd)
        
        self.custom_sign_in_button.place(x=150,y=280)
         
        self.root.mainloop()
        
    def show(self,m_title,m_msg):
        
        self.title = m_title
        self.msg = m_msg
        
        self.message = tk.Tk()
        self.message.overrideredirect(True)
        
        self.message.withdraw()
        
        mbox.showinfo(self.title,self.msg)
        
        self.message.destroy()
        
    def signin_button_cmd(self):
        
        self.Semail = self.signin_email_entry.get()
        self.Spassword = self.signin_pswd_entry.get()
        
        # check if user exixts in our database or not
        
        def check_user():
            
            database = pandas.read_csv('data/user_credentials.csv')
            
            if self.Semail in database['E-mail'].values:
            
                if self.Spassword in database.loc[database['E-mail']==self.Semail].values:
                    
                    user_selection.who_is_user(self.Semail, self.Spassword)
                    self.root.destroy()
                    
                    
                    Main_screen.Main_window()
                    
                else:
                    
                    self.show('Error', 'Please, check your password again!')
                    
            else:
                
                self.show('Error!', 'User not found!\nPlease check your E-mail again')
                
        check_user()
        
# login window Password
class LoginWindow():
    
    def __init__(self):
        
        self.app = tk.Tk()
        
        self.app.geometry('1200x600')
        self.app.resizable(False,False)
        
        self.app.title("Booking Bros 🎥")
        
        self.app.config(bg='#F3B745')
        
        self.script_dir      = os.path.dirname(__file__)
        self.rel_path        = "resources/welcome_screen_.png"
        self.abs_file_path   = os.path.join(self.script_dir, self.rel_path)
        self.img             = Image.open(self.abs_file_path)
        self.bg              = ImageTk.PhotoImage(self.img)
        self.label           = tk.Label(self.app, image=self.bg,borderwidth=0)
        self.label.place(x = 0,y = 0)
        
        self.sep = ttk.Separator(self.app,orient='vertical',)
        self.sep.place(x=750,relheight=1,relwidth=0.00001)
        
        self.already_user_lbl = tk.Label(self.app,text='Already a member?',bg="#F3B745",justify="center",fg='white',highlightthickness=0,borderwidth=0
                                         ,font = "Helvetica 12 bold")
        self.already_user_lbl.place(x=830,y=480)
        
        self.custom_login_label = tk.Label(self.app,text='L O G I N ',
                                                    bg='#F3B745',
                                                width=20,
                                                justify="center",
                                                fg='white',
                                                highlightthickness=0,
                                                borderwidth=0,
                                                font = "Helvetica 20 bold")
        self.custom_login_label.place(x=825,y=20)
    
    #-----------------------------------------------------email_entry----------------------------------------------------------------
        def email_click(_):
            self.custom_email_entry.config(state='normal')
            self.custom_email_entry.delete(0,tk.END)

        def email_on_enter(e):
            self.custom_email_entry['background'] = 'white'
            self.custom_email_entry['foreground'] = '#F3B745'   
        
        def email_on_leave(e):
            self.custom_email_entry['background'] = '#F3B745'
            self.custom_email_entry['foreground'] = 'white'    
        
        self.custom_email_entry = tk.Entry(self.app,bg='#F3B745',
                                width=25,
                                justify="center",
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
        
        self.custom_email_entry.insert(0, 'EMAIL')
        self.custom_email_entry.config(state='disabled')
        self.custom_email_entry.bind("<Button-1>",email_click)
        self.custom_email_entry.bind("<Enter>",email_on_enter)
        self.custom_email_entry.bind("<Leave>",email_on_leave)
        
        self.custom_email_entry.place(x=800,y=150)
    
    #-----------------------------------------------------phone_entry----------------------------------------------------------------
        def phone_click(_):
            self.custom_phone_entry.config(state='normal')
            self.custom_phone_entry.delete(0,tk.END)

        def phone_on_enter(e):
            self.custom_phone_entry['background'] = 'white'
            self.custom_phone_entry['foreground'] = '#F3B745'   
        
        def phone_on_leave(e):
            self.custom_phone_entry['background'] = '#F3B745'
            self.custom_phone_entry['foreground'] = 'white'
    
        self.custom_phone_entry = tk.Entry(self.app,bg='#F3B745',
                                width=25,
                                justify="center",
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
        
        self.custom_phone_entry.insert(0, 'PHONE no.')
        self.custom_phone_entry.config(state='disabled')
        self.custom_phone_entry.bind("<Button-1>",phone_click)
        self.custom_phone_entry.bind("<Enter>",phone_on_enter)
        self.custom_phone_entry.bind("<Leave>",phone_on_leave)
        
        self.custom_phone_entry.place(x=800,y=250)
    
    #-----------------------------------------------------name_entry-----------------------------------------------------------------
        def name_click(_):
            self.custom_name_entry.config(state='normal')
            self.custom_name_entry.delete(0,tk.END)
            
        def name_on_enter(e):
            self.custom_name_entry['background'] = 'white'
            self.custom_name_entry['foreground'] = '#F3B745'   
        
        def name_on_leave(e):
            self.custom_name_entry['background'] = '#F3B745'
            self.custom_name_entry['foreground'] = 'white'    
        
        self.custom_name_entry = tk.Entry(self.app,bg='#F3B745',
                                width=25,
                                justify="center",
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
        
        self.custom_name_entry.insert(0, 'NAME')
        self.custom_name_entry.config(state='disabled')
        self.custom_name_entry.bind("<Button-1>",name_click)
        self.custom_name_entry.bind("<Enter>",name_on_enter)
        self.custom_name_entry.bind("<Leave>",name_on_leave)
        
        self.custom_name_entry.place(x=800,y=350)      
    
    #-----------------------------------------------------Login_button---------------------------------------------------------------
        self.custom_log_in_button = tk.Button(self.app,width=10,
                                                height=2,
                                                text='Log-in',
                                                fg='white',
                                                font = "Helvetica 10 bold",
                                                bg='#0134FF',
                                                activeforeground='#F3B745',
                                                activebackground='#0134FF',
                                                borderwidth=0,
                                                highlightthickness=0,
                                                command=self.login_button_cmd)
        
        self.custom_log_in_button.place(x=1050,y=510) 
        
    #-----------------------------------------------------Sign-in_button-------------------------------------------------------------
        self.custom_sign_in_button = tk.Button(self.app,width=10,
                                                        height=2,
                                                        text='Sign-in',
                                                        fg='white',
                                                        font = "Helvetica 10 bold",
                                                        bg='#0134FF',
                                                        activeforeground='#F3B745',
                                                        activebackground='#0134FF',
                                                        borderwidth=0,
                                                        highlightthickness=0,
                                                        command=self.Signin_button_cmd)
        self.custom_sign_in_button.place(x=850,y=510)
        self.app.mainloop() 
        
    #-----------------------------------------------------Signin_button_command------------------------------------------------------
    def Signin_button_cmd(self):
        
        Signin_window(self.app)
        
        pass
    
    #-----------------------------------------------------Login_button_command-------------------------------------------------------
    def login_button_cmd(self):
        
        self.name = self.custom_name_entry.get()
        self.email = self.custom_email_entry.get()
        self.phone = self.custom_phone_entry.get()
        
        if (email_verification.email_validater(self.email)) == True:
            
            Email_pop_up(self.app,self.email).valid_email()
            email_verification.send_email(self.email) #--> uncomment this to send real e-mails 
            Confirmation_code(self.app,self.email,self.name,self.phone,self.app)
            
        elif (email_verification.email_validater(self.email)) == False:
            
            self.w = Email_pop_up(self.app, self.email).not_valid_email()
            
        else:
            
            None
            pass


if __name__ == '__main__':
    SplashScreen()
    LoginWindow()
            