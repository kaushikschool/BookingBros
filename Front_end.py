import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image 
import email_verification
from tkinter import messagebox

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
        
        self.splash_lablel = tk.Label(self.root,text='LODING!',width=20,bg='#455a64',justify="center",fg='#F9AA33',highlightthickness=0,borderwidth=0,font = "Helvetica 20 bold")
        self.splash_lablel.place(x=30,y=40)
        
        self.root.after(3020,self.exit_splash)
        
        self.root.mainloop()
        
    def exit_splash(self):
        self.root.destroy()
        
        
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
        
        self.email_pop.title('EMAIL EROOR!')
        
        lbl = tk.Label(self.email_pop,justify="center",
                    font = "Helvetica 10 bold",
                    text=f'Email entered "{self.email}" is not valid!.\nPlease check your email again')
        lbl.place(x=2,y=0)
        
        btn  = tk.Button(self.email_pop,text='Ok',command=self.email_pop.destroy)
        btn.place(x=160,y=68)
        

class C_code_match(object):
    
    def __init__(self,master,email,final_cc):
        
        self.cc_code_matcher = tk.Tk()
        
        self.email = email
        self.final_cc = final_cc
        
        self.cc_code_matcher.geometry('350x100')
        self.cc_code_matcher.resizable(False,False)
        
    def if_matched(self):
        
        self.cc_code_matcher.title('Sucess!')
        
        lbl = tk.Label(self.cc_code_matcher,justify="center",
                    font = "Helvetica 10 bold",
                    text=f'Your email\n{self.email}\nis added to our system succesfully!')
        lbl.place(x=2,y=0)
        
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



class Confirmation_code(object):
    
    def __init__(self,master,email,name,phone):
        
        self.cc_code_window = tk.Tk()
        
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
        
        print(email_verification.cc_code)
        
        self.cc_btn = tk.Button(self.cc_code_window,text='Submit confirmation code',width=40,command=self.cc_btn_cmd)
        self.cc_btn.place(x=50,y=60)
        
    def cc_btn_cmd(self):
        
        self.ask_cc_code = int(self.cc_entry.get())
        self.original_cc_code = email_verification.cc_code
        
        if self.ask_cc_code == self.original_cc_code:
            
            C_code_match(self.cc_code_window,self.email,self.ask_cc_code).if_matched()
            email_verification.user_info(self.phone, self.name, self.email, self.original_cc_code)
            self.cc_code_window.destroy()
           
            
            
        elif self.ask_cc_code != self.original_cc_code:
            
            C_code_match(self.cc_code_window,self.email,self.ask_cc_code).not_matched()
            
        else:
            None
            pass
        


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
        self.label.place(x = 0,y = 0,)
        
        self.sep = ttk.Separator(self.app,orient='vertical',)
        self.sep.place(x=750,relheight=1,relwidth=0.00001)
                
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
    
    #-----------------------------------------------------Submit_button--------------------------------------------------------------
        self.custom_button = tk.Button(self.app,width=10,
                            height=2,
                            text='NEXT',
                            fg='#FF398D',
                            font = "Helvetica 10 bold",
                            bg='#0134FF',
                            activeforeground='#F3B745',
                            activebackground='#0134FF',
                            borderwidth=0,
                            highlightthickness=0,
                            command=self.submit_button_cmd)
        
        self.custom_button.place(x=1050,y=510)
        self.app.mainloop()      
    
    #-----------------------------------------------------Submit_button_command------------------------------------------------------
    def submit_button_cmd(self):
        
        self.name = self.custom_name_entry.get()
        self.email = self.custom_email_entry.get()
        self.phone = self.custom_phone_entry.get()
        
        if (email_verification.email_validater(self.email)) == True:
            
            Email_pop_up(self.app,self.email).valid_email()
            # email_verification.send_email(self.email) #--> uncomment this to send real e-mails 
            Confirmation_code(self.app,self.email,self.name,self.phone)
            
        elif (email_verification.email_validater(self.email)) == False:
            
            self.w = Email_pop_up(self.app, self.email).not_valid_email()
            
        else:
            
            None
            pass
        
        
    def destroy_login_window():
        self.app.destroy()
   

if __name__ == '__main__':
    SplashScreen()
    LoginWindow()
            