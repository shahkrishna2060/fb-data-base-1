from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title("FACEBOOK")
root.iconbitmap("fb.ico")
root.geometry("320x600")
root.configure(bg="royalblue2")
root.resizable(0,1)

my_image=Image.open("fb.png")
resized_image=my_image.resize((80,60))
converted_image=ImageTk.PhotoImage(resized_image)
Label(image=converted_image).grid(row=0,column=0)
 

conn=sqlite3.connect("facebook.db")
c=conn.cursor()

# c.execute("""CREATE TABLE user(
#     firstName text,
#     lastNAme text,
#     address text,
#     age integer, 
#     password text,
#     fatherName text,
#     city text,
#     zip_code integer
#     )""")
# print("Table created successfully")

def submit():
    conn=sqlite3.connect("facebook.db")

    c=conn.cursor()
    c.execute("INSERT into user VALUES(:fname,:lname,:address,:age,:password,:fatherName,:city,:zip_code)",{
        "fname":fname.get(),
        "lname":lname.get(),
        "address":address.get(),
        "age":age.get(),
        "password":password.get(),
        "fatherName":fatherName.get(),
        "city":city.get(),
        "zip_code":zip_code.get()
    })
    messagebox.showinfo("USER","Inserted Sucessfully")
    conn.commit()
    conn.close()
    fname.delete(0,END)
    lname.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    fatherName.delete(0,END)
    city.delete(0,END)
    zip_code.delete(0,END)


def query():
    
    conn=sqlite3.connect("facebook.db")

    c=conn.cursor()
    c.execute("SELECT *, oid FROM user")
    records=c.fetchall()
    # print(records)

    print_record=''
    for record in records:
        print_record += str(record[0]) +' ' + str(record[1]) + ' ' +' '+'\t'+ str(record[8]) + '\n'
    
    query_label=Label(root,text=print_record,fg="black",bg="snow3")
    query_label.grid(row=9,column=0,columnspan=2)
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()

    c.execute("DELETE from user WHERE oid = "+ delete_box.get())
    print("Deleted Successfully")


    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute ("""UPDATE user SET 
        firstName=:first,
        lastName=:last,
        address=:address,
        age=:age,
        password=:password,
        fatherName=:fatherName,
        city=:city,
        zip_code=:zipcode
        WHERE oid = :oid """,
        {"first":fname_editor.get(),
        "last":lname_editor.get(),
        "address":address_editor.get(),
        "age":age_editor.get(),
        "password":password_editor.get(),
        "fatherName":fatherName_editor.get(),
        "city":city_editor.get(),
        "zipcode":zipcode_editor.get(),
        "oid":record_id

        }
    )

    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor=Toplevel()
    editor.title("Update Data")
    editor.geometry("300x400")
    editor.iconbitmap("fb.ico")
    editor.configure(bg="royalblue2")
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE oid="+record_id)
    records=c.fetchall()

    global fname_editor
    global lname_editor
    global address_editor
    global age_editor
    global password_editor
    global fatherName_editor
    global city_editor
    global zipcode_editor

    fname_editor=Entry(editor,width=25,bg="snow3",fg="beepskyblue2")
    fname_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    lname_editor=Entry(editor,width=25,bg="snow3",fg="black")
    lname_editor.grid(row=1,column=1)

    address_editor=Entry(editor,width=25,bg="snow3",fg="black")
    address_editor.grid(row=2,column=1)

    age_editor=Entry(editor,width=25,bg="snow3",fg="black")
    age_editor.grid(row=3,column=1)
    
    password_editor=Entry(editor,width=25,bg="snow3",fg="black")
    password_editor.grid(row=4,column=1)

    fatherName_editor=Entry(editor,width=25,bg="snow3",fg="black")
    fatherName_editor.grid(row=5,column=1)

    city_editor=Entry(editor,width=25,bg="snow3",fg="black")
    city_editor.grid(row=6,column=1)
    
    zipcode_editor=Entry(editor,width=25,bg="snow3",fg="black")
    zipcode_editor.grid(row=7,column=1)

    fname_label=Label(editor,text="First Name",width=15,bg="snow3",fg="black",pady=5)
    fname_label.grid(row=0,column=0,pady=(10,0))

    lname_label=Label(editor,text="Last Name",width=15,bg="snow3",fg="black",pady=5)
    lname_label.grid(row=1,column=0)
    
    address_label=Label(editor,text="Address",width=15,bg="snow3",fg="black",pady=5)
    address_label.grid(row=2,column=0)

    age_label=Label(editor,text="Age",width=15,bg="snow3",fg="black",pady=5)
    age_label.grid(row=3,column=0)

    password_label=Label(editor,text="Password",width=15,bg="snow3",fg="black",pady=5)
    password_label.grid(row=4,column=0)

    fatherName_label=Label(editor,text="Father Name",width=15,bg="snow3",fg="black",pady=5)
    fatherName_label.grid(row=5,column=0)

    city_label=Label(editor,text="City",width=15,bg="snow3",fg="black",pady=5)
    city_label.grid(row=6,column=0)

    zipcode_label=Label(editor,text="Zipcode",width=15,bg="snow3",fg="black",pady=5)
    zipcode_label.grid(row=7,column=0)

    for record in records:
        fname_editor.insert(0,record[0])
        lname_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        fatherName_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])

    edit_btn=Button(editor,text="Save",command=update,bg="snow3",fg="black")
    edit_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
    
