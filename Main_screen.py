import tkinter as tk
from tkinter import *
import csv
import user_selection
import os
from PIL import ImageTk, Image 
import cv2
from tkcalendar import Calendar,DateEntry

class Qr(object):
    def __init__(self,master):
        
        
        
        self.img = cv2.imread('resources/Sample_qr.png')
        cv2.imshow("QR CODE (closes after 50 sec)", self.img)
        cv2.waitKey(50000)
        cv2.destroyAllWindows()
        
        self.master = master
        self.master.destroy()
        
class Card(object):
    def __init__(self,product_price,master):
        
        self.master = master
        self.master.destroy()
        
        self.product_price = product_price
        
        self.card = tk.Tk()
        self.card.geometry('500x350')
        self.card.title('Card payment')
        self.card.config(bg='grey')
        self.card.resizable(False,False)

        self.card_payment_lbl = tk.Label(self.card,bg='#F3B745',text='PAY VIA CARD',justify="center",fg='white',highlightthickness=0,borderwidth=0,font='Helvetica 20 bold')
        self.card_payment_lbl.place(x=0,y=0,width=500,height=50)

        # card no
        self.card_no_lbl = tk.Label(self.card,bg='grey',text='CARD No.',justify="center",fg='white',highlightthickness=0,borderwidth=0,font='Helvetica 10 bold')
        self.card_no_lbl.place(x=10,y=80)
        
        # card number
        def card_click(_):
            self.card_entry.config(state='normal')
            self.card_entry.delete(0,tk.END)

        def card_on_enter(e):
            self.card_entry['background'] = 'white'
            self.card_entry['foreground'] = 'black'   
        
        def card_on_leave(e):
            self.card_entry['background'] = '#F3B745'
            self.card_entry['foreground'] = 'white' 
            
        self.card_entry = tk.Entry(self.card,bg='#F3B745',
                                        width=50,
                                        justify="center",
                                        fg='white',
                                        highlightthickness=0,
                                        borderwidth=0) 
        self.card_entry.place(x=120,y=80)
        
        self.card_entry.insert(0, 'CARD NUMBER')   
        self.card_entry.config(state='disabled')
        self.card_entry.bind("<Button-1>",card_click)
        self.card_entry.bind("<Enter>",card_on_enter)
        self.card_entry.bind("<Leave>",card_on_leave)   
        
        
        # card name
        self.card_name_lbl = tk.Label(self.card,bg='grey',text='CARD HOLDER',justify="center",fg='white',highlightthickness=0,borderwidth=0,font='Helvetica 10 bold')
        self.card_name_lbl.place(x=10,y=150)
        
        # card name
        def card_name_click(_):
            self.card_name_entry.config(state='normal')
            self.card_name_entry.delete(0,tk.END)

        def card_name_on_enter(e):
            self.card_name_entry['background'] = 'white'
            self.card_name_entry['foreground'] = 'black'   
        
        def card__name_on_leave(e):
            self.card_name_entry['background'] = '#F3B745'
            self.card_name_entry['foreground'] = 'white' 
            
        self.card_name_entry = tk.Entry(self.card,bg='#F3B745',
                                        width=50,
                                        justify="center",
                                        fg='white',
                                        highlightthickness=0,
                                        borderwidth=0) 
        self.card_name_entry.place(x=120,y=150)
        
        self.card_name_entry.insert(0, 'CARD HOLDER')   
        self.card_name_entry.config(state='disabled')
        self.card_name_entry.bind("<Button-1>",card_name_click)
        self.card_name_entry.bind("<Enter>",card_name_on_enter)
        self.card_name_entry.bind("<Leave>",card__name_on_leave)
        
        
        self.card_exp = tk.Label(self.card,bg='grey',text='CARD EXP.',justify="center",fg='white',highlightthickness=0,borderwidth=0,font='Helvetica 10 bold')
        self.card_exp.place(x=10,y=200)
        self.cal = DateEntry(self.card,width=30,bg="#F3B745",fg="white")
        self.cal.place(x=200,y=200)
        
        # cvv
        self.card_cvv_lbl = tk.Label(self.card,bg='grey',text='CARD CVV',justify="center",fg='white',highlightthickness=0,borderwidth=0,font='Helvetica 10 bold')
        self.card_cvv_lbl.place(x=10,y=250)
        
        def card_cvv_click(_):
            self.card_cvv_entry.config(state='normal')
            self.card_cvv_entry.delete(0,tk.END)

        def card_cvv_on_enter(e):
            self.card_cvv_entry['background'] = 'white'
            self.card_cvv_entry['foreground'] = 'black'   
        
        def card__cvv_on_leave(e):
            self.card_cvv_entry['background'] = '#F3B745'
            self.card_cvv_entry['foreground'] = 'white' 
            
        self.card_cvv_entry = tk.Entry(self.card,bg='#F3B745',
                                        width=50,
                                        justify="center",
                                        fg='white',
                                        highlightthickness=0,
                                        borderwidth=0) 
        self.card_cvv_entry.place(x=120,y=250)
        
        self.card_cvv_entry.insert(0, 'CARD CVV')   
        self.card_cvv_entry.config(state='disabled')
        self.card_cvv_entry.bind("<Button-1>",card_cvv_click)
        self.card_cvv_entry.bind("<Enter>",card_cvv_on_enter)
        self.card_cvv_entry.bind("<Leave>",card__cvv_on_leave)
        
        
        self.card_submit_btn = tk.Button(self.card,text='SUBBMIT',highlightthickness=0,borderwidth=0,fg='black',bg='white',command=self.card.destroy)
        self.card_submit_btn.place(x=50,y=300,height=25,width=400)
          
        self.card.mainloop()



