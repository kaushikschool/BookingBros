import tkinter as tk
from tkinter import *
import csv


class Movie_frame(object):
    
    def __init__(self,master):
        
        self.master = master
        
        self.mframe = LabelFrame(self.master,highlightthickness=0,borderwidth=0,text='MOVIES',font='Helvetica 20 bold',bg='grey')
        self.mframe.place(x=350,y=100,height=490,width=540)
        
        self.labl = tk.Label(self.mframe,text='hi')
        self.labl.place(x=50,y=100)
        
        movie_data = 'movies_data/Movies_dataset.csv'
        File  = open(movie_data)
        Reader = csv.reader(File)
        Data = list(Reader)
        del(Data[0])
        
        list_of_entry = []
        for x in list(range(0,len(Data))):
            list_of_entry.append(Data[x][0])
        
        # movie list
        self.var = tk.StringVar(value=list_of_entry)
        self.list_box = tk.Listbox(self.mframe,listvariable=self.var,font='Helvetica 20 bold',bg='white',fg='black')
        self.list_box.place(x=5,y=10,height=300,width=530)
        
    # btn to select movie
        self.select_movie  = tk.Button(self.mframe,text='Next')
        self.select_movie.place(x=235,y=400)    
        
        

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

Main_window()