facebook=Label(root,text="Facebook",font=("arial",30,"bold"),bg="snow3",fg="black")
facebook.grid(row=0,column=1,columnspan=2)

fname=Entry(root,width=30,bg="snow3",fg="black")
fname.grid(row=1,column=1)

lname=Entry(root,width=30,bg="snow3",fg="black")
lname.grid(row=2,column=1)

address=Entry(root,width=30,bg="snow3",fg="black")
address.grid(row=3,column=1)

age=Entry(root,width=30,bg="snow3",fg="black")
age.grid(row=4,column=1)

password=Entry(root,width=30,bg="snow3",fg="black",show="*")
password.grid(row=5,column=1)

fatherName=Entry(root,width=30,bg="snow3",fg="black")
fatherName.grid(row=6,column=1)

city=Entry(root,width=30,bg="snow3",fg="black")
city.grid(row=7,column=1)

zip_code=Entry(root,width=30,bg="snow3",fg="black")
zip_code.grid(row=8,column=1)

delete_box=Entry(root,width=30,bg="snow3",fg="black")
delete_box.grid(row=13,column=1,pady=5)

fname_label=Label(root,text="First Name",bg="snow3",fg="black",width=15,pady=5)
fname_label.grid(row=1,column=0)

lname_label=Label(root,text="Last Name",bg="snow3",fg="black",width=15,pady=5)
lname_label.grid(row=2,column=0)

address_label=Label(root,text="Address",bg="snow3",fg="black",width=15,pady=5)
address_label.grid(row=3,column=0)

age_label=Label(root,text="Age",bg="snow3",fg="black",width=15,pady=5)
age_label.grid(row=4,column=0)

password_label=Label(root,text="Password",bg="snow3",fg="black",width=15,pady=5)
password_label.grid(row=5,column=0)

fatherName_label=Label(root,text="Father Name",bg="snow3",fg="black",width=15,pady=5)
fatherName_label.grid(row=6,column=0)

city_label=Label(root,text="City",bg="snow3",fg="black",width=15,pady=5)
city_label.grid(row=7,column=0)

zip_code_label=Label(root,text="Zip code",bg="snow3",fg="black",width=15,pady=5)
zip_code_label.grid(row=8,column=0)

delete_label=Label(root,text="Delete ID",bg="snow3",fg="black",width=15,pady=5)
delete_label.grid(row=13,column=0,pady=5)

submit_btn=Button(root,text="Add Records",command=submit,bg="snow3",fg="black")
submit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show Records",command=query,bg="snow3",fg="black")
query_btn.grid(row=12,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

delete_btn=Button(root,text="Delete",command=delete,bg="snow3",fg="black")
delete_btn.grid(row=14,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

edit_btn=Button(root,text="Update",command=edit,bg="snow3",fg="black")
edit_btn.grid(row=15,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


conn.commit()
conn.close()
root.mainloop()