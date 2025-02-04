from doctest import master
from tkinter import *
import tkinter.messagebox
import datetime
import os
import webbrowser

def manager():
    man=Toplevel(root)
    man.title("Hey! Welcome Manager")
    man.geometry('1920x1380')
    man.config(bg="white")

    headfont = ("Times New Roman ", 25, "bold")
    head = Label(man, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    title=("Times New Roman",21,"bold")
    tit=Label(man,text="Please Select some action",fg="blue",bg="white")
    tit.config(font=title)
    tit.pack()
    tit.place(x=535, y=100)

    button1 = Button(man, text="View Menu", bg='white', fg='blue',width=22, height=3,command=menu)
    button2 = Button(man,text="Get The Bill",bg="white" , fg='blue',width=22,height=3,command=bill)
    button3 = Button(man, text="Exit", bg='white',fg='red', width=22, height=3,command=man.destroy)

    m.place(x=0, y=0)

    button1.pack(side=TOP)
    button1.place(x=605, y=245)
    button2.pack(side=TOP)
    button2.place(x=605, y=345)
    button3.pack(side=TOP)
    button3.place(x=605, y=445)

    man.mainloop()

def bill():
    global b
    b=Toplevel(root)
    b.title("Bill Details")
    b.geometry('1920x1280')
    b.config(bg="white")

    head=("Times New Roman",25,"bold")

    la=Label(b,text="Bangalore Delicacy",bg="black",fg="white",width="512",height="2")
    la.config(font=headfont)
    la.pack()

    global tn
    tn=StringVar()

    name = ('Times New Roman', 15, 'bold')

    la=Label(b,text="Enter Table Number to get the Bill",fg='blue' ,bg="white")
    la.config(font=head)
    la.pack()

    n=Label(b,text="\n",bg="white")
    n.pack()

    dishn1_ent = Entry(b, textvariable=tn)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    n=Label(b,text="\n",bg="white")
    n.pack()

    bu = Button(b, text="Check",fg='blue', width=15, height=2,command=checkbill)
    bu.config(bg="white")
    bu.pack()

    back = Button(b, text="Exit", fg='red', width=22, height=2, command=b.destroy)
    back.config(bg='white')
    back.pack(side=LEFT)
    back.place(x=600, y=320)

    n=Label(b,text="\n",bg="white")
    n.pack()

def checkbill():
    t=tn.get()
    t=t+".txt"
    try:
        f1=open(t,"r")
    except:
        tkinter.messagebox.showinfo('Table is Not Booked!', 'Table number you entered is invalid')
        return
        f1.close()
    cb=Toplevel(root)
    cb.title('Bill Details')
    cb.geometry('1920x1380')
    
    headfont=("Times New Roman",35,"bold")
    
    la=Label(cb,text="Bangalore Delicacy",fg="white",bg="black",width="512",height="2")
    la.config(font=headfont)
    la.pack()
    
    f1=open("normaldish.txt","r")
    f2=open("special.txt","r")
    st=f1.read()+f2.read()
    li=st.split("$")
    del li[-1]
    bill=0
    f1.close()
    f2.close()
    f1=f1=open(t,"r")
    st1=f1.read()
    li2=st1.split("$")
    del li2[-1]
    for l in li2:
        l1=l.split("x")
        for l2 in li:
            if(l2.startswith(l1[0])):
                l3=l2.split("|")
                l5=l3[1]
                q=l3[2]
                d=l1[0]+'\t'+l5+'\t'+l1[1]+'\t'+q
                o=Label(cb,text=d)
                o.pack()
                bill+=int(l1[1])*int(q)
                break
            else:
                continue
    bi="Grand Total is :"+ str(bill)
    b=Label(cb,text=bi)
    b.config(font=headfont)
    b.pack()
    f1.close()
    
    
    
    g=Label(cb,text="\n")
    g.pack()
    
    bu = Button(cb, text="Payment Done",fg='blue', width=15, height=2,command=paymentdone)
    bu.config(bg="white")
    bu.pack()
    
    return  
    
def paymentdone():
    t=tn.get()
    f=open("customer.txt","r")
    fu=f.read()
    li=fu.split('$')
    li2=list()
    for l in li:
        if(l.startswith(t)):
            continue
        else:
            li2.append(l)
    f.close()
    del li2[-1]
    up='$'.join(li2)
    f=open("customer.txt","w")
    f.write(up)
    f.write('$')
    f.close()
    f=open("freetable.txt","a")
    w=t+'$'
    f.write(w)
    f.close()
    m=t+".txt"
    os.remove(m)
    tkinter.messagebox.showinfo('Transaction Completed!','All Record/s With this customer is/are deleted after getting the bill ammount')
    return
    
    
        
def chef():
    che=Toplevel(root)
    che.title("Welcome Chef")
    che.geometry('1920x1380')
    che.config(bg="white")

    headfont=("Times New Roman",30,"bold")
    la=Label(che,text="Bangalore Delicacy",bg="black",fg="white",width="512",height="2")
    la.config(font=headfont)
    la.pack()

    title = ("Times New Roman", 21, "bold")
    tit = Label(che, text="Please Select some action", fg="green", bg="white")
    tit.config(font=title)
    tit.pack()
    tit.place(x=535, y=100)

    button1 = Button(che, text="Add Dish", bg='white', fg='green',width=22, height=3,command=adddish)
    button2 = Button(che, text="Update Dish",bg="white" , fg='green',width=22,height=3,command=update)
    button3 = Button(che, text="Delete Dish", bg='white', fg='green',width=22, height=3,command=delete)
    button4 = Button(che, text="View Order", bg='white', fg='green',width=22, height=3,command=vieworder)
    button5 = Button(che, text="View Menu", bg='white', fg='green', width=22, height=3, command=menu)


    m.place(x=0, y=0)

    button1.pack(side=TOP)
    button1.place(x=605, y=200)
    button2.pack(side=TOP)
    button2.place(x=605, y=300)
    button3.pack(side=TOP)
    button3.place(x=605, y=400)
    button4.pack(side=TOP)
    button4.place(x=605, y=500)
    button5.pack(side=TOP)
    button5.place(x=605, y=600)

def adddish():
    ad=Toplevel(root)
    ad.geometry('1920x1380')
    ad.title('Add Dish')
    headfont=("Times New Roman",35,"bold")

    head=Label(ad,text="Bangalore Delicacy",bg="black",fg="white",width="512",height="2")
    head.config(font=headfont)
    head.pack()

    space = Label(ad, text="\n")
    space.pack()

    global ty
    global dish
    global dishp
    global dishn

    ty=StringVar()
    dish=StringVar()
    dishn=StringVar()
    dishp = IntVar()

    name = ('Times New Roman', 15)

    ty = StringVar(ad)
    ty .set("Type Of Dish")  # default value

    w = OptionMenu(ad, ty, "normal", "special")
    w.pack()

    space = Label(ad, text="\n")
    space.pack()

    dishn1 = Label(ad, text="Dish Number")
    dishn1.config(font=name)
    dishn1.pack()

    dishn1_ent = Entry(ad, textvariable=dishn)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    space = Label(ad, text="\n")
    space.pack()

    dish1 = Label(ad, text="Dish Name :")
    dish1.config(font=name)
    dish1.pack()

    dish1_ent = Entry(ad, textvariable=dish)
    dish1_ent.config(font=name)
    dish1_ent.pack()

    space = Label(ad, text="\n")
    space.pack()

    dishp1 = Label(ad, text="Dish Price :")
    dishp1.config(font=name)
    dishp1.pack()

    dishp1_ent = Entry(ad, textvariable=dishp)
    dishp1_ent.config(font=name)
    dishp1_ent.pack()

    space = Label(ad, text="\n")
    space.pack()

    bu = Button(ad, text="Add",fg='green', width=15, height=2,command=adddback)
    bu.config(bg="white")
    bu.pack()

    back = Button(ad, text="Exit", width=22, height=2, command=ad.destroy)
    back.config(bg='white', fg='red')
    back.pack(side=LEFT)
    back.place(x=605, y=550)

    ad.mainloop()

def adddback():
    t=ty.get()
    dn=dish.get()
    dp=dishp.get()
    dnu=dishn.get()
    if(t=="normal"):
        f=open("normaldish.txt","a")
    else:
        f=open("special.txt","a")
    st = dnu + '|' + dn + '|' +str(dp)+ '$'
    tkinter.messagebox.showinfo('Dish Added!','Dish Added Successfully into Menu Card')
    f.write(st)
    f.close()

def update():
    up = Toplevel(root)
    up.geometry('1920x1380')
    up.title('ADD DISH')
    headfont = ("Times New Roman", 35, "bold")

    head = Label(up, text="Bangalore Delicacy",bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    noo=("Times New Roman",15,"bold")

    space = Label(up, text="\n")
    space.pack()

    space = Label(up, text="\n")
    space.pack()

    no=Label(up,text="***Notice*** If You Don't Want to change Some Fields Write Old Entry Value As it is")
    no.config(fg="red")
    no.config(font=noo)
    no.pack()

    space = Label(up, text="\n")
    space.pack()

    global ty
    global dish
    global dishp
    global dishn

    ty = StringVar()
    dish = StringVar()
    dishn = StringVar()
    dishp = StringVar()

    name = ('Times New Roman', 15, 'bold')

    ty = StringVar(up)
    ty .set("Type Of Dish")  # default value

    w = OptionMenu(up, ty, "normal", "special")
    w.pack()

    space = Label(up, text="\n")
    space.pack()

    dishn1 = Label(up, text="Dish Number  :")
    dishn1.config(font=name)
    dishn1.pack()

    dishn1_ent = Entry(up, textvariable=dishn)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    space = Label(up, text="\n")
    space.pack()

    dish1 = Label(up, text="New Dish Name :")
    dish1.config(font=name)
    dish1.pack()

    dish1_ent = Entry(up, textvariable=dish)
    dish1_ent.config(font=name)
    dish1_ent.pack()

    space = Label(up, text="\n")
    space.pack()

    dishp1 = Label(up, text="New Dish Price :")
    dishp1.config(font=name)
    dishp1.pack()

    dishp1_ent = Entry(up, textvariable=dishp)
    dishp1_ent.config(font=name)
    dishp1_ent.pack()

    space = Label(up, text="\n")
    space.pack()

    bu = Button(up, text="Update", fg='green', width=15, height=2, command=updback)
    bu.config(bg="white")
    bu.pack()

    back = Button(up, text="Exit",fg='red', width=22, height=2, command=up.destroy)
    back.config(bg='white')
    back.pack(side=LEFT)
    back.place(x=600, y=650)

    up.mainloop()


def updback():
    t = ty.get()
    dn = dish.get()
    dp = dishp.get()
    dnu = dishn.get()
    if(t == "normal"):
        f = open("normaldish.txt", "r")
        n = "normaldish.txt"
    else:
        f = open("special.txt", "r")
        n = "special.txt"
    flag=0
    fu=f.read()
    li=fu.split('$')
    l2=list()
    for l in li:
        if (l.startswith(dnu)):
            st = dnu + '|' + dn + '|' + dp + '$'
            flag=1
        else:
            l2.append(l)

    if(flag==1):
        tkinter.messagebox.showinfo('Dish Updated!', 'Dish Updated Successfully in Menu Card')
        f.close()
        f = open(n, "w")
        del l2[-1]
        l2.append(st)
        up = '$'.join(l2)
        f.write(up)
        f.close()
    else:
        f.close()
        tkinter.messagebox.showerror('Dish Not Found!', 'Dish Not Found in  Menu Card')

def delete():
    de = Toplevel(root)
    de.geometry('1920x1380')
    de.title('ADD DISH')
    headfont = ("Times New Roman", 35, "bold")

    head = Label(de, text="Bangalore Delicacy",bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    space = Label(de, text="\n")
    space.pack()

    space = Label(de, text="\n")
    space.pack()

    space = Label(de, text="\n")
    space.pack()

    global ty
    global dishn

    ty = StringVar()
    dishn = StringVar()

    name = ('Times New Roman', 15, 'bold')

    ty = StringVar(de)
    ty .set("Type Of Dish")  # default value

    w = OptionMenu(de, ty, "normal", "special")
    w.pack()

    space = Label(de, text="\n")
    space.pack()

    dishn1 = Label(de, text="Dish Number  :")
    dishn1.config(font=name)
    dishn1.pack()

    dishn1_ent = Entry(de, textvariable=dishn)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    space = Label(de, text="\n")
    space.pack()

    bu = Button(de, text="Delete", fg='red',width=15, height=2, command=delback)
    bu.config(bg="white")
    bu.pack()

    back = Button(de, text="Exit",fg='red', width=22, height=2, command=de.destroy)
    back.config(bg='white')
    back.pack(side=LEFT)
    back.place(x=600, y=430)

    de.mainloop()

def delback():
    t = ty.get()
    dnu = dishn.get()
    if(t == "normal"):
        f = open("normaldish.txt", "r")
        n = "normaldish.txt"
    else:
        f = open("special.txt", "r")
        n = "special.txt"
    flag=0
    fu=f.read()
    li=fu.split('$')
    l2=list()
    for l in li:
        if (l.startswith(dnu)):
            flag=1
        else:
            l2.append(l)

    if(flag==1):
        tkinter.messagebox.showinfo('Dish Deleted!', 'Dish Deleted Successfully in Menu Card')
        f.close()
        f = open(n, "w")
        up = '$'.join(l2)
        f.write(up)
        f.close()
    else:
        f.close()
        tkinter.messagebox.showerror('Dish Not Found!', 'Dish Not Found in  Menu Card')

def vieworder():
    global vo
    vo=Toplevel(root)
    vo.title('view Order')
    vo.geometry('1920x1380')
    vo.config(bg="white")

    headfont = ("Times New Roman", 35, "bold")
    head = Label(vo, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    name = ('Times New Roman', 15, 'bold')

    title = ("Times New Roman", 20, "bold")

    global tablen
    tablen=StringVar()

    f=open("customer.txt","r")
    l1=list()
    fu=f.read()
    li=fu.split('$')
    i=1
    for l in li:
        li2=l.split('|')
        l1.append(li2[0])
    f.close()
    stri=','.join(l1)
    free="Booked Tables are : " + stri

    li=Label(vo,text=free)
    li.config(bg="white",font=title)
    li.pack()

    space = Label(vo, text="\n",bg="white")
    space.pack()

    dishn1 = Label(vo, text="Enter A Table Number :")
    dishn1.config(font=name,bg="white")
    dishn1.pack()

    dishn1_ent = Entry(vo, textvariable=tablen)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    space = Label(vo, text="\n",bg="white")
    space.pack()

    bu = Button(vo, text="Check",fg='green', width=15, height=2,command=voback)
    bu.config(bg="white")
    bu.pack()

def voback():
    z=open("normaldish.txt","r")
    y=open("special.txt","r")
    h=z.read()+y.read()
    z.close()
    y.close()
    h1=h.split('$')
    del h1[-1]
    t=tablen.get()
    n=t+".txt"
    try:
        f=open(n,"r+")
    except:
        tkinter.messagebox.showerror('Table is Not Booked!', 'Table Number you entered is invalid')
        return
    
    fu=f.read()
    li=fu.split('$')
    del li[-1]
    lo=Label(vo,text="\n",bg="white")
    lo.pack()
    for l in li:
        li2=l.split('x')
        for h2 in h1:
            if(h2.startswith(li2[0])):
                h3=h2.split('|')
                li=h3[1]
                break
                
        st="Item Name:"+li+"\t\t"+"Quantity:"+li2[1]
        lo1=Label(vo,text=st,bg="white")
        lo1.pack()
    f.close()


def customer():
    cu=Toplevel(root)
    cu.title('Welcome Sir/Madam to Bangalore Delicacy')
    cu.config(bg="white")
    cu.geometry('1920x1380')

    headfont = ("Times New Roman", 35, "bold")
    head = Label(cu, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    title = ("Times New Roman", 25, "bold")
    tit = Label(cu, text="Please Select some action", fg="orange", bg="white")
    tit.config(font=title)
    tit.pack()
    tit.place(x=500, y=150)

    button1 = Button(cu, text="Book a Table and Order", bg='white', fg='orange',width=22, height=3,command=bto)
    button2 = Button(cu,text="Order from Table",bg="white" , fg="orange",width=22,height=3,command=orderfromtable)
    button3 = Button(cu, text="Exit", bg='white',fg='red', width=22, height=3,command=cu.destroy)

    m.place(x=0, y=0)
    button1.pack(side=TOP)
    button1.place(x=605, y=300)
    button2.pack(side=TOP)
    button2.place(x=605, y=400)
    button3.pack(side=TOP)
    button3.place(x=605, y=500)

    cu.mainloop()

def bto():
    bt=Toplevel(root)
    bt.title('Book A Table and Add')
    bt.geometry('1920x1380')
    bt.config(bg="white")

    name = ('Times New Roman', 15, 'bold')

    headfont = ("Times New Roman", 35, "bold")
    head = Label(bt, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    global tablen
    tablen=StringVar()

    space = Label(bt, text="\n",bg="white")
    space.pack()

    title=("Times New Roman",25,"bold")
    tit=Label(bt,text="Please Select an Table: 1-20",fg="black",bg="white")
    tit.config(font=title)
    tit.pack()

    space = Label(bt, text="\n",bg="white")
    space.pack()

    space = Label(bt, text="\n",bg="white")
    space.pack()

    dishn1 = Label(bt, text="Enter A Table Number :")
    dishn1.config(font=name,bg="white")
    dishn1.pack()

    dishn1_ent = Entry(bt, textvariable=tablen)
    dishn1_ent.config(font=name)
    dishn1_ent.pack()

    space = Label(bt, text="\n",bg="white")
    space.pack()


    space = Label(bt, text="\n",bg="white")
    space.pack()

    bu = Button(bt, text="Check",fg='orange', width=22, height=2,command=btoback)
    bu.config(bg="white")
    bu.pack()

def btoback():
    flag=0
    n=tablen.get()
    f=open("freetable.txt","r")
    fu=f.read()
    li=fu.split('$')
    for l in li:
        if(l==n):
            flag=1
            tkinter.messagebox.showinfo('Table Available','Entered Table is available')
            bto2()

    if(flag!=1):
        tkinter.messagebox.showerror('Ohh! Sorry','Entered Table is not available')
        customer()

def bto2():
    bt2=Toplevel(root)
    bt2.title('Please Enter Your Details')
    bt2.geometry('1920x1380')
    bt2.config(bg="white")

    name = ('Times New Roman', 15, 'bold')

    global tb
    global nme
    global add
    global psw

    tb=StringVar()
    nme=StringVar()
    add=StringVar()
    psw=StringVar()

    headfont = ("Times New Roman", 35, "bold")
    head = Label(bt2, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    title=("Times New Roman",20,"bold")
    tit=Label(bt2,text="Please Fill Your Details",fg="black",bg="white")
    tit.config(font=title,bg="white")
    tit.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    dishn1 = Label(bt2, text="Table Number :")
    dishn1.config(font=name,bg="white")
    dishn1.pack()

    dishn1_ent = Entry(bt2, textvariable=tb)
    dishn1_ent.config(font=name,bg="white")
    dishn1_ent.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    dish1 = Label(bt2, text="Name :")
    dish1.config(font=name,bg="white")
    dish1.pack()

    dish1_ent = Entry(bt2, textvariable=nme)
    dish1_ent.config(font=name,bg="white")
    dish1_ent.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    dishp1 = Label(bt2, text="Address :")
    dishp1.config(font=name,bg="white")
    dishp1.pack()

    dishp1_ent = Entry(bt2, textvariable=add)
    dishp1_ent.config(font=name,bg="white")
    dishp1_ent.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    dishp2 = Label(bt2, text="Enter One Time Password :")
    dishp2.config(font=name,bg="white")
    dishp2.pack()

    dishp2_ent = Entry(bt2, textvariable=psw,show='*')
    dishp2_ent.config(font=name,bg="white")
    dishp2_ent.pack()

    space = Label(bt2, text="\n",bg="white")
    space.pack()

    bu = Button(bt2, text="Book & Order",fg='orange', width=15, height=2,command=bto2back)
    bu.config(bg="white")
    bu.pack()

    back = Button(bt2, text="Exit",fg='red', width=22, height=2, command=bt2.destroy)
    back.config(bg='white')
    back.pack(side=LEFT)
    back.place(x=600, y=640)

def bto2back():
    t=tb.get()
    p=psw.get()
    n=nme.get()
    a=add.get()

    st = t + '|' + p + '|' + n  + '|' + a + '$'
    

    f=open("customer.txt","a")
    f.write(st)
    tkinter.messagebox.showinfo('Added Successfully!','Your Details are Saved Successfully into our database')
    f.close()

    f=open("freetable.txt","r")
    fu=f.read()
    li=fu.split('$')
    li2=list()
    for l in li:
        if(t==l):
            continue
        else:
            li2.append(l)
    s='$'.join(li2)
    f.close()
    f=open("freetable.txt","w")
    f.write(s)
    f.close()

def orderfromtable():
    oft=Toplevel(root)
    oft.geometry('1920x1380')
    oft.title('Order From Table')
    oft.config(bg="white")

    name = ('Times New Roman', 15, 'bold')

    global tb
    global dc
    global qt
    global psw

    tb=StringVar()
    dc=StringVar()
    qt=IntVar()
    psw=StringVar()

    headfont = ("Times New Roman", 35, "bold")
    head = Label(oft, text="Bangalore Delicacy", bg="black", fg="white", width="512", height="2")
    head.config(font=headfont)
    head.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    back = Button(oft, text="Menu", bg='white', fg='black', width=20, height=3,command=menu)
    back.config(bg='orange', fg='white')
    back.pack(side=RIGHT)
    back.place(x=1390, y=116)

    title=("Times New Roman",20,"bold")
    tit=Label(oft,text="Please Fill Your Details",fg="black",bg="white")
    tit.config(font=title,bg="white")
    tit.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    dishn1 = Label(oft, text="Table Number :")
    dishn1.config(font=name,bg="white")
    dishn1.pack()

    dishn1_ent = Entry(oft, textvariable=tb)
    dishn1_ent.config(font=name,bg="white")
    dishn1_ent.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    dish1 = Label(oft, text="Dish Code:")
    dish1.config(font=name,bg="white")
    dish1.pack()

    dish1_ent = Entry(oft, textvariable=dc)
    dish1_ent.config(font=name,bg="white")
    dish1_ent.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    dishp1 = Label(oft, text="Quantity :")
    dishp1.config(font=name,bg="white")
    dishp1.pack()

    dishp1_ent = Entry(oft, textvariable=qt)
    dishp1_ent.config(font=name,bg="white")
    dishp1_ent.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    dishp2 = Label(oft, text="Enter One Time Password :")
    dishp2.config(font=name,bg="white")
    dishp2.pack()

    dishp2_ent = Entry(oft, textvariable=psw,show='*')
    dishp2_ent.config(font=name,bg="white")
    dishp2_ent.pack()

    space = Label(oft, text="\n",bg="white")
    space.pack()

    bu = Button(oft, text="Order",fg='orange', width=15, height=2,command=oftback)
    bu.config(bg="white" )
    bu.pack()

    back = Button(oft, text="Exit",fg='red', width=22, height=2, command=oft.destroy)
    back.config(bg='white')
    back.pack(side=LEFT)
    back.place(x=605, y=640)

def oftback():
    t=tb.get()
    d=dc.get()
    q=qt.get()
    p=psw.get()
    flag=0
    f=open("customer.txt","r")
    fu=f.read()
    li=fu.split('$')
    li1=list()
    for l in li:
        if(l.startswith(t)):
            li1=l.split('|')
            if(p==li1[1]):
                flag=1
    f.close()
    flag1=0
    f1=open("normaldish.txt","r")
    f2=open("special.txt","r")
    u=f1.read()+f2.read()
    j=u.split('$')
    for g in j:
        if(g.startswith(d)):
            flag1=1
        else:
            continue
        
    
    f1.close()
    f2.close()
    
    if(flag==1 and flag1==1):
        tkinter.messagebox.showinfo('Order Placed','PLease wait...Your Order is On its Way')
        t=t+".txt"
        f=open(t,"a")
        z=d+'x'+str(q)+'$'
        f.write(z)
        f.close()
    else:
        tkinter.messagebox.showerror('Invalid Dish Code or Password','Sorry!!!! Invalid Password or Dish Code')

def menu():
    webbrowser.open_new('http://localhost/FS/menu.php')


root=Tk()
root.title('Bangalore Delicacy')
root.geometry("1980x1280")
root.config(bg="white")
headfont=("Times New Roman",35,"bold")

head=Label(root,text="Bangalore Delicacy",bg="black",fg="white",width="512",height="2")
head.config(font=headfont)
head.pack()

title_frame = Frame(root, bg='snow', width=600, height=300)

m = Label(title_frame, width=600, height=300)


#creating login buttons

button1 = Button(root, text="Manager", bg='white', fg='blue',width=22, height=3,command=manager)
button2 = Button(root, text="Chef", bg='white',fg='green', width=22, height=3,command=chef)
button3 = Button(root, text="Customer", bg='white',fg='orange', width=22, height=3,command=customer)
button4 = Button(root, text="Exit", bg='white',fg='red', width=22, height=3,command=root.destroy)

m.place(x=0, y=0)

button1.pack(side=TOP)
button1.place(x=605, y=200)
button2.pack(side=TOP)
button2.place(x=605, y=300)
button3.pack(side=TOP)
button3.place(x=605, y=400)
button4.pack(side=TOP)
button4.place(x=605, y=500)


root.mainloop()
