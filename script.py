import tkinter as tkr
app=tkr.Tk(__name__)
app.title('My Calculator')
app.geometry('500x500')
tkr.Label(app,text='Enter first number').place(x=10,y=10)
tkr.Label(app,text='Enter second number').place(x=320,y=10)
tkr.Label(app,text='Result').place(x=150,y=200)

v1=tkr.Variable(app)
v2=tkr.Variable(app)
t=tkr.Variable(app)
tkr.Entry(app,textvariable=v1).place(x=10,y=40)
tkr.Entry(app,textvariable=v2).place(x=320,y=40)
tkr.Label(app,textvariable=t).place(x=200,y=200)

def func1():
    print(int(v1.get())+int(v2.get()))
    t.set(int(v1.get())+int(v2.get()))
def func2():
    print(int(v1.get())-int(v2.get()))
    t.set(int(v1.get())-int(v2.get()))
def func3():
    print(int(v1.get())*int(v2.get()))
    t.set(int(v1.get())*int(v2.get()))
def func4():
    print(float(v1.get())/float(v2.get()))
    t.set(float(v1.get())/float(v2.get()))
    

tkr.Button(app,text='+',command=func1,bg='red').place(x=150,y=100)
tkr.Button(app,text='-',command=func2,bg='red').place(x=190,y=100)
tkr.Button(app,text='*',command=func3,bg='red').place(x=240,y=100)
tkr.Button(app,text='/',command=func4,bg='red').place(x=290,y=100)



app.mainloop()
