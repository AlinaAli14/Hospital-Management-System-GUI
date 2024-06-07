                     # hospital menagment system.
# tkinter is using to grafical user interface (GUI).
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
def connect_to_database():
    global conn
    db_connection= mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="db_connection"
    )
    if db_connection.is_connected():
        print("Connected to the database")
    else:
        print("Failed to connect to the database")

cursor= db_connection.cursor()
cursor.execute("select*from hospitalpatient")
rows=cursor.fetchall()
for row in rows:
    print(row)
 
cursor.close()
db_connection.close()

win = Tk()# to farform tkinter 
win.state('zoomed')#click a  run button for open a full screen. 
win.config(bg='black')#usng congig are set in background color.

#-----------------button funcation-----------------------#
# get method are used in fatch an info.
################################################
def pdb():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error","all fields are required")
    else:
        # mysql.connector.connect(host,username,password,database)under for peramiter
        con = mysql.connector.connect(host='localhost',username='root',password='1234', database='db_connection')    
        #my courser
        my_cursor = con.cursor()
        # thier will using query in insert a table of connect sqldata base.
        my_cursor.execute("insert into alldata values(%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)",(
            PatientName.get(),
            DoctorID.get(),
            Room.get(),
            PateintId.get(),
            ParmanentAdress.get(),
            DOB.get(),
            Gender.get(),
            Issue.get(),
            Medicines.get(),
            DailyDose.get(),
            Phone.get(),
            Email.get(),
            LastVisit.get(),
            NextVisit.get(),
        ))
        con.commit()
        # fetch_data()
        con.close()
        messagebox.showinfo("success","Data has been inserted")
####################################################
########


#fatch data.
# def fetch_data():
#         con = mysql.connector.connect(host='localhost',username='root',password='4011', database='mysql1')    
# # #         #my courser
#         my_cursor = con.cursor()
# # #         # thier will using query in insert a table of connect sqldata base.
#         my_cursor.execute('select* from hospital')
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#           table.delete(* table.get_children())
#           for item in rows:
#               table.insert(' ',END,values=item)
#         con.commit()
#         con.close() 
########################################


#heading
#font using change a style and hight of font.
#bg using set background color.
#fg using set font color.
#pack method are using under multiple work 
#fill=x are work in horizantal diraction.
# there module are work in without verible  
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
###################################
#frame1
# bd are used for boder in Frame.
Frame1 = Frame(win,bd=15,relief=RIDGE)
Frame1.place(x=0,y=54,width=1537,height=400)
#frame patiant information.
lf1 = LabelFrame(Frame1,text='PATIENT INFORMATION',font='arial 10 bold',bd=10,bg='pink')
lf1.place(x=8,y=0,width=900,height=370)
#lable pationt information
#left
#name
Label(Frame1,text='Patient Name',bg='pink',font='arial 10 bold').place(x=30,y=25)
#Doctor ID
Label(Frame1,text='Doctor ID',bg='pink',font='arial 10 bold').place(x=30,y=70)
#dose
Label(Frame1,text='Room No.',bg='pink',font='arial 10 bold').place(x=30,y=115)
# No.of Tablets
Label(Frame1,text='Patient ID',bg='pink',font='arial 10 bold').place(x=30,y=160)
#Gender Date
Label(Frame1,text='Address',bg='pink',font='arial 10 bold').place(x=30,y=215)
#Expiry Date
Label(Frame1,text='DOB',bg='pink',font='arial 10 bold').place(x=30,y=265)
#Daly Dose
Label(Frame1,text='Gender',bg='pink',font='arial 10 bold').place(x=30,y=310)
#Side Effect
Label(Frame1,text='Issue',bg='pink',font='arial 10 bold').place(x=30,y=435)
#
#right
#blood preseure
Label(Frame1,text='Medicine',bg='pink',font='arial 10 bold').place(x=450,y=25)
#storege device
Label(Frame1,text='Daily Dose',bg='pink',font='arial 10 bold').place(x=450,y=70)
#medcation
Label(Frame1,text='Phone',bg='pink',font='arial 10 bold').place(x=450,y=115)
#patient id.
Label(Frame1,text='Email',bg='pink',font='arial 10 bold').place(x=450,y=160)
#patient Name.
# Label(Frame1,text='First visit',bg='pink',font='arial 10 bold').place(x=450,y=215)
#DOB
Label(Frame1,text='Last visit',bg='pink',font='arial 10 bold').place(x=450,y=265)
#petient addr.
Label(Frame1,text='Next visit',bg='pink',font='arial 10 bold').place(x=450,y=310)
#entry Field for all labels.
#TEXT veriabal for all lables
PatientName = StringVar()
DoctorID= StringVar()
Room= StringVar()
PateintId = StringVar()

