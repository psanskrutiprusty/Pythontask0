
import sqlite3 as s

from tkinter import *
import tkinter.messagebox as m

from tkinter import simpledialog
w=Tk()

d=0
ae=0
de=0
cg=0.0





abc=s.connect("D:/j.db")
a=abc.cursor()
a.execute("create table if not exists student(name char(30),branch char(50),regd_id int,dsp_marks int,aec_marks int,dec_marks int)")
def database():
    name=t1.get()
    branch=t2.get()
    reg_id=int(t3.get())
    dsp=d
    aec=ae
    dec=de
    a.execute("insert into student values('%s','%s',%d,%d,%d,%d)"%(name,branch,reg_id,dsp,aec,dec))
    abc.commit()
    m.showinfo(title="submit data",message="record submitted successfully")





v1=StringVar()
v2=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()

def cgpa():
    total=d+ae+de
    p=(total/300)*100
    global cg
    cg=p/9.5
    m.showinfo(title="result",message="your cgpa is "+str(cg))


def grade():
    if( cg>=9.0):
         m.showinfo(title="grade",message="your grade is O")
    elif (cg >=8.0):
         m.showinfo(title="grade",message="your grade is A")
    elif (cg>=7.0):
        m.showinfo(title="grade",message="your grade is B")
    elif(cg>=6.0):
        m.showinfo(title="grade",message="your grade is C")
    else:
        m.showinfo(title="grade",message="your grade is D")
  


def inp():
    a=open_window()
    
         
    

    
      



def calculate():
    database()
    
    top2=Toplevel()
    top2.title('GUI_3')
    top2.geometry('500x500')
    B1=Button(top2,text="CGPA",font=("aerial",20,"bold"),command=cgpa)
    B2=Button(top2,text="GRADE",font=("aerial",20,"bold"),command = grade)
    B3=Button(top2,text="NEW INPUT", font=("aerial",20,"bold"),command=inp)
    B4=Button(top2,text="CLOSE",font=("aerial",20,"bold"),command=w.destroy)
    
    B1.pack(anchor=CENTER)
    B2.pack()
    B3.pack()
    B4.pack()
 
    
def dsp():
    global d
    d=int(simpledialog.askstring("enter marks","input your marks in DSP"))
     
     
   
    
    
    
    
def aec():
     global ae
     ae=int(simpledialog.askstring("enter marks","input your marks in AEC"))
    
    
    
def dec():
    global de
    de=int(simpledialog.askstring("enter marks","input your marks in DEC"))
   
    
    




    

def window_2():
   
   
    top1=Toplevel()
    top1.title('GUI_2')
    top1.geometry('500x500')
    B1=Button(top1,text="DSP",font=("aerial",20,"bold"),command=dsp)
    B2=Button(top1,text="AEC",font=("aerial",20,"bold"),command=aec)
    B3=Button(top1,text="DEC",font=("aerial",20,"bold"),command=dec)
    B4=Button(top1,text="SUBMIT",font=("aerial",20,"bold"),command=calculate)
   
    B1.pack(anchor=CENTER)
    B2.pack()
    B3.pack()
    B4.pack()
    
    
    
    
    
    

def open_window():
    name=v1.get()
    password=v2.get()
    msg=''
    if(name=='' or password == ''):
        msg='inavalid name or password'
        m.showinfo(title="info",message=msg)
    else:
     
      top=Toplevel()
      top.title('GUI_1')
      top.geometry('500x500')
      L1=Label(top,font=("aerial",20,"bold"),text="NAME")
      L2=Label(top,font=("aerial",20,"bold"),text="BRANCH")
      L3=Label(top,font=("aerial",20,"bold"),text="REGISTRATION ID")
      E1=Entry(top,font=("arial",20,"bold"),textvariable=t1)
      E2=Entry(top,font=("arial",20,"bold"),textvariable=t2)
      E3=Entry(top,font=("arial",20,"bold"),textvariable=t3)
      B1=Button(top,text="SUBMIT",font=("aerial",20,"bold"),command=window_2)
      L1.grid(row=1,column=20)
      L2.grid(row=2,column=20)
      L3.grid(row=3,column=20)
      E1.grid(row=1,column=30)
      E2.grid(row=2,column=30)
      E3.grid(row=3,column=30)
      B1.grid(row=4,column=30)
      
      E1.delete(0,END)
      E2.delete(0,END)
      E3.delete(0,END)
      return 
         
          
    


      

    
    
    
    
    
    
    
    
    
   
w.geometry('1000x1000')     
      

L1=Label(w,text="STUDENT DATABASE",width=20,font=("bold",20))
L2=Label(w,text="USER_NAME",width=20,font=("bold",10))
L3=Label(w,text="PASSWORD",width=20,font=("bold",10))

E1=Entry(w,font=("arial",20,"bold"),textvariable=v1)
E2=Entry(w,font=("arial",20,"bold"),textvariable=v2)

B1=Button(w,text="SUBMIT",font=("aerial",20,"bold"),command=open_window)


    

w.title('GUI_0')

L1.place(x=90,y=53)
L2.place(x=80,y=130)
L3.place(x=80,y=180)
E1.place(x=240,y=130)
E2.place(x=240,y=180)
B1.place(x=180,y=380)


w.mainloop()


    
     
