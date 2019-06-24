from tkinter import *
import csv
from sklearn import tree
x=[]
y=[]
count=0
a = open("a.csv","r")
new = a.readline()
new = a.readline()
while new!='':
    data=new.split(",")
    y.append(data[-1][:-1])
    z=[(int(data[1])),(int(data[2])),(int(data[3])),(int(data[4])),(int(data[5])),(int(data[6]))]
    x.append(z)
    new = a.readline()
a.close()
#print(x,y)

def viewdata():
    top=Toplevel()
    top.title("Group Information")
    top.geometry('500x500')
    canvas=Canvas(width=500,height=500,bg='lightblue')
    canvas.pack()
    photo2=PhotoImage(file="G://project//student//review//pic.png")
    canvas.create_image(0,0,image=photo2,anchor=NW)
    label=Label(top,text='Design of Classification Model for Placement Prediction',width=40,bg="light blue",font=("bold",10))
    label.pack()
    label4=Label(top,text='Guide',width=20,bg="light blue",font=("bold",10))
    label4.place(x=50,y=100)
    label5=Label(top,text='Shri. V. P. Mahatme',width=20,bg="light blue",font=("bold",10))
    label5.place(x=250,y=100)
    label6=Label(top,text='Projectees',width=20,bg="light blue",font=("bold",10))
    label6.place(x=50,y=200)
    label7=Label(top,text='Ritish Nedunoori  CT15121',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=200)
    label7=Label(top,text='Sahil Siddiqui  CT15029',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=220)
    label7=Label(top,text='Himanshi Sharma  CT15065',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=240)
    label7=Label(top,text='Sanika Jangle  CT15019',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=260)

def printClasses():
    global x,y
    txt.delete(0.0,'end')
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(x,y)
    h=e1.get()          #h contains the aggregate 
    r=e2.get()          #r contains the roll number
    w=var.get()         #w is the backlogs
    t=e3.get()          #t is 10th agg
    i=e4.get()          #i is 12th agg
    s=e5.get()          #s is workshops
    l=e6.get()          #l is languages
    #print(h)
    #print(r)
    #print(w)
    if r=='' or h=='' or w=='' or t=='' or i=='' or s=='' or l=='':
        txt.insert(0.0,"Please fill data")

    elif len(r)==7 or len(r)==8:
        if len(h)<3 and int(h)>50:
            prediction = clf.predict([[h,w,t,i,s,l]])
            if prediction=='':
                txt.insert(0.0,'you are not eligible')
            else:
                z=e2.get()
                print(z + " is eligible for ",prediction)
                txt.insert(0.0,prediction)
            
                entry=str(z)+","+str(h)+","+str(t)+","+str(i)+","+str(s)+","+str(l)+","+prediction[0]+"\n"
                fp.write(entry)
        elif len(h)<3 and int(h)<50:
            txt.insert(0.0,'Not Eligible')
        else:
            txt.insert(0.0,'Enter correct data')
    else:
        txt.insert(0.0,'Enter correct data')
           
file= open("count.txt","r")
count = int(file.readline())
file.close()
file=open("count.txt","w")
file.write("0")
file.close()
#print(count)
fp=open('b.csv','a')
if count>0:
    fp.write("Roll no.,Aggregate,Company\n")        
#GUI part
    
main=Tk()

main.geometry('1500x1500')
canvas=Canvas(width=1500,height=1800,bg='lightblue')
canvas.pack()

photo=PhotoImage(file="G://project//student//review//pic.png")
photo1=PhotoImage(file="G://project//student//review//k.png")

canvas.create_image(0,-100,image=photo,anchor=NW)
canvas.create_image(600,200,image=photo1,anchor=NW)

#canvas2.create_image(200,300,image=img,anchor=NW)
main.title('Training and Placement cell')
label0=Label(main,text='STUDENT DATABASE',bg="light blue",fg="black",width=20,font=("bold",25))
label0.place(x=475,y=70)
l3=Label(main,text='ROLL NUMBER',width=20,bg="light blue",font=("bold",10))
l3.place(x=100,y=110)
e2=Entry(main)
e2.place(x=300,y=110)
label1=Label(main,text=' AGGREGATE',width=20,bg="light blue",font=("bold",10))
label1.place(x=100,y=150)
label2=Label(main,text=' BACKLOGS',width=20,bg="light blue",font=("bold",10))
label2.place(x=100,y=190)

label3=Label(main,text="Kavikulguru Institute of Technology and Science Ramtek"
             "\n Department of Computer Technology",bg="light blue",fg="black",width=50,font=("bold",15))
label3.place(x=400,y=10)

label8=Label(main,text=' 10th agg',width=20,bg="light blue",font=("bold",10))
label8.place(x=100,y=230)

label9=Label(main,text=' 12th agg',width=20,bg="light blue",font=("bold",10))
label9.place(x=100,y=270)

label10=Label(main,text=' Workshops',width=20,bg="light blue",font=("bold",10))
label10.place(x=100,y=310)

label11=Label(main,text=' Programming Languages',width=20,bg="light blue",font=("bold",10))
label11.place(x=100,y=350)

e1=Entry(main)
e1.place(x=300,y=150)
var=IntVar()

e3=Entry(main)
e3.place(x=300,y=230)

e4=Entry(main)
e4.place(x=300,y=270)

e5=Entry(main)
e5.place(x=300,y=310)

e6=Entry(main)
e6.place(x=300,y=350)

rb1=Radiobutton(main,text='0',variable=var,value=0)
rb2=Radiobutton(main,text='1',variable=var,value=1)

rb1.place(x=300,y=190)

rb2.place(x=350,y=190)
b1=Button(main,text='Submit',bg="light blue",fg="black",command=printClasses)
b1.place(x=300,y=390)
b2=Button(main,text='Project Information',bg="light blue",fg="black",command=viewdata)
b2.place(x=300,y=660)
txt=Text(main,width=15,height=5,bg="light yellow",wrap=WORD)
txt.place(x=300,y=430)
#button1.pack()
main.mainloop()

fp.close()