Address= StringVar()
DOB =StringVar()
Gender = StringVar()
Issue= StringVar()
Medicines= StringVar()
DailyDose = StringVar()
Phone= StringVar()
Email= StringVar()
# FirstVisit = StringVar()
LastVisit = StringVar()
NextVisit= StringVar()
#left
e1 = Entry(lf1,bd=4,textvariable=PatientName)
e1.place(x=150,y=8,width=210)
e2 = Entry(lf1,bd=4, textvariable=DoctorID)
e2.place(x=150,y=50,width=210)
e3= Entry(lf1,bd=4, textvariable=Room)
e3.place(x=150,y=50,width=210)
e4 = Entry(lf1,bd=4, textvariable=PateintId)
e4.place(x=150,y=90,width=210)
e5 = Entry(lf1,bd=4, textvariable=Address)
e5.place(x=150,y=140,width=210)
e6 = Entry(lf1,bd=4, textvariable=DOB)
e6.place(x=150,y=190,width=210)
e7 = Entry(lf1,bd=4, textvariable=Gender)
e7.place(x=150,y=240,width=210)
e8 = Entry(lf1,bd=4, textvariable=Issue)
e8.place(x=150,y=290,width=210)
#right
e9 = Entry(lf1,bd=4, textvariable=Medicines)
e9.place(x=600,y=8,width=210)
e10 = Entry(lf1,bd=4, textvariable=DailyDose)
e10.place(x=600,y=50,width=210)
e11 = Entry(lf1,bd=4, textvariable=Phone)
e11.place(x=600,y=90,width=210)
e12 = Entry(lf1,bd=4, textvariable=Email)
e12.place(x=600,y=140,width=210)
# e13 = Entry(lf1,bd=4, textvariable=FirstVisit)
# e13.place(x=600,y=190,width=210)
e14 = Entry(lf1,bd=4, textvariable=LastVisit)
e14.place(x=600,y=245,width=210)
e15 = Entry(lf1,bd=4, textvariable=NextVisit)
e15.place(x=600,y=290,width=210)
#
# frame priscription
lf2 = LabelFrame(Frame1,text='PRISCIPTION',font='arial 10 bold',bd=10)
lf2.place(x=920,y=0,width=580,height=370)
#text box for  peisciption
txt_frame = Text(lf2,bg='yellow',font='impack 10 bold',width=80,height=400)
txt_frame.pack(fill=BOTH)
###############################################
#frame2
Frame2 = Frame(win,bd=15,relief=RIDGE)
Frame2.place(x=0,y=449,width=1537,height=290)
#######################################
#button delete
d_btn = Button(win,text='Delete',font='ariel 16 bold',bg='red',fg='white',bd=7,cursor='hand2')
d_btn.place(x=0,y=740,width=270)
#button prescription 
P_btn = Button(win,text='Prescription',font='ariel 16 bold',bg='purple',fg='white',bd=7,cursor='hand2')
P_btn.place(x=270,y=740,width=460)
#button save prescription data
S_btn = Button(win,text='Save Prescription Data',font='ariel 16 bold',bg='green',fg='white',bd=7,cursor='hand2',command=pdb)
S_btn.place(x=730,y=740,width=400) 
#button  clear270
C_btn = Button(win,text='CLEAR',font='ariel 16 bold',bg='Darkblue',fg='white',bd=7,cursor='hand2')
C_btn.place(x=1130,y=740,width=200) 
#button exit
E_btn = Button(win,text='EXIT',font='ariel 16 bold',bg='gold',fg='white',bd=7,cursor='hand2')
E_btn.place(x=1330,y=740,width=210)
#########################################
#Scroll  bar for prescription DATA in fill entery.
# using scroll bar are define  TKINTER module of secound line.
#using x axis to used in scroll bAR.
scroll_x = ttk.Scrollbar(Frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill=X)
#USING Y Axis to used in scroll bar.
scroll_y = ttk.Scrollbar(Frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill=Y)
#table
table = ttk.Treeview(Frame2,columns=('PNA','DID','ROOM','PID','ADD','DOB','GD','IS','MED','DD','PN','EID','LV','NV'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x =ttk.Scrollbar(command=table.xview)
scroll_y =ttk.Scrollbar(command=table.yview)
#hading for pricaption Data.
table.heading('PNA',text='Patient Name')
table.heading('DID',text='Doctor ID')
table.heading('ROOM',text='Room.No')
table.heading('PID',text='Patient ID')
table.heading('ADD',text='Address ')
table.heading('DOB',text='DOB')
table.heading('GD',text='Gender')
table.heading('IS',text='Issue')
table.heading('MED',text='Medicines')
table.heading('DD',text='Daily Dose')
table.heading('PN',text='PhoneNo.')
table.heading('EID',text='Email ID')
# table.heading('FV',text='First Visit')
table.heading('LV',text='Last Visit')
table.heading('NV',text='Next Visit')
table['show'] ='headings'
table.pack(fill=BOTH,expand=1)
###
table.column('PNA',width=100)
table.column('DID',width=100)
table.column('ROOM',width=100)
table.column('PID',width=100)
table.column('ADD',width=100)
table.column('DOB',width=100)
table.column('GD',width=100)
table.column('IS',width=100)
table.column('MED',width=100)
table.column('DD',width=100)
table.column('PN',width=100)
table.column('EID',width=100)
# table.column('FV',width=100)
table.column('LV',width=100)
table.column('NV',width=100)
mainloop()