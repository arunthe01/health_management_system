import tkinter
from tkinter import*
import tkinter.messagebox
import sqlite3


root=Tk()
ket=Tk()
ket.title('QUERIES')
ket.geometry("800x300")
root.title('hospital management system')
root.geometry("800x400")


heading= Label(root,text="HEALTH MANAGEMENT SYSTEM", bg="gray11" , fg="white" , font=100, relief="groove", height=2)
heading.grid(row=0,column=0,pady=20, padx=20)

usr_label=Label(root, text="USER-NAME", font=25).grid(row=1,column=0)

pass_label= Label(root,text="PASSWORD", font=25)
pass_label.grid(row=3,column=0)

username=Entry(root,width="35")
username.grid(row=1, column=2)

password=Entry(root,width="35")
password.grid(row=3, column=2)

fir_name =tkinter.StringVar(ket)
lst_name=tkinter.StringVar(ket)
dp_name=tkinter.StringVar(ket)
tm_=tkinter.StringVar(ket)

fi_name =tkinter.StringVar(ket)
ls_name=tkinter.StringVar(ket)
d_name=tkinter.StringVar(ket)
t_=tkinter.StringVar(ket)


def addtodb1():
	conn=sqlite3.connect('hospital.db')
	c=conn.cursor()
	c.execute("insert into DOC values(:fn , :ln , :dp_n, :timing)",
	{
	  'fn':fi_name.get(),
	  'ln':ls_name.get(),
	  'dp_n':d_name.get(),
	  'timing':t_.get()
	})

	conn.commit()
	conn.close()





def addtodb():
	conn=sqlite3.connect('hospital.db')
	c=conn.cursor()
	c.execute("insert into PAT values(:fn , :ln , :dp_n, :timing)",
	{
	  'fn':fir_name.get(),
	  'ln':lst_name.get(),
	  'dp_n':dp_name.get(),
	  'timing':tm_.get()
	})

	conn.commit()
	conn.close()



def newpat():
	newpat_=Toplevel(ket)
	newpat_.title("NEW PATIENT")
	newpat_.geometry("250x150")
	f_name=Label(newpat_,text="FIRST NAME")
	f_name.grid(row=0,column=0)
	f_entry=Entry(newpat_,width=15,textvariable=fir_name)
	f_entry.grid(row=0,column=1)
	l_name=Label(newpat_,text="LAST NAME")
	l_name.grid(row=1,column=0)
	l_entry=Entry(newpat_,width=15,textvariable=lst_name)
	l_entry.grid(row=1,column=1)
	dep_name=Label(newpat_,text="DEPARTMENT")
	dep_name.grid(row=2,column=0)
	dep_entry=Entry(newpat_,width=15,textvariable=dp_name)
	dep_entry.grid(row=2,column=1)
	tim=Label(newpat_,text="ALLOTMENT TIME")
	tim.grid(row=3,column=0)
	tim_entry=Entry(newpat_,width=15,textvariable=tm_)
	tim_entry.grid(row=3,column=1)
	sub_btn=Button(newpat_,text="SUBMIT",command=addtodb)
	sub_btn.grid(row=5,column=1)


def newdoc():
	newpat_=Toplevel(ket)
	newpat_.title("NEW DOCTOR")
	newpat_.geometry("250x150")
	f_name=Label(newpat_,text="FIRST NAME")
	f_name.grid(row=0,column=0)
	f_entry=Entry(newpat_,width=15,textvariable=fi_name)
	f_entry.grid(row=0,column=1)
	l_name=Label(newpat_,text="LAST NAME")
	l_name.grid(row=1,column=0)
	l_entry=Entry(newpat_,width=15,textvariable=ls_name)
	l_entry.grid(row=1,column=1)
	dep_name=Label(newpat_,text="DEPARTMENT")
	dep_name.grid(row=2,column=0)
	dep_entry=Entry(newpat_,width=15,textvariable=d_name)
	dep_entry.grid(row=2,column=1)
	tim=Label(newpat_,text="TIMINGS")
	tim.grid(row=3,column=0)
	tim_entry=Entry(newpat_,width=15,textvariable=t_)
	tim_entry.grid(row=3,column=1)
	sub_btn=Button(newpat_,text="SUBMIT",command=addtodb1)
	sub_btn.grid(row=5,column=1)






def patlist():
	conn=sqlite3.connect('hospital.db')
	c=conn.cursor() 
	c.execute("select * from PAT")
	this_list= c.fetchall()
	k=""

	for i in this_list :
		k+=str(i)+"\n"
		#print("FIRST NAME : " + i[0] + "\t" + "LAST NAME : " + i[1] + "\t" + "DEPARTMENT : "+ i[2] +"\t" + "TIMINGS : " +i[3]+"\t")
	conn.commit()
	conn.close()
	this_label=Label(ket,text=k).grid(row=10,column=1)



def doclist():
	conn=sqlite3.connect('hospital.db')
	c=conn.cursor() 
	c.execute("select * from DOC")
	this_list= c.fetchall()
	k=""

	for i in this_list :
		k+=str(i)+"\n"
		#print("FIRST NAME : " + i[0] + "\t" + "LAST NAME : " + i[1] + "\t" + "DEPARTMENT : "+ i[2] +"\t" + "TIMINGS : " +i[3]+"\t")
	conn.commit()
	conn.close()
	print("unga")
	this_label=Label(ket,text=k)
	this_label.grid(row=8,column=1)



def login_bt():
	x=username.get()
	y=password.get()

	if(str(x)!=str('arun') or str(y)!=str('abhinav')):
		tkinter.messagebox.showinfo("NOTE","PLEASE ENTER VALID DETAILS")
	else:
		


		Doc_list=Button(ket,text="DOC LIST",command=doclist,width=42)
		Doc_list.grid(row=8,column=0)
		pat_list=Button(ket,text="PATIENT LIST",command=patlist,width=42).grid(row=10,column=0)
		new_pat=Button(ket,text="ADD NEW PATIENT",command=newpat,width=42).grid(row=12,column=0)
		new_doc=Button(ket,text=" ADD NEW DOCTOR",command=newdoc,width=42).grid(row=14,column=0)
		

submit_btn= Button(text="login",font=25, command=login_bt)
submit_btn.grid(row=6,column=2 ,stick="s")


root.mainloop()