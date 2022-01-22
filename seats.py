import tkinter as tk
import pandas as pd
import tkinter.messagebox as mbox
import user_selection

class MainApp():
    
    def __init__(self,df,date,movie):
        
        self.date = int(date)
        self.movie = movie
        self.price = None
        
        print(self.movie)
        print(self.date)
        
        self.df = df
        
        self.root = tk.Tk()
        
        self.root.title('SEATS')
        self.root.geometry('1200x700')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        self.screen_label = tk.Label(self.root,text='SCREEN',bg='#75736d',fg='white',font='Helvetica 20 bold')
        self.screen_label.place(x=25,y=20,width=1150,height=30)
        
        self.entry_label = tk.Label(self.root,text='E\nN\nT\nR\nY',bg='#75736d',fg='#0ff56f',font='Helvetica 10 bold')
        self.entry_label.place(x=0,y=65,width=20,height=90)
        
        self.exit_label = tk.Label(self.root,text='\nE\nX\nI\nT\n',justify='center',bg='#75736d',fg='#eb5050',font='Helvetica 10 bold')
        self.exit_label.place(x=1180,y=65,width=20,height=90)
      
        self.left_frame_btns()
        self.right_frame_btns()
        self.center_frame_btns()
        self.premium_frame_btns()
        
        self.root.mainloop()
        
        # print(self.date,self,movie)
        
        # print(self.df)
        
        # user_selection.df_to_csv(self.df, self.movie, self.date)
        
        print(self.df)
        # user_selection.df_to_csv(self.df, self.movie, self.date)
        
        
        
    def left_frame_btns(self):
            # left
        self.left_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.left_frame.place(x=30,y=160,height=400,width=310)
        
            # NOTE row 1
        self.Left_row1_column0 = tk.Button(self.left_frame, text='R11',command=lambda: self.left_functions(0,0))  
        self.Left_row1_column0.grid(row=0,ipady=2.5,pady=5,column=0)
        
        self.Left_row1_column1 = tk.Button(self.left_frame,text= 'R12',command=lambda: self.left_functions(0,1))
        self.Left_row1_column1.grid(row=0,ipady=2.5,pady=5,column=1)
        
        self.Left_row1_column2 = tk.Button(self.left_frame, text='R13',command=lambda: self.left_functions(0,2))
        self.Left_row1_column2.grid(row=0,ipady=2.5,pady=5,column=2)
        
        self.Left_row1_column3 = tk.Button(self.left_frame, text='R14',command=lambda: self.left_functions(0,3))
        self.Left_row1_column3.grid(row=0,ipady=2.5,pady=5,column=3)
    
        self.Left_row1_column4 = tk.Button(self.left_frame, text='R15',command=lambda: self.left_functions(0,4))
        self.Left_row1_column4.grid(row=0,ipady=2.5,pady=5,column=4)
        
        self.Left_row1_column5 = tk.Button(self.left_frame, text='R16',command=lambda: self.left_functions(0,5))
        self.Left_row1_column5.grid(row=0,ipady=2.5,pady=5,column=5)
        
            # NOTE row 2
        self.Left_row2_column0 = tk.Button(self.left_frame, text='R21',command=lambda: self.left_functions(1,0))
        self.Left_row2_column0.grid(row=1,ipady=2.5,pady=5,column=0)    
        
        self.Left_row2_column1 = tk.Button(self.left_frame, text='R22',command=lambda: self.left_functions(1,1))
        self.Left_row2_column1.grid(row=1,ipady=2.5,pady=5,column=1)
        
        self.Left_row2_column2 = tk.Button(self.left_frame, text='R23',command=lambda: self.left_functions(1,2))
        self.Left_row2_column2.grid(row=1,ipady=2.5,pady=5,column=2)
        
        self.Left_row2_column3 = tk.Button(self.left_frame, text='R24',command=lambda: self.left_functions(1,3))
        self.Left_row2_column3.grid(row=1,ipady=2.5,pady=5,column=3)
        
        self.Left_row2_column4 = tk.Button(self.left_frame, text='R25',command=lambda: self.left_functions(1,4))
        self.Left_row2_column4.grid(row=1,ipady=2.5,pady=5,column=4)
        
        self.Left_row2_column5 = tk.Button(self.left_frame, text='R26',command=lambda: self.left_functions(1,5))
        self.Left_row2_column5.grid(row=1,ipady=2.5,pady=5,column=5)
                 # Left_row 3
        self.Left_row3_column0 = tk.Button(self.left_frame, text='R31',command=lambda: self.left_functions(2,0))
        self.Left_row3_column0.grid(row=2,ipady=2.5,pady=5,column=0)    
        
        self.Left_row3_column1 = tk.Button(self.left_frame, text='R32',command=lambda: self.left_functions(2,1))
        self.Left_row3_column1.grid(row=2,ipady=2.5,pady=5,column=1)
        
        self.Left_row3_column2 = tk.Button(self.left_frame, text='R33',command=lambda: self.left_functions(2,2))
        self.Left_row3_column2.grid(row=2,ipady=2.5,pady=5,column=2)
        
        self.Left_row3_column3 = tk.Button(self.left_frame, text='R34',command=lambda: self.left_functions(2,3))
        self.Left_row3_column3.grid(row=2,ipady=2.5,pady=5,column=3)
        
        self.Left_row3_column4 = tk.Button(self.left_frame, text='R35',command=lambda: self.left_functions(2,4))
        self.Left_row3_column4.grid(row=2,ipady=2.5,pady=5,column=4)
        
        self.Left_row3_column5 = tk.Button(self.left_frame, text='R36',command=lambda: self.left_functions(2,5))
        self.Left_row3_column5.grid(row=2,ipady=2.5,pady=5,column=5)       
          # Left_row 4
        self.Left_row4_column0 = tk.Button(self.left_frame, text='R41',command=lambda: self.left_functions(3,0))
        self.Left_row4_column0.grid(row=3,ipady=2.5,pady=5,column=0)    
        
        self.Left_row4_column1 = tk.Button(self.left_frame, text='R42',command=lambda: self.left_functions(3,1))
        self.Left_row4_column1.grid(row=3,ipady=2.5,pady=5,column=1)
        
        self.Left_row4_column2 = tk.Button(self.left_frame, text='R43',command=lambda: self.left_functions(3,2))
        self.Left_row4_column2.grid(row=3,ipady=2.5,pady=5,column=2)
        
        self.Left_row4_column3 = tk.Button(self.left_frame, text='R44',command=lambda: self.left_functions(3,3))
        self.Left_row4_column3.grid(row=3,ipady=2.5,pady=5,column=3)
        
        self.Left_row4_column4 = tk.Button(self.left_frame, text='R45',command=lambda: self.left_functions(3,4))
        self.Left_row4_column4.grid(row=3,ipady=2.5,pady=5,column=4)
        
        self.Left_row4_column5 = tk.Button(self.left_frame, text='R46',command=lambda: self.left_functions(3,5))
        self.Left_row4_column5.grid(row=3,ipady=2.5,pady=5,column=5) 
             # Left_row 5
        self.Left_row5_column0 = tk.Button(self.left_frame, text='R51',command=lambda: self.left_functions(4,0))
        self.Left_row5_column0.grid(row=4,ipady=2.5,pady=5,column=0)    
        
        self.Left_row5_column1 = tk.Button(self.left_frame, text='R52',command=lambda: self.left_functions(4,1))
        self.Left_row5_column1.grid(row=4,ipady=2.5,pady=5,column=1)
        
        self.Left_row5_column2 = tk.Button(self.left_frame, text='R53',command=lambda: self.left_functions(4,2))
        self.Left_row5_column2.grid(row=4,ipady=2.5,pady=5,column=2)
        
        self.Left_row5_column3 = tk.Button(self.left_frame, text='R54',command=lambda: self.left_functions(4,3))
        self.Left_row5_column3.grid(row=4,ipady=2.5,pady=5,column=3)
        
        self.Left_row5_column4 = tk.Button(self.left_frame, text='R55',command=lambda: self.left_functions(4,4))
        self.Left_row5_column4.grid(row=4,ipady=2.5,pady=5,column=4)
        
        self.Left_row5_column5 = tk.Button(self.left_frame, text='R56',command=lambda: self.left_functions(4,5))
        self.Left_row5_column5.grid(row=4,ipady=2.5,pady=5,column=5)  
             # Left_row 6
        self.Left_row6_column0 = tk.Button(self.left_frame, text='R61',command=lambda: self.left_functions(5,0))
        self.Left_row6_column0.grid(row=5,ipady=2.5,pady=5,column=0)    
        
        self.Left_row6_column1 = tk.Button(self.left_frame, text='R62',command=lambda: self.left_functions(5,1))
        self.Left_row6_column1.grid(row=5,ipady=2.5,pady=5,column=1)
        
        self.Left_row6_column2 = tk.Button(self.left_frame, text='R63',command=lambda: self.left_functions(5,2))
        self.Left_row6_column2.grid(row=5,ipady=2.5,pady=5,column=2)
        
        self.Left_row6_column3 = tk.Button(self.left_frame, text='R64',command=lambda: self.left_functions(5,3))
        self.Left_row6_column3.grid(row=5,ipady=2.5,pady=5,column=3)
        
        self.Left_row6_column4 = tk.Button(self.left_frame, text='R65',command=lambda: self.left_functions(5,4))
        self.Left_row6_column4.grid(row=5,ipady=2.5,pady=5,column=4)
        
        self.Left_row6_column5 = tk.Button(self.left_frame, text='R66',command=lambda: self.left_functions(5,5))
        self.Left_row6_column5.grid(row=5,ipady=2.5,pady=5,column=5) 
             # Left_row 7
        self.Left_row7_column0 = tk.Button(self.left_frame, text='R71',command=lambda: self.left_functions(6,0))
        self.Left_row7_column0.grid(row=6,ipady=2.5,pady=5,column=0)    
        
        self.Left_row7_column1 = tk.Button(self.left_frame, text='R72',command=lambda: self.left_functions(6,1))
        self.Left_row7_column1.grid(row=6,ipady=2.5,pady=5,column=1)
        
        self.Left_row7_column2 = tk.Button(self.left_frame, text='R73',command=lambda: self.left_functions(6,2))
        self.Left_row7_column2.grid(row=6,ipady=2.5,pady=5,column=2)
        
        self.Left_row7_column3 = tk.Button(self.left_frame, text='R74',command=lambda: self.left_functions(6,3))
        self.Left_row7_column3.grid(row=6,ipady=2.5,pady=5,column=3)
        
        self.Left_row7_column4 = tk.Button(self.left_frame, text='R75',command=lambda: self.left_functions(6,4))
        self.Left_row7_column4.grid(row=6,ipady=2.5,pady=5,column=4)
        
        self.Left_row7_column5 = tk.Button(self.left_frame, text='R76',command=lambda: self.left_functions(6,5))
        self.Left_row7_column5.grid(row=6,ipady=2.5,pady=5,column=5) 
            # Left_row 8
        self.Left_row8_column0 = tk.Button(self.left_frame, text='R81',command=lambda: self.left_functions(7,0))
        self.Left_row8_column0.grid(row=7,ipady=2.5,pady=5,column=0)    
        
        self.Left_row8_column1 = tk.Button(self.left_frame, text='R82',command=lambda: self.left_functions(7,1))
        self.Left_row8_column1.grid(row=7,ipady=2.5,pady=5,column=1)
        
        self.Left_row8_column2 = tk.Button(self.left_frame, text='R83',command=lambda: self.left_functions(7,2))
        self.Left_row8_column2.grid(row=7,ipady=2.5,pady=5,column=2)
        
        self.Left_row8_column3 = tk.Button(self.left_frame, text='R84',command=lambda: self.left_functions(7,3))
        self.Left_row8_column3.grid(row=7,ipady=2.5,pady=5,column=3)
        
        self.Left_row8_column4 = tk.Button(self.left_frame, text='R85',command=lambda: self.left_functions(7,4))
        self.Left_row8_column4.grid(row=7,ipady=2.5,pady=5,column=4)
        
        self.Left_row8_column5 = tk.Button(self.left_frame, text='R86',command=lambda: self.left_functions(7,5))
        self.Left_row8_column5.grid(row=7,ipady=2.5,pady=5,column=5) 
             # Left_row 9
        self.Left_row9_column0 = tk.Button(self.left_frame, text='R91',command=lambda: self.left_functions(8,0))
        self.Left_row9_column0.grid(row=8,ipady=2.5,pady=5,column=0)    
        
        self.Left_row9_column1 = tk.Button(self.left_frame, text='R92',command=lambda: self.left_functions(8,1))
        self.Left_row9_column1.grid(row=8,ipady=2.5,pady=5,column=1)
        
        self.Left_row9_column2 = tk.Button(self.left_frame, text='R93',command=lambda: self.left_functions(8,2))
        self.Left_row9_column2.grid(row=8,ipady=2.5,pady=5,column=2)
        
        self.Left_row9_column3 = tk.Button(self.left_frame, text='R94',command=lambda: self.left_functions(8,3))
        self.Left_row9_column3.grid(row=8,ipady=2.5,pady=5,column=3)
        
        self.Left_row9_column4 = tk.Button(self.left_frame, text='R95',command=lambda: self.left_functions(8,4))
        self.Left_row9_column4.grid(row=8,ipady=2.5,pady=5,column=4)
        
        self.Left_row9_column5 = tk.Button(self.left_frame, text='R96',command=lambda: self.left_functions(8,5))
        self.Left_row9_column5.grid(row=8,ipady=2.5,pady=5,column=5) 
    
    def right_frame_btns(self):
         # right
        self.right_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.right_frame.place(x=860,y=160,height=400,width=310)
        
        self.Right_row1_column0 = tk.Button(self.right_frame, text='R11',command=lambda: self.right_functions(0,0))  
        self.Right_row1_column0.grid(row=0,ipady=2.5,pady=5,column=0)
        
        self.Right_row1_column1 = tk.Button(self.right_frame,text= 'R12',command=lambda: self.right_functions(0,1))
        self.Right_row1_column1.grid(row=0,ipady=2.5,pady=5,column=1)
        
        self.Right_row1_column2 = tk.Button(self.right_frame, text='R13',command=lambda: self.right_functions(0,2))
        self.Right_row1_column2.grid(row=0,ipady=2.5,pady=5,column=2)
        
        self.Right_row1_column3 = tk.Button(self.right_frame, text='R14',command=lambda: self.right_functions(0,3))
        self.Right_row1_column3.grid(row=0,ipady=2.5,pady=5,column=3)
    
        self.Right_row1_column4 = tk.Button(self.right_frame, text='R15',command=lambda: self.right_functions(0,4))
        self.Right_row1_column4.grid(row=0,ipady=2.5,pady=5,column=4)
        
        self.Right_row1_column5 = tk.Button(self.right_frame, text='R16',command=lambda: self.right_functions(0,5))
        self.Right_row1_column5.grid(row=0,ipady=2.5,pady=5,column=5)
        
            # NOTE row 2
        self.Right_row2_column0 = tk.Button(self.right_frame, text='R21',command=lambda: self.right_functions(1,0))
        self.Right_row2_column0.grid(row=1,ipady=2.5,pady=5,column=0)    
        
        self.Right_row2_column1 = tk.Button(self.right_frame, text='R22',command=lambda: self.right_functions(1,1))
        self.Right_row2_column1.grid(row=1,ipady=2.5,pady=5,column=1)
        
        self.Right_row2_column2 = tk.Button(self.right_frame, text='R23',command=lambda: self.right_functions(1,2))
        self.Right_row2_column2.grid(row=1,ipady=2.5,pady=5,column=2)
        
        self.Right_row2_column3 = tk.Button(self.right_frame, text='R24',command=lambda: self.right_functions(1,3))
        self.Right_row2_column3.grid(row=1,ipady=2.5,pady=5,column=3)
        
        self.Right_row2_column4 = tk.Button(self.right_frame, text='R25',command=lambda: self.right_functions(1,4))
        self.Right_row2_column4.grid(row=1,ipady=2.5,pady=5,column=4)
        
        self.Right_row2_column5 = tk.Button(self.right_frame, text='R26',command=lambda: self.right_functions(1,5))
        self.Right_row2_column5.grid(row=1,ipady=2.5,pady=5,column=5)
             # Right_row 3
        self.Right_row3_column0 = tk.Button(self.right_frame, text='R31',command=lambda: self.right_functions(2,0))
        self.Right_row3_column0.grid(row=2,ipady=2.5,pady=5,column=0)    
        
        self.Right_row3_column1 = tk.Button(self.right_frame, text='R32',command=lambda: self.right_functions(2,1))
        self.Right_row3_column1.grid(row=2,ipady=2.5,pady=5,column=1)
        
        self.Right_row3_column2 = tk.Button(self.right_frame, text='R33',command=lambda: self.right_functions(2,2))
        self.Right_row3_column2.grid(row=2,ipady=2.5,pady=5,column=2)
        
        self.Right_row3_column3 = tk.Button(self.right_frame, text='R34',command=lambda: self.right_functions(2,3))
        self.Right_row3_column3.grid(row=2,ipady=2.5,pady=5,column=3)
        
        self.Right_row3_column4 = tk.Button(self.right_frame, text='R35',command=lambda: self.right_functions(2,4))
        self.Right_row3_column4.grid(row=2,ipady=2.5,pady=5,column=4)
        
        self.Right_row3_column5 = tk.Button(self.right_frame, text='R36',command=lambda: self.right_functions(2,5))
        self.Right_row3_column5.grid(row=2,ipady=2.5,pady=5,column=5)       
          # Right_row 4
        self.Right_row4_column0 = tk.Button(self.right_frame, text='R41',command=lambda: self.right_functions(3,0))
        self.Right_row4_column0.grid(row=3,ipady=2.5,pady=5,column=0)    
        
        self.Right_row4_column1 = tk.Button(self.right_frame, text='R42',command=lambda: self.right_functions(3,1))
        self.Right_row4_column1.grid(row=3,ipady=2.5,pady=5,column=1)
        
        self.Right_row4_column2 = tk.Button(self.right_frame, text='R43',command=lambda: self.right_functions(3,2))
        self.Right_row4_column2.grid(row=3,ipady=2.5,pady=5,column=2)
        
        self.Right_row4_column3 = tk.Button(self.right_frame, text='R44',command=lambda: self.right_functions(3,3))
        self.Right_row4_column3.grid(row=3,ipady=2.5,pady=5,column=3)
        
        self.Right_row4_column4 = tk.Button(self.right_frame, text='R45',command=lambda: self.right_functions(3,4))
        self.Right_row4_column4.grid(row=3,ipady=2.5,pady=5,column=4)
        
        self.Right_row4_column5 = tk.Button(self.right_frame, text='R46',command=lambda: self.right_functions(3,5))
        self.Right_row4_column5.grid(row=3,ipady=2.5,pady=5,column=5) 
             # Right_row 5
        self.Right_row5_column0 = tk.Button(self.right_frame, text='R51',command=lambda: self.right_functions(4,0))
        self.Right_row5_column0.grid(row=4,ipady=2.5,pady=5,column=0)    
        
        self.Right_row5_column1 = tk.Button(self.right_frame, text='R52',command=lambda: self.right_functions(4,1))
        self.Right_row5_column1.grid(row=4,ipady=2.5,pady=5,column=1)
        
        self.Right_row5_column2 = tk.Button(self.right_frame, text='R53',command=lambda: self.right_functions(4,2))
        self.Right_row5_column2.grid(row=4,ipady=2.5,pady=5,column=2)
        
        self.Right_row5_column3 = tk.Button(self.right_frame, text='R54',command=lambda: self.right_functions(4,3))
        self.Right_row5_column3.grid(row=4,ipady=2.5,pady=5,column=3)
        
        self.Right_row5_column4 = tk.Button(self.right_frame, text='R55',command=lambda: self.right_functions(4,4))
        self.Right_row5_column4.grid(row=4,ipady=2.5,pady=5,column=4)
        
        self.Right_row5_column5 = tk.Button(self.right_frame, text='R56',command=lambda: self.right_functions(4,5))
        self.Right_row5_column5.grid(row=4,ipady=2.5,pady=5,column=5)  
             # Right_row 6
        self.Right_row6_column0 = tk.Button(self.right_frame, text='R61',command=lambda: self.right_functions(5,0))
        self.Right_row6_column0.grid(row=5,ipady=2.5,pady=5,column=0)    
        
        self.Right_row6_column1 = tk.Button(self.right_frame, text='R62',command=lambda: self.right_functions(5,1))
        self.Right_row6_column1.grid(row=5,ipady=2.5,pady=5,column=1)
        
        self.Right_row6_column2 = tk.Button(self.right_frame, text='R63',command=lambda: self.right_functions(5,2))
        self.Right_row6_column2.grid(row=5,ipady=2.5,pady=5,column=2)
        
        self.Right_row6_column3 = tk.Button(self.right_frame, text='R64',command=lambda: self.right_functions(5,3))
        self.Right_row6_column3.grid(row=5,ipady=2.5,pady=5,column=3)
        
        self.Right_row6_column4 = tk.Button(self.right_frame, text='R65',command=lambda: self.right_functions(5,4))
        self.Right_row6_column4.grid(row=5,ipady=2.5,pady=5,column=4)
        
        self.Right_row6_column5 = tk.Button(self.right_frame, text='R66',command=lambda: self.right_functions(5,5))
        self.Right_row6_column5.grid(row=5,ipady=2.5,pady=5,column=5) 
             # Right_row 7
        self.Right_row7_column0 = tk.Button(self.right_frame, text='R71',command=lambda: self.right_functions(6,0))
        self.Right_row7_column0.grid(row=6,ipady=2.5,pady=5,column=0)    
        
        self.Right_row7_column1 = tk.Button(self.right_frame, text='R72',command=lambda: self.right_functions(6,1))
        self.Right_row7_column1.grid(row=6,ipady=2.5,pady=5,column=1)
        
        self.Right_row7_column2 = tk.Button(self.right_frame, text='R73',command=lambda: self.right_functions(6,2))
        self.Right_row7_column2.grid(row=6,ipady=2.5,pady=5,column=2)
        
        self.Right_row7_column3 = tk.Button(self.right_frame, text='R74',command=lambda: self.right_functions(6,3))
        self.Right_row7_column3.grid(row=6,ipady=2.5,pady=5,column=3)
        
        self.Right_row7_column4 = tk.Button(self.right_frame, text='R75',command=lambda: self.right_functions(6,4))
        self.Right_row7_column4.grid(row=6,ipady=2.5,pady=5,column=4)
        
        self.Right_row7_column5 = tk.Button(self.right_frame, text='R76',command=lambda: self.right_functions(6,5))
        self.Right_row7_column5.grid(row=6,ipady=2.5,pady=5,column=5) 
             # Right_row 8
        self.Right_row8_column0 = tk.Button(self.right_frame, text='R81',command=lambda: self.right_functions(7,0))
        self.Right_row8_column0.grid(row=7,ipady=2.5,pady=5,column=0)    
        
        self.Right_row8_column1 = tk.Button(self.right_frame, text='R82',command=lambda: self.right_functions(7,1))
        self.Right_row8_column1.grid(row=7,ipady=2.5,pady=5,column=1)
        
        self.Right_row8_column2 = tk.Button(self.right_frame, text='R83',command=lambda: self.right_functions(7,2))
        self.Right_row8_column2.grid(row=7,ipady=2.5,pady=5,column=2)
        
        self.Right_row8_column3 = tk.Button(self.right_frame, text='R84',command=lambda: self.right_functions(7,3))
        self.Right_row8_column3.grid(row=7,ipady=2.5,pady=5,column=3)
        
        self.Right_row8_column4 = tk.Button(self.right_frame, text='R85',command=lambda: self.right_functions(7,4))
        self.Right_row8_column4.grid(row=7,ipady=2.5,pady=5,column=4)
        
        self.Right_row8_column5 = tk.Button(self.right_frame, text='R86',command=lambda: self.right_functions(7,5))
        self.Right_row8_column5.grid(row=7,ipady=2.5,pady=5,column=5) 
             # Right_row 9
        self.Right_row9_column0 = tk.Button(self.right_frame, text='R91',command=lambda: self.right_functions(8,0))
        self.Right_row9_column0.grid(row=8,ipady=2.5,pady=5,column=0)    
        
        self.Right_row9_column1 = tk.Button(self.right_frame, text='R92',command=lambda: self.right_functions(8,1))
        self.Right_row9_column1.grid(row=8,ipady=2.5,pady=5,column=1)
        
        self.Right_row9_column2 = tk.Button(self.right_frame, text='R93',command=lambda: self.right_functions(8,2))
        self.Right_row9_column2.grid(row=8,ipady=2.5,pady=5,column=2)
        
        self.Right_row9_column3 = tk.Button(self.right_frame, text='R94',command=lambda: self.right_functions(8,3))
        self.Right_row9_column3.grid(row=8,ipady=2.5,pady=5,column=3)
        
        self.Right_row9_column4 = tk.Button(self.right_frame, text='R95',command=lambda: self.right_functions(8,4))
        self.Right_row9_column4.grid(row=8,ipady=2.5,pady=5,column=4)
        
        self.Right_row9_column5 = tk.Button(self.right_frame, text='R96',command=lambda: self.right_functions(8,5))
        self.Right_row9_column5.grid(row=8,ipady=2.5,pady=5,column=5) 
       
    def center_frame_btns(self):
        # center 
        self.center_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.center_frame.place(x=415,y=160,height=400,width=365)
        
        self.Center_row1_column0 = tk.Button(self.center_frame, text='R11',command=lambda: self.center_functions(0,0))  
        self.Center_row1_column0.grid(row=0,ipady=2.5,pady=5,column=0)
        
        self.Center_row1_column1 = tk.Button(self.center_frame,text= 'R12',command=lambda: self.center_functions(0,1))
        self.Center_row1_column1.grid(row=0,ipady=2.5,pady=5,column=1)
        
        self.Center_row1_column2 = tk.Button(self.center_frame, text='R13',command=lambda: self.center_functions(0,2))
        self.Center_row1_column2.grid(row=0,ipady=2.5,pady=5,column=2)
        
        self.Center_row1_column3 = tk.Button(self.center_frame, text='R14',command=lambda: self.center_functions(0,3))
        self.Center_row1_column3.grid(row=0,ipady=2.5,pady=5,column=3)
    
        self.Center_row1_column4 = tk.Button(self.center_frame, text='R15',command=lambda: self.center_functions(0,4))
        self.Center_row1_column4.grid(row=0,ipady=2.5,pady=5,column=4)
        
        self.Center_row1_column5 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(0,5))
        self.Center_row1_column5.grid(row=0,ipady=2.5,pady=5,column=5)
        
        self.Center_row1_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(0,6))
        self.Center_row1_column6.grid(row=0,ipady=2.5,pady=5,column=6)
        
            # NOTE row 2
        self.Center_row2_column0 = tk.Button(self.center_frame, text='R21',command=lambda: self.center_functions(1,0))
        self.Center_row2_column0.grid(row=1,ipady=2.5,pady=5,column=0)    
        
        self.Center_row2_column1 = tk.Button(self.center_frame, text='R22',command=lambda: self.center_functions(1,1))
        self.Center_row2_column1.grid(row=1,ipady=2.5,pady=5,column=1)
        
        self.Center_row2_column2 = tk.Button(self.center_frame, text='R23',command=lambda: self.center_functions(1,2))
        self.Center_row2_column2.grid(row=1,ipady=2.5,pady=5,column=2)
        
        self.Center_row2_column3 = tk.Button(self.center_frame, text='R24',command=lambda: self.center_functions(1,3))
        self.Center_row2_column3.grid(row=1,ipady=2.5,pady=5,column=3)
        
        self.Center_row2_column4 = tk.Button(self.center_frame, text='R25',command=lambda: self.center_functions(1,4))
        self.Center_row2_column4.grid(row=1,ipady=2.5,pady=5,column=4)
        
        self.Center_row2_column5 = tk.Button(self.center_frame, text='R26',command=lambda: self.center_functions(1,5))
        self.Center_row2_column5.grid(row=1,ipady=2.5,pady=5,column=5)
        
        self.Center_row2_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(1,6))
        self.Center_row2_column6.grid(row=1,ipady=2.5,pady=5,column=6)
        
                 # Center_row 3
        self.Center_row3_column0 = tk.Button(self.center_frame, text='R31',command=lambda: self.center_functions(2,0))
        self.Center_row3_column0.grid(row=2,ipady=2.5,pady=5,column=0)    
        
        self.Center_row3_column1 = tk.Button(self.center_frame, text='R32',command=lambda: self.center_functions(2,1))
        self.Center_row3_column1.grid(row=2,ipady=2.5,pady=5,column=1)
        
        self.Center_row3_column2 = tk.Button(self.center_frame, text='R33',command=lambda: self.center_functions(2,2))
        self.Center_row3_column2.grid(row=2,ipady=2.5,pady=5,column=2)
        
        self.Center_row3_column3 = tk.Button(self.center_frame, text='R34',command=lambda: self.center_functions(2,3))
        self.Center_row3_column3.grid(row=2,ipady=2.5,pady=5,column=3)
        
        self.Center_row3_column4 = tk.Button(self.center_frame, text='R35',command=lambda: self.center_functions(2,4))
        self.Center_row3_column4.grid(row=2,ipady=2.5,pady=5,column=4)
        
        self.Center_row3_column5 = tk.Button(self.center_frame, text='R36',command=lambda: self.center_functions(2,5))
        self.Center_row3_column5.grid(row=2,ipady=2.5,pady=5,column=5) 
        
        self.Center_row3_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(2,6))
        self.Center_row3_column6.grid(row=2,ipady=2.5,pady=5,column=6)      
          # Center_row 4
        self.Center_row4_column0 = tk.Button(self.center_frame, text='R41',command=lambda: self.center_functions(3,0))
        self.Center_row4_column0.grid(row=3,ipady=2.5,pady=5,column=0)    
        
        self.Center_row4_column1 = tk.Button(self.center_frame, text='R42',command=lambda: self.center_functions(3,1))
        self.Center_row4_column1.grid(row=3,ipady=2.5,pady=5,column=1)
        
        self.Center_row4_column2 = tk.Button(self.center_frame, text='R43',command=lambda: self.center_functions(3,2))
        self.Center_row4_column2.grid(row=3,ipady=2.5,pady=5,column=2)
        
        self.Center_row4_column3 = tk.Button(self.center_frame, text='R44',command=lambda: self.center_functions(3,3))
        self.Center_row4_column3.grid(row=3,ipady=2.5,pady=5,column=3)
        
        self.Center_row4_column4 = tk.Button(self.center_frame, text='R45',command=lambda: self.center_functions(3,4))
        self.Center_row4_column4.grid(row=3,ipady=2.5,pady=5,column=4)
        
        self.Center_row4_column5 = tk.Button(self.center_frame, text='R46',command=lambda: self.center_functions(3,5))
        self.Center_row4_column5.grid(row=3,ipady=2.5,pady=5,column=5) 
        
        self.Center_row4_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(3,6))
        self.Center_row4_column6.grid(row=3,ipady=2.5,pady=5,column=6)
             # Center_row 5
        self.Center_row5_column0 = tk.Button(self.center_frame, text='R51',command=lambda: self.center_functions(4,0))
        self.Center_row5_column0.grid(row=4,ipady=2.5,pady=5,column=0)    
        
        self.Center_row5_column1 = tk.Button(self.center_frame, text='R52',command=lambda: self.center_functions(4,1))
        self.Center_row5_column1.grid(row=4,ipady=2.5,pady=5,column=1)
        
        self.Center_row5_column2 = tk.Button(self.center_frame, text='R53',command=lambda: self.center_functions(4,2))
        self.Center_row5_column2.grid(row=4,ipady=2.5,pady=5,column=2)
        
        self.Center_row5_column3 = tk.Button(self.center_frame, text='R54',command=lambda: self.center_functions(4,3))
        self.Center_row5_column3.grid(row=4,ipady=2.5,pady=5,column=3)
        
        self.Center_row5_column4 = tk.Button(self.center_frame, text='R55',command=lambda: self.center_functions(4,4))
        self.Center_row5_column4.grid(row=4,ipady=2.5,pady=5,column=4)
        
        self.Center_row5_column5 = tk.Button(self.center_frame, text='R56',command=lambda: self.center_functions(4,5))
        self.Center_row5_column5.grid(row=4,ipady=2.5,pady=5,column=5) 
        
        self.Center_row5_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(4,6))
        self.Center_row5_column6.grid(row=4,ipady=2.5,pady=5,column=6) 
             # Center_row 6
        self.Center_row6_column0 = tk.Button(self.center_frame, text='R61',command=lambda: self.center_functions(5,0))
        self.Center_row6_column0.grid(row=5,ipady=2.5,pady=5,column=0)    
        
        self.Center_row6_column1 = tk.Button(self.center_frame, text='R62',command=lambda: self.center_functions(5,1))
        self.Center_row6_column1.grid(row=5,ipady=2.5,pady=5,column=1)
        
        self.Center_row6_column2 = tk.Button(self.center_frame, text='R63',command=lambda: self.center_functions(5,2))
        self.Center_row6_column2.grid(row=5,ipady=2.5,pady=5,column=2)
        
        self.Center_row6_column3 = tk.Button(self.center_frame, text='R64',command=lambda: self.center_functions(5,3))
        self.Center_row6_column3.grid(row=5,ipady=2.5,pady=5,column=3)
        
        self.Center_row6_column4 = tk.Button(self.center_frame, text='R65',command=lambda: self.center_functions(5,4))
        self.Center_row6_column4.grid(row=5,ipady=2.5,pady=5,column=4)
        
        self.Center_row6_column5 = tk.Button(self.center_frame, text='R66',command=lambda: self.center_functions(5,5))
        self.Center_row6_column5.grid(row=5,ipady=2.5,pady=5,column=5) 
        
        self.Center_row6_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(5,6))
        self.Center_row6_column6.grid(row=5,ipady=2.5,pady=5,column=6)
             # Center_row 7
        self.Center_row7_column0 = tk.Button(self.center_frame, text='R71',command=lambda: self.center_functions(6,0))
        self.Center_row7_column0.grid(row=6,ipady=2.5,pady=5,column=0)    
        
        self.Center_row7_column1 = tk.Button(self.center_frame, text='R72',command=lambda: self.center_functions(6,1))
        self.Center_row7_column1.grid(row=6,ipady=2.5,pady=5,column=1)
        
        self.Center_row7_column2 = tk.Button(self.center_frame, text='R73',command=lambda: self.center_functions(6,2))
        self.Center_row7_column2.grid(row=6,ipady=2.5,pady=5,column=2)
        
        self.Center_row7_column3 = tk.Button(self.center_frame, text='R74',command=lambda: self.center_functions(6,3))
        self.Center_row7_column3.grid(row=6,ipady=2.5,pady=5,column=3)
        
        self.Center_row7_column4 = tk.Button(self.center_frame, text='R75',command=lambda: self.center_functions(6,4))
        self.Center_row7_column4.grid(row=6,ipady=2.5,pady=5,column=4)
        
        self.Center_row7_column5 = tk.Button(self.center_frame, text='R76',command=lambda: self.center_functions(6,5))
        self.Center_row7_column5.grid(row=6,ipady=2.5,pady=5,column=5) 
        
        self.Center_row7_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(6,6))
        self.Center_row7_column6.grid(row=6,ipady=2.5,pady=5,column=6)
            # Center_row 8
        self.Center_row8_column0 = tk.Button(self.center_frame, text='R81',command=lambda: self.center_functions(7,0))
        self.Center_row8_column0.grid(row=7,ipady=2.5,pady=5,column=0)    
        
        self.Center_row8_column1 = tk.Button(self.center_frame, text='R82',command=lambda: self.center_functions(7,1))
        self.Center_row8_column1.grid(row=7,ipady=2.5,pady=5,column=1)
        
        self.Center_row8_column2 = tk.Button(self.center_frame, text='R83',command=lambda: self.center_functions(7,2))
        self.Center_row8_column2.grid(row=7,ipady=2.5,pady=5,column=2)
        
        self.Center_row8_column3 = tk.Button(self.center_frame, text='R84',command=lambda: self.center_functions(7,3))
        self.Center_row8_column3.grid(row=7,ipady=2.5,pady=5,column=3)
        
        self.Center_row8_column4 = tk.Button(self.center_frame, text='R85',command=lambda: self.center_functions(7,4))
        self.Center_row8_column4.grid(row=7,ipady=2.5,pady=5,column=4)
        
        self.Center_row8_column5 = tk.Button(self.center_frame, text='R86',command=lambda: self.center_functions(7,5))
        self.Center_row8_column5.grid(row=7,ipady=2.5,pady=5,column=5) 
        
        self.Center_row8_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(7,6))
        self.Center_row8_column6.grid(row=7,ipady=2.5,pady=5,column=6)
             # Center_row 9
        self.Center_row9_column0 = tk.Button(self.center_frame, text='R91',command=lambda: self.center_functions(8,0))
        self.Center_row9_column0.grid(row=8,ipady=2.5,pady=5,column=0)    
        
        self.Center_row9_column1 = tk.Button(self.center_frame, text='R92',command=lambda: self.center_functions(8,1))
        self.Center_row9_column1.grid(row=8,ipady=2.5,pady=5,column=1)
        
        self.Center_row9_column2 = tk.Button(self.center_frame, text='R93',command=lambda: self.center_functions(8,2))
        self.Center_row9_column2.grid(row=8,ipady=2.5,pady=5,column=2)
        
        self.Center_row9_column3 = tk.Button(self.center_frame, text='R94',command=lambda: self.center_functions(8,3))
        self.Center_row9_column3.grid(row=8,ipady=2.5,pady=5,column=3)
        
        self.Center_row9_column4 = tk.Button(self.center_frame, text='R95',command=lambda: self.center_functions(8,4))
        self.Center_row9_column4.grid(row=8,ipady=2.5,pady=5,column=4)
        
        self.Center_row9_column5 = tk.Button(self.center_frame, text='R96',command=lambda: self.center_functions(8,5))
        self.Center_row9_column5.grid(row=8,ipady=2.5,pady=5,column=5)
        
        self.Center_row9_column6 = tk.Button(self.center_frame, text='R16',command=lambda: self.center_functions(8,6))
        self.Center_row9_column6.grid(row=8,ipady=2.5,pady=5,column=6)
        
    def premium_frame_btns(self):    
        # premium       
        self.premium_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0,text='\t\t\t\t\t\t\t\tPREMIUM SEATS')
        self.premium_frame.place(x=90,y=600,width=1020,height=80)
        
        self.Premium_row1_column1 = tk.Button(self.premium_frame,  text='P11',command=lambda: self.premium_functions(0,0))
        self.Premium_row1_column1.grid(row=0,column=0,ipady=10)
        
        self.Premium_row1_column2 = tk.Button(self.premium_frame,  text='P12',command=lambda: self.premium_functions(0,1))
        self.Premium_row1_column2.grid(row=0,column=1,ipady=10)
        
        self.Premium_row1_column3 = tk.Button(self.premium_frame,  text='P13',command=lambda: self.premium_functions(0,2))
        self.Premium_row1_column3.grid(row=0,column=2,ipady=10)
        
        self.Premium_row1_column4 = tk.Button(self.premium_frame,  text='P14',command=lambda: self.premium_functions(0,3))
        self.Premium_row1_column4.grid(row=0,column=3,ipady=10)
        
        self.Premium_row1_column5 = tk.Button(self.premium_frame,  text='P15',command=lambda: self.premium_functions(0,4))
        self.Premium_row1_column5.grid(row=0,column=4,ipady=10)
        
        self.Premium_row1_column6 = tk.Button(self.premium_frame,  text='P16',command=lambda: self.premium_functions(0,5))
        self.Premium_row1_column6.grid(row=0,column=5,ipady=10)
        self.Premium_row1_column7 = tk.Button(self.premium_frame,  text='P17',command=lambda: self.premium_functions(0,6))
        self.Premium_row1_column7.grid(row=0,column=6,ipady=10)
        self.Premium_row1_column8 = tk.Button(self.premium_frame,  text='P18',command=lambda: self.premium_functions(0,7))
        self.Premium_row1_column8.grid(row=0,column=7,ipady=10)
        self.Premium_row1_column9 = tk.Button(self.premium_frame,  text='P19',command=lambda: self.premium_functions(0,8))
        self.Premium_row1_column9.grid(row=0,column=8,ipady=10)
        self.Premium_row1_column10 = tk.Button(self.premium_frame,  text='P110',command=lambda: self.premium_functions(0,9))
        self.Premium_row1_column10.grid(row=0,column=9,ipady=10)
        self.Premium_row1_column11 = tk.Button(self.premium_frame,  text='P111',command=lambda: self.premium_functions(0,10))
        self.Premium_row1_column11.grid(row=0,column=10,ipady=10)
        self.Premium_row1_column12 = tk.Button(self.premium_frame,  text='P112',command=lambda: self.premium_functions(0,11))
        self.Premium_row1_column12.grid(row=0,column=11,ipady=10)
        self.Premium_row1_column13 = tk.Button(self.premium_frame,  text='P113',command=lambda: self.premium_functions(0,12))
        self.Premium_row1_column13.grid(row=0,column=12,ipady=10)
        self.Premium_row1_column14 = tk.Button(self.premium_frame,  text='P114',command=lambda: self.premium_functions(0,13))
        self.Premium_row1_column14.grid(row=0,column=13,ipady=10)
        self.Premium_row1_column15 = tk.Button(self.premium_frame,  text='P115',command=lambda: self.premium_functions(0,14))
        self.Premium_row1_column15.grid(row=0,column=14,ipady=10)
        self.Premium_row1_column16 = tk.Button(self.premium_frame,  text='P116',command=lambda: self.premium_functions(0,15))
        self.Premium_row1_column16.grid(row=0,column=15,ipady=10)
        self.Premium_row1_column17 = tk.Button(self.premium_frame,  text='P117',command=lambda: self.premium_functions(0,16))
        self.Premium_row1_column17.grid(row=0,column=16,ipady=10)
        self.Premium_row1_column18 = tk.Button(self.premium_frame,  text='P118',command=lambda: self.premium_functions(0,17))
        self.Premium_row1_column18.grid(row=0,column=17,ipady=10)
        self.Premium_row1_column19 = tk.Button(self.premium_frame,  text='P119',command=lambda: self.premium_functions(0,18))
        self.Premium_row1_column19.grid(row=0,column=18,ipady=10)
    
    
    def premium_functions(self,rows,columns):
        self.pre_side = self.df.iloc[9:,:]
        self.price = 100
        
        if self.df.iloc[rows,columns] == 1:
            self.root.withdraw()
            self.show('SEAT INFO.', f'Selected seat R{rows}{columns} is already booked!')
            self.root.deiconify()
        elif self.df.iloc[rows,columns] == 0:
            
            
            self.df.iloc[rows,columns] = 1
            user_selection.df_to_csv(self.df, self.movie, self.date)
            
            
            self.show('SEAT INFO.', 'Booking successful!')
            self.root.destroy()
        else:
            print('unkknows error')
        
        self.root.destroy()
    
    def left_functions(self,rows,columns):
        
        self.lef_side = self.df.iloc[0:9,0:6]
        self.price = 50
        if self.df.iloc[rows,columns] == 1:
            self.root.withdraw()
            self.show('SEAT INFO.', f'Selected seat R{rows}{columns} is already booked!')
            self.root.deiconify()
            
        elif self.df.iloc[rows,columns] == 0:
            
        
            self.df.iloc[rows,columns] = 1
            user_selection.df_to_csv(self.df, self.movie, self.date)
            
            self.show('SEAT INFO.', 'Booking successful!')
            self.root.destroy()
        else:
            print('unkknows error')
         
           
        
        
    def right_functions(self,rows,columns):
        self.rig_side = self.df.iloc[0:9,13:]
        self.price = 50
        
        if self.df.iloc[rows,columns] == 1:
            self.root.withdraw()
            self.show('SEAT INFO.', f'Selected seat r{rows}{columns} is already booked!')
            self.root.deiconify()
            
        elif self.df.iloc[rows,columns] == 0:
            
            
            self.df.iloc[rows,columns] = 1
            user_selection.df_to_csv(self.df, self.movie, self.date)
            
            self.show('SEAT INFO.', 'Booking successful!')
            self.root.destroy()
            
        else:
            print('unkknows error')
        
        
    
    def center_functions(self,rows,columns):
        self.cen_side = self.df.iloc[0:9,6:13]
        self.price = 80
        
        if self.df.iloc[rows,columns] == 1:
            self.root.withdraw()
            self.show('SEAT INFO.', f'Selected seat r{rows}{columns} is already booked!')
            self.root.deiconify()
            
        elif self.df.iloc[rows,columns] == 0:
            
            
            self.df.iloc[rows,columns] = 1
            user_selection.df_to_csv(self.df, self.movie, self.date)
            self.show('SEAT INFO.', 'Booking successful!')
            self.root.destroy()
            
        else:
            print('unkknows error')
            
        
            
    def show(self,m_title,m_msg):
        
        self.title = m_title
        self.msg = m_msg
        
        self.message = tk.Tk()
        self.message.overrideredirect(True)
        self.message.withdraw()
        
        mbox.showinfo(self.title,self.msg)
        
        self.message.destroy()
        
    
        
# MainApp('hi')