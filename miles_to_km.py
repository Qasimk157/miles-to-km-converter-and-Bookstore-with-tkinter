from tkinter import *

def miles_to_km():
    km=float(e1_value.get())*1.60934
    t1.insert(END,km)
window=Tk()
b1=Button(window,text="miles_to_km",command=miles_to_km)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)



def km_to_miles():
    miles=float(e2_value.get())*0.62137
    t2.insert(END,miles)
b2=Button(window,text="km_to miles",command=km_to_miles)
b2.grid(row=1,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)




window.mainloop()
