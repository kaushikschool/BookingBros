import tkinter as tk

class MainApp():
    
    def __init__(self,df):
        
        self.df = df
        print('database')
        print(df)
        
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
        
      
      
    def left_frame_btns(self):
        # left
        self.left_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.left_frame.place(x=30,y=160,height=400,width=310)
            # row 1
        self.Left_row1_column0 = self.seat(self.left_frame,0, 0, 'R11')    
        self.Left_row1_column1 = self.seat(self.left_frame,0, 1, 'R12')
        self.Left_row1_column2 = self.seat(self.left_frame,0, 2, 'R13')
        self.Left_row1_column3 = self.seat(self.left_frame,0, 3, 'R14')
        self.Left_row1_column4 = self.seat(self.left_frame,0, 4, 'R15')
        self.Left_row1_column5 = self.seat(self.left_frame,0, 5, 'R16')  
            # Left_row 2
        self.Left_row2_column0 = self.seat(self.left_frame,1, 0, 'R21')    
        self.Left_row2_column1 = self.seat(self.left_frame,1, 1, 'R22')
        self.Left_row2_column2 = self.seat(self.left_frame,1, 2, 'R23')
        self.Left_row2_column3 = self.seat(self.left_frame,1, 3, 'R24')
        self.Left_row2_column4 = self.seat(self.left_frame,1, 4, 'R25')
        self.Left_row2_column5 = self.seat(self.left_frame,1, 5, 'R26')
            # Left_row 3
        self.Left_row3_column0 = self.seat(self.left_frame,2, 0, 'R31')    
        self.Left_row3_column1 = self.seat(self.left_frame,2, 1, 'R32')
        self.Left_row3_column2 = self.seat(self.left_frame,2, 2, 'R33')
        self.Left_row3_column3 = self.seat(self.left_frame,2, 3, 'R34')
        self.Left_row3_column4 = self.seat(self.left_frame,2, 4, 'R35')
        self.Left_row3_column5 = self.seat(self.left_frame,2, 5, 'R36')       
          # Left_row 4
        self.Left_row4_column0 = self.seat(self.left_frame,3, 0, 'R41')    
        self.Left_row4_column1 = self.seat(self.left_frame,3, 1, 'R42')
        self.Left_row4_column2 = self.seat(self.left_frame,3, 2, 'R43')
        self.Left_row4_column3 = self.seat(self.left_frame,3, 3, 'R44')
        self.Left_row4_column4 = self.seat(self.left_frame,3, 4, 'R45')
        self.Left_row4_column5 = self.seat(self.left_frame,3, 5, 'R46')
            # Left_row 5
        self.Left_row5_column0 = self.seat(self.left_frame,4, 0, 'R51')    
        self.Left_row5_column1 = self.seat(self.left_frame,4, 1, 'R52')
        self.Left_row5_column2 = self.seat(self.left_frame,4, 2, 'R53')
        self.Left_row5_column3 = self.seat(self.left_frame,4, 3, 'R54')
        self.Left_row5_column4 = self.seat(self.left_frame,4, 4, 'R55')
        self.Left_row5_column5 = self.seat(self.left_frame,4, 5, 'R56')  
            # Left_row 6
        self.Left_row6_column0 = self.seat(self.left_frame,5, 0, 'R61')    
        self.Left_row6_column1 = self.seat(self.left_frame,5, 1, 'R62')
        self.Left_row6_column2 = self.seat(self.left_frame,5, 2, 'R63')
        self.Left_row6_column3 = self.seat(self.left_frame,5, 3, 'R64')
        self.Left_row6_column4 = self.seat(self.left_frame,5, 4, 'R65')
        self.Left_row6_column5 = self.seat(self.left_frame,5, 5, 'R66') 
            # Left_row 7
        self.Left_row7_column0 = self.seat(self.left_frame,6, 0, 'R71')    
        self.Left_row7_column1 = self.seat(self.left_frame,6, 1, 'R72')
        self.Left_row7_column2 = self.seat(self.left_frame,6, 2, 'R73')
        self.Left_row7_column3 = self.seat(self.left_frame,6, 3, 'R74')
        self.Left_row7_column4 = self.seat(self.left_frame,6, 4, 'R75')
        self.Left_row7_column5 = self.seat(self.left_frame,6, 5, 'R76') 
            # Left_row 8
        self.Left_row8_column0 = self.seat(self.left_frame,7, 0, 'R81')    
        self.Left_row8_column1 = self.seat(self.left_frame,7, 1, 'R82')
        self.Left_row8_column2 = self.seat(self.left_frame,7, 2, 'R83')
        self.Left_row8_column3 = self.seat(self.left_frame,7, 3, 'R84')
        self.Left_row8_column4 = self.seat(self.left_frame,7, 4, 'R85')
        self.Left_row8_column5 = self.seat(self.left_frame,7, 5, 'R86') 
            # Left_row 9
        self.Left_row9_column0 = self.seat(self.left_frame,8, 0, 'R91')    
        self.Left_row9_column1 = self.seat(self.left_frame,8, 1, 'R92')
        self.Left_row9_column2 = self.seat(self.left_frame,8, 2, 'R93')
        self.Left_row9_column3 = self.seat(self.left_frame,8, 3, 'R94')
        self.Left_row9_column4 = self.seat(self.left_frame,8, 4, 'R95')
        self.Left_row9_column5 = self.seat(self.left_frame,8, 5, 'R96') 
    
    def right_frame_btns(self):
        # right
        self.right_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.right_frame.place(x=860,y=160,height=400,width=310)
        
        self.Right_row1_column0 = self.seat(self.right_frame,0, 0, 'R11')    
        self.Right_row1_column1 = self.seat(self.right_frame,0, 1, 'R12')
        self.Right_row1_column2 = self.seat(self.right_frame,0, 2, 'R13')
        self.Right_row1_column3 = self.seat(self.right_frame,0, 3, 'R14')
        self.Right_row1_column4 = self.seat(self.right_frame,0, 4, 'R15')
        self.Right_row1_column5 = self.seat(self.right_frame,0, 5, 'R16')  
            # row 2
        self.Right_row2_column0 = self.seat(self.right_frame,1, 0, 'R21')    
        self.Right_row2_column1 = self.seat(self.right_frame,1, 1, 'R22')
        self.Right_row2_column2 = self.seat(self.right_frame,1, 2, 'R23')
        self.Right_row2_column3 = self.seat(self.right_frame,1, 3, 'R24')
        self.Right_row2_column4 = self.seat(self.right_frame,1, 4, 'R25')
        self.Right_row2_column5 = self.seat(self.right_frame,1, 5, 'R26')
            # row 3
        self.Right_row3_column0 = self.seat(self.right_frame,2, 0, 'R31')    
        self.Right_row3_column1 = self.seat(self.right_frame,2, 1, 'R32')
        self.Right_row3_column2 = self.seat(self.right_frame,2, 2, 'R33')
        self.Right_row3_column3 = self.seat(self.right_frame,2, 3, 'R34')
        self.Right_row3_column4 = self.seat(self.right_frame,2, 4, 'R35')
        self.Right_row3_column5 = self.seat(self.right_frame,2, 5, 'R36')       
          # row 4
        self.Right_row4_column0 = self.seat(self.right_frame,3, 0, 'R41')    
        self.Right_row4_column1 = self.seat(self.right_frame,3, 1, 'R42')
        self.Right_row4_column2 = self.seat(self.right_frame,3, 2, 'R43')
        self.Right_row4_column3 = self.seat(self.right_frame,3, 3, 'R44')
        self.Right_row4_column4 = self.seat(self.right_frame,3, 4, 'R45')
        self.Right_row4_column5 = self.seat(self.right_frame,3, 5, 'R46')
            # row 5
        self.Right_row5_column0 = self.seat(self.right_frame,4, 0, 'R51')    
        self.Right_row5_column1 = self.seat(self.right_frame,4, 1, 'R52')
        self.Right_row5_column2 = self.seat(self.right_frame,4, 2, 'R53')
        self.Right_row5_column3 = self.seat(self.right_frame,4, 3, 'R54')
        self.Right_row5_column4 = self.seat(self.right_frame,4, 4, 'R55')
        self.Right_row5_column5 = self.seat(self.right_frame,4, 5, 'R56')  
            # row 6
        self.Right_row6_column0 = self.seat(self.right_frame,5, 0, 'R61')    
        self.Right_row6_column1 = self.seat(self.right_frame,5, 1, 'R62')
        self.Right_row6_column2 = self.seat(self.right_frame,5, 2, 'R63')
        self.Right_row6_column3 = self.seat(self.right_frame,5, 3, 'R64')
        self.Right_row6_column4 = self.seat(self.right_frame,5, 4, 'R65')
        self.Right_row6_column5 = self.seat(self.right_frame,5, 5, 'R66') 
            # row 7
        self.Right_row7_column0 = self.seat(self.right_frame,6, 0, 'R71')    
        self.Right_row7_column1 = self.seat(self.right_frame,6, 1, 'R72')
        self.Right_row7_column2 = self.seat(self.right_frame,6, 2, 'R73')
        self.Right_row7_column3 = self.seat(self.right_frame,6, 3, 'R74')
        self.Right_row7_column4 = self.seat(self.right_frame,6, 4, 'R75')
        self.Right_row7_column5 = self.seat(self.right_frame,6, 5, 'R76') 
            # row 8
        self.Right_row8_column0 = self.seat(self.right_frame,7, 0, 'R81')    
        self.Right_row8_column1 = self.seat(self.right_frame,7, 1, 'R82')
        self.Right_row8_column2 = self.seat(self.right_frame,7, 2, 'R83')
        self.Right_row8_column3 = self.seat(self.right_frame,7, 3, 'R84')
        self.Right_row8_column4 = self.seat(self.right_frame,7, 4, 'R85')
        self.Right_row8_column5 = self.seat(self.right_frame,7, 5, 'R86') 
            # row 9
        self.Right_row9_column0 = self.seat(self.right_frame,8, 0, 'R91')    
        self.Right_row9_column1 = self.seat(self.right_frame,8, 1, 'R92')
        self.Right_row9_column2 = self.seat(self.right_frame,8, 2, 'R93')
        self.Right_row9_column3 = self.seat(self.right_frame,8, 3, 'R94')
        self.Right_row9_column4 = self.seat(self.right_frame,8, 4, 'R95')
        self.Right_row9_column5 = self.seat(self.right_frame,8, 5, 'R96') 
       
    def center_frame_btns(self):
        # center 
        self.center_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0)
        self.center_frame.place(x=415,y=160,height=400,width=365)
        
        self.Center_row1_column0 = self.seat(self.center_frame,0, 0, 'R11')    
        self.Center_row1_column1 = self.seat(self.center_frame,0, 1, 'R12')
        self.Center_row1_column2 = self.seat(self.center_frame,0, 2, 'R13')
        self.Center_row1_column3 = self.seat(self.center_frame,0, 3, 'R14')
        self.Center_row1_column4 = self.seat(self.center_frame,0, 4, 'R15')
        self.Center_row1_column5 = self.seat(self.center_frame,0, 5, 'R16')
        self.Center_row1_column6 = self.seat(self.center_frame,0, 6, 'R17') 
            # Center_row 2
        self.Center_row2_column0 = self.seat(self.center_frame,1, 0, 'R21')    
        self.Center_row2_column1 = self.seat(self.center_frame,1, 1, 'R22')
        self.Center_row2_column2 = self.seat(self.center_frame,1, 2, 'R23')
        self.Center_row2_column3 = self.seat(self.center_frame,1, 3, 'R24')
        self.Center_row2_column4 = self.seat(self.center_frame,1, 4, 'R25')
        self.Center_row2_column5 = self.seat(self.center_frame,1, 5, 'R26')
        self.Center_row2_column6 = self.seat(self.center_frame,1, 6, 'R27')
            # Center_row 3
        self.Center_row3_column0 = self.seat(self.center_frame,2, 0, 'R31')    
        self.Center_row3_column1 = self.seat(self.center_frame,2, 1, 'R32')
        self.Center_row3_column2 = self.seat(self.center_frame,2, 2, 'R33')
        self.Center_row3_column3 = self.seat(self.center_frame,2, 3, 'R34')
        self.Center_row3_column4 = self.seat(self.center_frame,2, 4, 'R35')
        self.Center_row3_column5 = self.seat(self.center_frame,2, 5, 'R36') 
        self.Center_row3_column6 = self.seat(self.center_frame,2, 6, 'R37')      
          # Center_row 4
        self.Center_row4_column0 = self.seat(self.center_frame,3, 0, 'R41')    
        self.Center_row4_column1 = self.seat(self.center_frame,3, 1, 'R42')
        self.Center_row4_column2 = self.seat(self.center_frame,3, 2, 'R43')
        self.Center_row4_column3 = self.seat(self.center_frame,3, 3, 'R44')
        self.Center_row4_column4 = self.seat(self.center_frame,3, 4, 'R45')
        self.Center_row4_column5 = self.seat(self.center_frame,3, 5, 'R46')
        self.Center_row4_column6 = self.seat(self.center_frame,3, 6, 'R47')
            # Center_row 5
        self.Center_row5_column0 = self.seat(self.center_frame,4, 0, 'R51')    
        self.Center_row5_column1 = self.seat(self.center_frame,4, 1, 'R52')
        self.Center_row5_column2 = self.seat(self.center_frame,4, 2, 'R53')
        self.Center_row5_column3 = self.seat(self.center_frame,4, 3, 'R54')
        self.Center_row5_column4 = self.seat(self.center_frame,4, 4, 'R55')
        self.Center_row5_column5 = self.seat(self.center_frame,4, 5, 'R56') 
        self.Center_row5_column6 = self.seat(self.center_frame,4, 6, 'R57') 
            # Center_row 6
        self.Center_row6_column0 = self.seat(self.center_frame,5, 0, 'R61')    
        self.Center_row6_column1 = self.seat(self.center_frame,5, 1, 'R62')
        self.Center_row6_column2 = self.seat(self.center_frame,5, 2, 'R63')
        self.Center_row6_column3 = self.seat(self.center_frame,5, 3, 'R64')
        self.Center_row6_column4 = self.seat(self.center_frame,5, 4, 'R65')
        self.Center_row6_column5 = self.seat(self.center_frame,5, 5, 'R66') 
        self.Center_row6_column6 = self.seat(self.center_frame,5, 6, 'R67')
            # Center_row 7
        self.Center_row7_column0 = self.seat(self.center_frame,6, 0, 'R71')    
        self.Center_row7_column1 = self.seat(self.center_frame,6, 1, 'R72')
        self.Center_row7_column2 = self.seat(self.center_frame,6, 2, 'R73')
        self.Center_row7_column3 = self.seat(self.center_frame,6, 3, 'R74')
        self.Center_row7_column4 = self.seat(self.center_frame,6, 4, 'R75')
        self.Center_row7_column5 = self.seat(self.center_frame,6, 5, 'R76') 
        self.Center_row7_column6 = self.seat(self.center_frame,6, 6, 'R77')
            # Center_row 8
        self.Center_row8_column0 = self.seat(self.center_frame,7, 0, 'R81')    
        self.Center_row8_column1 = self.seat(self.center_frame,7, 1, 'R82')
        self.Center_row8_column2 = self.seat(self.center_frame,7, 2, 'R83')
        self.Center_row8_column3 = self.seat(self.center_frame,7, 3, 'R84')
        self.Center_row8_column4 = self.seat(self.center_frame,7, 4, 'R85')
        self.Center_row8_column5 = self.seat(self.center_frame,7, 5, 'R86') 
        self.Center_row8_column6 = self.seat(self.center_frame,7, 6, 'R87')
            # Center_row 9
        self.Center_row9_column0 = self.seat(self.center_frame,8, 0, 'R91')    
        self.Center_row9_column1 = self.seat(self.center_frame,8, 1, 'R92')
        self.Center_row9_column2 = self.seat(self.center_frame,8, 2, 'R93')
        self.Center_row9_column3 = self.seat(self.center_frame,8, 3, 'R94')
        self.Center_row9_column4 = self.seat(self.center_frame,8, 4, 'R95')
        self.Center_row9_column5 = self.seat(self.center_frame,8, 5, 'R96')
        self.Center_row9_column6 = self.seat(self.center_frame,8, 6, 'R97') 
        
    def premium_frame_btns(self):    
        # premium       
        self.premium_frame = tk.LabelFrame(self.root,highlightthickness=0,borderwidth=0,text='\t\t\t\t\t\t\t\tPREMIUM SEATS')
        self.premium_frame.place(x=90,y=600,width=1020,height=80)
        
        self.Premium_row1_column1 = self.seat(self.premium_frame, 0, 0,   'P11')
        self.Premium_row1_column2 = self.seat(self.premium_frame, 0, 1,   'P12')
        self.Premium_row1_column3 = self.seat(self.premium_frame, 0, 2,   'P13')
        self.Premium_row1_column4 = self.seat(self.premium_frame, 0, 3,   'P14')
        self.Premium_row1_column5 = self.seat(self.premium_frame, 0, 4,   'P15')
        self.Premium_row1_column6 = self.seat(self.premium_frame, 0, 5,   'P16')
        self.Premium_row1_column7 = self.seat(self.premium_frame, 0, 6,   'P17')
        self.Premium_row1_column8 = self.seat(self.premium_frame, 0, 7,   'P18')
        self.Premium_row1_column9 = self.seat(self.premium_frame, 0, 8,   'P19')
        self.Premium_row1_column10 = self.seat(self.premium_frame, 0, 9,  'P110')
        self.Premium_row1_column11 = self.seat(self.premium_frame, 0, 10, 'P111')
        self.Premium_row1_column12 = self.seat(self.premium_frame, 0, 11, 'P112')
        self.Premium_row1_column13 = self.seat(self.premium_frame, 0, 12, 'P113')
        self.Premium_row1_column14 = self.seat(self.premium_frame, 0, 13, 'P114')
        self.Premium_row1_column15 = self.seat(self.premium_frame, 0, 14, 'P115')
        self.Premium_row1_column16 = self.seat(self.premium_frame, 0, 15, 'P116')
        self.Premium_row1_column17 = self.seat(self.premium_frame, 0, 16, 'P117')
        self.Premium_row1_column18 = self.seat(self.premium_frame, 0, 17, 'P118')
        self.Premium_row1_column19 = self.seat(self.premium_frame, 0, 18, 'P119')
            
    def seat(self,master,row,column,text):

        self.master = master
        self.text = text
        self.row = row
        self.column = column
        
        return tk.Button(self.master,text=self.text,command=None).grid(row=self.row,column=self.column,pady=8)
        
        
