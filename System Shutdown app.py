from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')

def reButton():
    os.system('shutdown /r /t 20')

def lout():
    os.system('shutdown -l')

def shut():
    os.system('shutdown /s /t 1')

st=Tk()
st.geometry('500x500')
st.config(bg='black')
st.title("ShutDown App")

r_button=Button(st,text='Restart',font=('New Time Roman',25,'bold'),relief=RAISED,cursor='plus',command=restart)
r_button.place(x=150,y=50,height=60,width=200)

rt_button=Button(st,text='Restart Time',font=('New Time Roman',25,'bold'),relief=RAISED,cursor="plus",command=reButton)
rt_button.place(x=150,y=150,height=60,width=200)

lout_button=Button(st,text='Log Out',font=('New Time Roman',25,'bold'),relief=RAISED,cursor='plus',command=lout)
lout_button.place(x=150,y=250,height=60,width=200)

sout_button=Button(st,text='Shut Down',font=('New Time Roman',25,'bold'),relief=RAISED,cursor='plus',command=shut)
sout_button.place(x=150,y=350,height=60,width=200)

st.mainloop()

