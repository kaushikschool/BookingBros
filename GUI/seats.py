from tkinter import *  

app = Tk() 
app.geometry('880x400')
app.resizable(False,False)




a11 = Checkbutton(app, text='a11').grid(row=0,column=0)
a12 = Checkbutton(app,text='a12').grid(row=0,column=1)
a13 = Checkbutton(app,text='a13').grid(row=0,column=2)
a14 = Checkbutton(app,text='a14').grid(row=0,column=3)
emptys01 = Label(app,text='\t').grid(row=0,column=4)
a15 = Checkbutton(app,text='a15').grid(row=0,column=5)
a16 = Checkbutton(app,text='a16').grid(row=0,column=6)
a17 = Checkbutton(app,text='a17').grid(row=0,column=7)
a18 = Checkbutton(app,text='a18').grid(row=0,column=8)
a19 = Checkbutton(app,text='a15').grid(row=0,column=9)
emptys02 = Label(app,text='\t').grid(row=0,column=10)
a110 = Checkbutton(app,text='a110').grid(row=0,column=11)
a111 = Checkbutton(app,text='a111').grid(row=0,column=12)
a112 = Checkbutton(app,text='a112').grid(row=0,column=13)
a113 = Checkbutton(app,text='a113').grid(row=0,column=14)
a114 = Checkbutton(app,text='a114').grid(row=0,column=15)

app.mainloop()