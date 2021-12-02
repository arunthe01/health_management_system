import tkinter
from tkinter import*
import sqlite3




#c.execute("""CREATE TABLE DOC(
#         first_name text,
 #        last_name text,
  #       department text,
   #      timings text
	#)""")

#c.execute("insert into DOC values('muni','shankar','neuro','9:00 to 11:00')")

#c.execute("select* from DOC")


#manydocs=[ ('ravi', 'sasthry' , ' ortho' , '13:00 to 14:30'), ('krishna' , 'prasad' , 'dental' , '15:00 to 17:00')]


#c.executemany("insert into DOC values(?,?,?,?)",manydocs)

#c.execute("select* from DOC")

#items =c.fetchall()

#for i in items:
	#print(i)

#c.execute("""CREATE TABLE info(
        #username text,
        #password text
	#)""")

#c.execute("insert into info values('arun','abhinav')")



#c.execute("""CREATE TABLE PAT(
 #        first_name text,
  #       last_name text,
   #      department text,
    #     timings text
     #   )""")



#manypats=[ ('kisthi', 'simha' , ' ortho ' , '13:00 to 14:30'), ('kuppaiah' , 'jari' , 'dental' , '15:00 to 17:00')]


#c.executemany("insert into PAT values(?,?,?,?)",manypats)

conn=sqlite3.connect('hospital.db')

c=conn.cursor()


c.execute (" DELETE FROM DOC WHERE first_name='muni' ")
 

conn.commit()

conn.close()