class Payment_screen(object):
    
    def __init__(self,product_name,film_name,stream_name,buy_ticket,product_price):
        
        self.product_name = product_name
        self.film_name = film_name
        self.stream_name = stream_name
        self.buy_ticket = buy_ticket
        self.product_price = product_price
        
        self.payment = tk.Tk()
        self.payment.geometry('500x500')
        self.payment.config(bg='grey')
        self.payment.title('Payment')
        self.payment.resizable(False,False)
        
        
        self.user_info_list = user_selection.user_data()
        
        self.payment_lbl = tk.Label(self.payment,text='PAYMENT',font='Helvetica 20 bold',bg='grey',fg='#F3B745',highlightthickness=0,borderwidth=0)
        self.payment_lbl.place(x=50,width=400,y=20)
        
        self.user_deatil_lbl = tk.Label(self.payment,text=f'USER DETAILS',font='Helvetica 15 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.user_deatil_lbl.place(x=25,width=150,y=100)
        
        self.user_name_lbl = tk.Label(self.payment,text=f'Name: {self.user_info_list[1]}',font='Helvetica 10 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.user_name_lbl.place(x=25,width=200,y=150)
        
        self.user_email_lbl = tk.Label(self.payment,text=f'Email: {self.user_info_list[2]}',font='Helvetica 10 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.user_email_lbl.place(x=25,width=200,y=200)
        
        self.user_phone_lbl = tk.Label(self.payment,text=f'Phone: {self.user_info_list[3]}',font='Helvetica 10 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.user_phone_lbl.place(x=25,width=200,y=250)
        
        self.user_id_lbl = tk.Label(self.payment,text=f'ID: {self.user_info_list[0]}',font='Helvetica 10 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.user_id_lbl.place(x=25,width=200,y=300)
        
        if self.product_name == 'Movie':
            
            self.movie_lbl = tk.Label(self.payment,text=f'Movie: {self.film_name}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.movie_lbl.place(x=25,width=200,y=350)
            
            self.movie_price_label = tk.Label(self.payment,text=f'Price: ${self.product_price}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.movie_price_label.place(x=25,width=200,y=400)
        
        elif self.product_name == 'Stream': 
            
            self.stream_lbl = tk.Label(self.payment,text=f'Stream: {self.stream_name}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.stream_lbl.place(x=25,width=200,y=350)
            
            self.stream_price_label = tk.Label(self.payment,text=f'Price: ${self.product_price}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.stream_price_label.place(x=25,width=200,y=400)
            
        elif self.product_name == 'BuyTicket': 
            
            self.buy_ticket_lbl = tk.Label(self.payment,text=f'Movie: {self.buy_ticket}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.buy_ticket_lbl.place(x=25,width=200,y=350)
            
            self.buy_ticket_price_label = tk.Label(self.payment,text=f'Price: ${self.product_price}',font='Helvetica 10 bold',bg='grey',fg='white',highlightthickness=0,borderwidth=0)
            self.buy_ticket_price_label.place(x=25,width=200,y=400)
            
        else:
            pass
            None
            
            
        self.payment_option_label = tk.Label(self.payment,text='Payment options',font='Helvetica 15 bold',fg='white',bg='grey',highlightthickness=0,borderwidth=0)
        self.payment_option_label.place(x=300,width=200,y=100)
        
        # card payment option
        
        def card_payment_btn_focus(e):
            self.card_payment_btn['background'] ='#F3B745'
            self.card_payment_btn['foreground'] = '#FF00C6'
        
        def card_payment_btn_focus_out(e):
            self.card_payment_btn['background'] =  '#FF00C6'
            self.card_payment_btn['foreground'] = '#F3B745' 
        
        self.card_payment_btn = tk.Button(self.payment,bg='#FF00C6',
                                width=12,
                                justify="center",
                                text='Pay via CARD',
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 15 bold",command=self.card_payment_btn_cmd)
 
        self.card_payment_btn.config(fg='white')
        self.card_payment_btn.bind("<Enter>",card_payment_btn_focus)
        self.card_payment_btn.bind("<Leave>",card_payment_btn_focus_out)
        
        self.card_payment_btn.place(x=300,y=200)
        
        # upi payment option
        
        def upi_payment_btn_focus(e):
            self.upi_payment_btn['background'] ='#F3B745'
            self.upi_payment_btn['foreground'] = '#FF00C6'
        
        def upi_payment_btn_focus_out(e):
            self.upi_payment_btn['background'] =  '#FF00C6'
            self.upi_payment_btn['foreground'] = '#F3B745' 
        
        self.upi_payment_btn = tk.Button(self.payment,bg='#FF00C6',
                                width=12,
                                justify="center",
                                text='Pay via UPI',
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 15 bold",command=self.upi_payment_btn_cmd)
 
        self.upi_payment_btn.config(fg='white')
        self.upi_payment_btn.bind("<Enter>",upi_payment_btn_focus)
        self.upi_payment_btn.bind("<Leave>",upi_payment_btn_focus_out)
        
        self.upi_payment_btn.place(x=300,y=300)
            
        self.payment.mainloop()
        
    def upi_payment_btn_cmd(self):
        
        Qr(self.payment)
        
        
    def card_payment_btn_cmd(self):
        Card(self.product_price,self.payment)
    

class Movie_frame(object):
    
    def __init__(self,master):
        
        self.master = master
        
        self.mframe = LabelFrame(self.master,highlightthickness=0,borderwidth=0,text='MOVIES',font='Helvetica 20 bold',bg='grey')
        self.mframe.place(x=350,y=100,height=490,width=540)
        
        self.movie_data = 'movies_data/Movies_dataset.csv'
        self.File  = open(self.movie_data)
        self.Reader = csv.reader(self.File)
        self.Data = list(self.Reader)
        del(self.Data[0])
        
        list_of_entry = []
        for x in list(range(0,len(self.Data))):
            list_of_entry.append(self.Data[x][0])
        
        # movie list
        self.var = tk.StringVar(value=list_of_entry)
        self.list_box = tk.Listbox(self.mframe,listvariable=self.var,font='Helvetica 20 bold',bg='white',fg='black')
        self.list_box.place(x=5,y=10,height=300,width=530)
        
    # btn to select movie and next
        self.next  = tk.Button(self.mframe,text='Next',command=self.next_btn_command)
        self.next.place(x=235,y=400)    
        
    # btn to select movie and next
        self.back = tk.Button(self.mframe,text='Back',command=self.back_btn_cmd)
        self.back.place(x=135,y=400)
        
    def movie_labels(self,master,lbl_text,xp,yp):
        
        self.xp = xp
        self.yp = yp
        self.master = master
        self.lbl_text = lbl_text
        
        self.lbl = tk.Label(self.master,highlightthickness=0,borderwidth=0,text=f'{self.lbl_text}',font='Helvetica 10 bold',fg='white',bg='black')
        self.lbl.place(x=self.xp,y=self.yp)
        
        
        
    def next_btn_command(self):
        
        self.lbox_index = self.list_box.curselection()[0]
        
        self.movie_name = self.Data[self.lbox_index][0]
        self.movie_genre = self.Data[self.lbox_index][1]
        self.movie_lead_studio = self.Data[self.lbox_index][2]
        self.movie_rating = int(self.Data[self.lbox_index][3])
        self.movie_price = int(self.Data[self.lbox_index][4])
        
        
        self.movie_deatil_frame = tk.LabelFrame(self.mframe,highlightthickness=0,borderwidth=0,text='MOVIES',font='Helvetica 20 bold',bg='black')
        self.movie_deatil_frame.place(x=5,y=10,height=300,width=530)
        
        self.movie_labels(self.movie_deatil_frame, 'MOVIE', 230, 4)
        self.film_name_label = tk.Label(self.movie_deatil_frame,text=f'{self.movie_name}',font='Helvetica 20 bold')
        self.film_name_label.place(x=15,y=20,width=500,height=40)
        
        self.movie_labels(self.movie_deatil_frame, 'GENRE', 230, 64)
        self.film_genre_label = tk.Label(self.movie_deatil_frame,text=f'{self.movie_genre}',font='Helvetica 20 bold')
        self.film_genre_label.place(x=15,y=80,width=500,height=40)
        
        self.movie_labels(self.movie_deatil_frame, 'STUDIO', 230, 124)
        self.film_lead_studio_label = tk.Label(self.movie_deatil_frame,text=f'{self.movie_lead_studio}',font='Helvetica 20 bold')
        self.film_lead_studio_label.place(x=15,y=140,width=500,height=40)
        
        self.movie_labels(self.movie_deatil_frame, 'RATING', 230, 184)
        self.film_lead_studio_label = tk.Label(self.movie_deatil_frame,text=f'{self.movie_rating/10}',font='Helvetica 20 bold')
        self.film_lead_studio_label.place(x=15,y=200,width=500,height=40)
        
        user_selection.movie(self.movie_name, self.movie_price)
        
        self.buy_movie_btn = tk.Button(self.mframe,text='Buy and watch movie online!',command=self.buy_movie_btn_cmd)
        self.buy_movie_btn.place(x=335,y=400)
    
        self.list_box.lower()
        
    def buy_movie_btn_cmd(self):
        Payment_screen('Movie', self.movie_name, None, None, self.movie_price)
        
    def back_btn_cmd(self):
        
        self.list_box.lift()
        

class Main_window():
    
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title('Booking Bros')
        self.root.geometry('900x600')
        self.root.resizable(False,False)
        self.root.config(bg='#F3B745')
        
        # main label
        self.main_lblb = tk.Label(self.root,text='welcome To Booking Bros',
                                                bg='#F3B745',
                                                justify="center",
                                                fg='white',
                                                highlightthickness=0,
                                                borderwidth=0,
                                                font = "Helvetica 20 bold")
        self.main_lblb.place(x=280,y=20)
        
        # Movie button
        
        def movie_btn_focus(e):
            self.movie_btn['background'] ='#F3B745'
            self.movie_btn['foreground'] = '#FF00C6'
        
        def movie_btn_focus_out(e):
            self.movie_btn['background'] =  '#FF00C6'
            self.movie_btn['foreground'] = '#F3B745' 
        
        self.movie_btn = tk.Button(self.root,bg='#FF00C6',
                                width=12,
                                justify="center",
                                text='MOVIES',
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold",command=self.mfarme)
 
        self.movie_btn.config(fg='white')
        self.movie_btn.bind("<Enter>",movie_btn_focus)
        self.movie_btn.bind("<Leave>",movie_btn_focus_out)
        
        self.movie_btn.place(x=50,y=225)
        
        # Stream buton
        def stream_btn_focus(e):
            self.stream_btn['background'] ='#F3B745'
            self.stream_btn['foreground'] = '#FF00C6'
        
        def stream_btn_focus_out(e):
            self.stream_btn['background'] =  '#FF00C6'
            self.stream_btn['foreground'] = '#F3B745' 
        
        self.stream_btn = tk.Button(self.root,bg='#FF00C6',
                                width=12,
                                justify="center",
                                text='STREAMS',
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
 
        self.stream_btn.config(fg='white')
        self.stream_btn.bind("<Enter>",stream_btn_focus)
        self.stream_btn.bind("<Leave>",stream_btn_focus_out)
        
        self.stream_btn.place(x=50,y=325)
        
        # website button
        def website_btn_focus(e):
            self.website_btn['background'] ='#F3B745'
            self.website_btn['foreground'] = '#FF00C6'
        
        def website_btn_focus_out(e):
            self.website_btn['background'] =  '#FF00C6'
            self.website_btn['foreground'] = '#F3B745' 
        
        self.website_btn = tk.Button(self.root,bg='#FF00C6',
                                width=12,
                                justify="center",
                                text='WEBSITE',
                                fg='white',
                                highlightthickness=0,
                                borderwidth=0,
                                font = "Helvetica 20 bold")
        
        
 
        self.website_btn.config(fg='white')
        self.website_btn.bind("<Enter>",website_btn_focus)
        self.website_btn.bind("<Leave>",website_btn_focus_out)
        
        self.website_btn.place(x=50,y=425)
        
        self.root.mainloop()
        
    def mfarme(self):
        Movie_frame(self.root)

# Main_window()