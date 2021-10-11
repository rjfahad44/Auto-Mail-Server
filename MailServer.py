from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import re
import os
import sys
import time
import random
import email
import imaplib
from email.message import EmailMessage
from threading import Thread
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from tqdm.auto import tqdm
from time import sleep
from tkinter.ttk import Progressbar
from datetime import datetime


root = Tk()
root.title("Auto Mail Sender")
ICON = PhotoImage(file="images/icon.png")
root.iconphoto(False, ICON)
# root.iconbitmap("images/icon.ico")



w = 400
h = 500

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

canvas = tk.Canvas(root, height=hs, width=ws)
canvas.pack()

frame = tk.Frame(root, bg="dark slate gray")
frame.place(x=20, y=25, width=360, height=450)

Label(canvas, text="Mail Server", font=('Helvetica', 13)).pack()

bgimage = PhotoImage(file="images/MailServer.png")
lable = Label(frame, image=bgimage,  width=360, height=450)
lable.pack()



root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=0, height=0)

regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
OPTIONS = [
    "Select Gender",
    "Male",
    "Female",
    "Common"
    ]
GenderSelection = StringVar(frame)
GenderSelection.set(OPTIONS[0])
log = StringVar()


def HOME():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = False
    for widget in frame.winfo_children():
        widget.destroy()
    for cnv in canvas.winfo_children():
        cnv.destroy()

    bgimage = PhotoImage(file="images/mail.png")
    img = tk.Label(frame, image=bgimage)
    img.image = bgimage
    img.place(x=0, y=-100, height=550, width=360)

    Label(frame, text="Server", font=('Helvetica', 13)).place(x=150, y=87)

    def DT():
        global stop
        global th_stop
        while True:

            def on_closing():
                global stop
                stop = True
                root.quit()
                root.destroy()

            if th_stop:
                break
            if stop:
                break

            root.protocol("WM_DELETE_WINDOW", on_closing)

            now = datetime.now()
            date = now.strftime("Date : %B %d %Y")
            time = now.strftime("Time : %I:%M:%S %p")
            Label(frame, text=time, font=('Helvetica', 15)).place(x=80, y=300)
            Label(frame, text=date, font=('Helvetica', 15)).place(x=80, y=330)
            sleep(1)
    th = Thread(target=DT)
    th.start()


def ServerSetup():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    for widget in frame.winfo_children():
        widget.destroy()
    for cnv in canvas.winfo_children():
        cnv.destroy()
    label = Label(canvas, text="Server", font=('Helvetica', 13))
    label.pack()


    # Add Server Email #
    def savedata():
        for cnv in canvas.winfo_children():
            cnv.destroy()
        label = Label(canvas, text="Add Server Email", font=('Helvetica', 13))
        label.pack()

        con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
        cursor = con.cursor()
        cursor.execute("select * from tb_server_mail")
        row = cursor.fetchall()

        if not row:
            if (re.search(regex, Email.get())):

                email = Email.get()
                password = Password.get()
                host = Host.get()
                port = Port.get()
                id = str(1)

                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("insert into tb_server_mail values('" + id + "', '" + email + "', '" + password + "', '" + host + "', '" + port + "')")
                cursor.execute("commit")

                Email.delete(0, 'end')
                Password.delete(0, 'end')
                MessageBox.showinfo("Saved Server Email", "Save Successfully")
                con.close()
                Server_thread = Thread(target=Server)
                Server_thread.start()
            else:
                MessageBox.showinfo("", "Mail/Password Are Invalid\nPlease!! Try Again")
        else:
            MessageBox.showinfo("Server Mail", "Server Mail Already Exist!!!\nYou can't add another email\nif you want to add another email,first off all delete Server email and then added new one.")

    label = tk.Label(frame, text="Enter Server Email: ", bg="dark slate gray", fg="snow2")
    label.place(x=80, y=15)
    Email = Entry(frame, font=('Helvetica', 10))
    Email.place(x=80, y=35, width=200, height=25)

    label = tk.Label(frame, text="Enter Password: ", bg="dark slate gray", fg="snow2")
    label.place(x=80, y=65)
    Password = Entry(frame, show="*", font=('Helvetica', 10))
    Password.place(x=80, y=85, width=200, height=25)

    label = tk.Label(frame, text="Enter Host: ", bg="dark slate gray", fg="snow2")
    label.place(x=80, y=120)
    Host = Entry(frame, font=('Helvetica', 10))
    Host.place(x=80, y=140, width=200, height=25)

    label = tk.Label(frame, text="Enter Port: ", bg="dark slate gray", fg="snow2")
    label.place(x=80, y=175)
    Port = Entry(frame, font=('Helvetica', 10))
    Port.place(x=80, y=195, width=70, height=25)


    button = Button(frame, text="Save", bg="sea green", command=savedata, fg="snow2")
    button.place(x=80, y=230, width=200)


    # Edit Server Email #
    def cb(event):
        def Edititem():
            for cnv in canvas.winfo_children():
                cnv.destroy()
            label = Label(canvas, text="Edit Server Email", font=('Helvetica', 13))
            label.pack()
            def Update():
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("update tb_server_mail set S_id='" + str(1) + "', S_email='" + Email.get() + "', S_password='" + Password.get() + "', S_host='" + Host.get() + "', S_port='" + Port.get() + "'")
                cursor.execute("commit")
                Email.delete(0, 'end')
                Password.delete(0, 'end')
                MessageBox.showinfo("Update Server Email", "Update Successfully")
                con.close()
                ServerEmailList.delete(0, tk.END)

            label = tk.Label(frame, text="Enter Server Email: ", bg="dark slate gray", fg="snow2")
            label.place(x=80, y=15)
            Email = Entry(frame, font=('Helvetica', 10))
            Email.insert(0, select[0][1])
            Email.place(x=80, y=35, width=200, height=25)

            label = tk.Label(frame, text="Enter Password: ", bg="dark slate gray", fg="snow2")
            label.place(x=80, y=65)
            Password = Entry(frame, show="*", font=('Helvetica', 10))
            Password.insert(0, select[0][2])
            Password.place(x=80, y=85, width=200, height=25)

            label = tk.Label(frame, text="Enter Host: ", bg="dark slate gray", fg="snow2")
            label.place(x=80, y=120)
            Host = Entry(frame, font=('Helvetica', 10))
            Host.insert(0, select[0][3])
            Host.place(x=80, y=140, width=200, height=25)

            label = tk.Label(frame, text="Enter Port: ", bg="dark slate gray", fg="snow2")
            label.place(x=80, y=175)
            Port = Entry(frame, font=('Helvetica', 10))
            Port.insert(0, select[0][4])
            Port.place(x=80, y=195, width=70, height=25)

            button = Button(frame, text="Update", bg="sea green", command=Update, fg="snow2")
            button.place(x=80, y=230, width=200)


        # Delete Server Email #
        def Deleteitem():
            for cnv in canvas.winfo_children():
                cnv.destroy()
            label = Label(canvas, text="Delete Server Email", font=('Helvetica', 13))
            label.pack()

            result = MessageBox.askquestion('Delete!!', select[0][1] + "\n\nDo you want to Delete this anyway!!!")

            if result == 'yes':
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("delete from tb_server_mail where S_email ='" + select[0][1] + "'")
                cursor.execute("commit")
                con.close()
                MessageBox.showinfo("Delete Server Mail!!", "Delete Successfully")
                ServerSetup()
            else:
                ServerSetup()


        con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
        cursor = con.cursor()
        cursor.execute("select * from tb_server_mail")
        select = cursor.fetchall()
        con.close()

        def Cancel():
            ServerSetup()

        button = Button(frame, text="Edit", bg="sea green", command=Edititem, width=9)
        button.place(x=80, y=400)

        button = Button(frame, text="Cancel", bg="sandy brown", command=Cancel, width=6)
        button.place(x=154, y=400)

        button = Button(frame, text="Delete", bg="salmon1", command=Deleteitem, width=9)
        button.place(x=206, y=400)


    scrollbar = Scrollbar(frame)
    scrollbar.place()
    ServerEmailList = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=SINGLE, bg="azure3")
    lable = Label(frame, text="The Server Email is shown below : ",font=('Comic Sans MS', 11), bg="dark slate gray", fg="linen")
    lable.place(x=65, y=280)
    lable = Label(frame, text="\nif you want to edit/delete server mail\nplease click the server mail.", bg="dark slate gray", fg="linen")
    lable.place(x=80, y=300)

    ServerEmailList.place(x=60, y=360, height=20, width=250)

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_server_mail")
    row = cursor.fetchall()
    con.close()
    ServerEmailList.insert(END, row[0][1])
    ServerEmailList.bind('<<ListboxSelect>>', cb)
    scrollbar.config(command=ServerEmailList.yview)


def AgentSerevr():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    GenderSelection.set(OPTIONS[0])
    for widget in frame.winfo_children():
        widget.destroy()
    for cnv in canvas.winfo_children():
        cnv.destroy()
    label = Label(canvas, text="Agent", font=('Helvetica', 13))
    label.pack()

    def savedata():
        for cnv in canvas.winfo_children():
            cnv.destroy()
        label = Label(canvas, text="Add Agent", font=('Helvetica', 13))
        label.pack()

        if Fname.get() == "" or Lname.get() == "" or Email.get() == "":
            MessageBox.showinfo("Add Agent", "Something is wrong")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
            cursor = con.cursor()
            cursor.execute("insert into tb_client_mail values('','"+Fname.get()+"','"+Lname.get()+"','"+Email.get()+"','"+GenderSelection.get()+"', '"+str(1)+"')")
            cursor.execute("commit")

            Fname.delete(0, 'end')
            Lname.delete(0, 'end')
            Email.delete(0, 'end')
            GenderSelection.set(OPTIONS[0])
            MessageBox.showinfo("Add Agent", "Add Successfully")
            AgentSerevr()
            con.close()

    label = tk.Label(frame, text="Enter First Name: ", bg="dark slate gray", fg="snow")
    label.place(x=30, y=10)
    Fname = Entry(frame, font=('Helvetica', 11), width=22)
    Fname.place(x=145, y=10)
    label = tk.Label(frame, text="Enter Last Name: ", bg="dark slate gray", fg="snow")
    label.place(x=30, y=40)
    Lname = Entry(frame, font=('Helvetica', 11), width=22)
    Lname.place(x=145, y=40)
    label = tk.Label(frame, text="Enter Email: ", bg="dark slate gray", fg="snow")
    label.place(x=30, y=80)
    Email = Entry(frame, font=('Helvetica', 11), width=22)
    Email.place(x=145, y=80)

    Gender = OptionMenu(frame, GenderSelection, *OPTIONS)
    Gender.place(x=30, y=110, width=115)

    savebtn = Button(frame, text="Save", bg="pale green", command=savedata)
    savebtn.place(x=150, y=110, height=30,  width=178)


    def cb(event):

        def Edititem():
            for cnv in canvas.winfo_children():
                cnv.destroy()
            label = Label(canvas, text="Edit Agent", font=('Helvetica', 13))
            label.pack()
            def Update():
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("update tb_client_mail set Fname='" + Fname.get() + "',Lname='" + Lname.get() + "',Email='" + Email.get() + "',Gender='" + GenderSelection.get() + "' where Email='"+ email +"'")
                cursor.execute("commit")
                Fname.delete(0, 'end')
                Lname.delete(0, 'end')
                Email.delete(0, 'end')
                GenderSelection.set(OPTIONS[0])
                MessageBox.showinfo("Update Agent", "Update Successfully")
                con.close()
                ListBox_for_agent.delete(0, tk.END)
                AgentSerevr()

            label = tk.Label(frame, text="Edit First Name: ", bg="dark slate gray", fg="snow")
            label.place(x=30, y=10)
            Fname = Entry(frame, font=('Helvetica', 11), width=22)
            Fname.insert(0, select[0][1])
            Fname.place(x=145, y=10)
            label = tk.Label(frame, text="Edit Last Name: ", bg="dark slate gray", fg="snow")
            label.place(x=30, y=40)
            Lname = Entry(frame, font=('Helvetica', 11), width=22)
            Lname.insert(0, select[0][2])
            Lname.place(x=145, y=40)
            label = tk.Label(frame, text="Edit Email: ", bg="dark slate gray", fg="snow")
            label.place(x=30, y=80)
            Email = Entry(frame, font=('Helvetica', 11), width=22)
            Email.insert(0, select[0][3])
            Email.place(x=145, y=80)

            Gender = OptionMenu(frame, GenderSelection, *OPTIONS)
            GenderSelection.set(select[0][4])
            Gender.place(x=30, y=110, width=115)

            savebtn = Button(frame, text="Update", bg="pale green", command=Update)
            savebtn.place(x=150, y=110, height=30, width=178)

        def Cancel():
            AgentSerevr()

        def Delete():
            for cnv in canvas.winfo_children():
                cnv.destroy()
            label = Label(canvas, text="Delete Agent", font=('Helvetica', 13))
            label.pack()
            con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
            cursor = con.cursor()
            cursor.execute("select * from tb_client_mail where Email = '"+ email +"'")
            search_item = cursor.fetchall()
            con.close()
            # print(search_item[0][3])

            result = MessageBox.askquestion('Delete!!', value.split()[0] + ' .' + search_item[0][3] + "\n\nDo you want to Delete this anyway!!!")

            if result == 'yes':
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("delete from tb_client_mail where Email ='" + email + "'")
                cursor.execute("commit")
                con.close()
                MessageBox.showinfo("Delete Agent!!", "Delete Successfully")
                AgentSerevr()
            else:
                AgentSerevr()


        # id = str(ListBox_for_agent.curselection()[0]+1)
        value = ListBox_for_agent.get(ListBox_for_agent.curselection())
        # print(value.split()[3])
        email = value.split()[3]
        con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
        cursor = con.cursor()
        cursor.execute("select * from tb_client_mail where Email='" + email + "'")
        select = cursor.fetchall()
        con.close()

        button = Button(frame, text="Edit", bg="sea green", command=Edititem, fg="snow", width=16)
        button.place(x=0, y=410)

        button = Button(frame, text="Cancel", bg="sandy brown", command=Cancel, fg="snow", width=15)
        button.place(x=123, y=410)

        button = Button(frame, text="Delete", bg="coral1", command=Delete, fg="snow", width=16)
        button.place(x=239, y=410)


    scrollbar = Scrollbar(frame)
    scrollbar.place(x=345, y=160, height=250)
    ListBox_for_agent = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=SINGLE, bg="lavender")

    ListBox_for_agent.place(x=0, y=160, width=345, height=250)

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_client_mail")
    row = cursor.fetchall()
    con.close()
    c = 1
    for i in row:
        ListBox_for_agent.insert(END, str(c) + '. ' + i[1] + ' ' + i[2] + "     " + i[3])
        c = c + 1
    ListBox_for_agent.bind('<<ListboxSelect>>', cb)
    scrollbar.config(command=ListBox_for_agent.yview)


def ShowAgentMail():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    for widget in frame.winfo_children():
        widget.destroy()
    for cnv in canvas.winfo_children():
        cnv.destroy()
    label = Label(canvas, text="All Agent Email", font=('Helvetica', 13))
    label.pack()


    scrollbar = Scrollbar(frame)
    scrollbar.place(x=345, rely=0, relheight=1)
    list = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=SINGLE, bg="lavender")

    list.place(relx=0, rely=0, relheight=1, width=345)

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_client_mail")
    row = cursor.fetchall()
    con.close()
    c = 1
    for i in row:
        list.insert(END, str(c) + '. Name: ' + i[1] + ' ' + i[2])
        list.insert(END, '    Email: ' + i[3])
        c = c + 1
    scrollbar.config(command=list.yview)


def isActiveStatus():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    for widget in frame.winfo_children():
        widget.destroy()
    for cnv in canvas.winfo_children():
        cnv.destroy()
    label = Label(canvas, text="Active Status", font=('Helvetica', 13))
    label.pack()

    def cb(event):
        value = List_of_Active_status.get(List_of_Active_status.curselection())
        email = value.split()[2]
        # print(email)
        con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
        cursor = con.cursor()
        cursor.execute("select * from tb_client_mail where Email = '"+ email +"'")
        row = cursor.fetchall()
        # print(row[0][5])
        con.close()
        def is_change():
            if row[0][5]:
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("update tb_client_mail set isActive='"+ str(0)  +"' where Email ='" + email + "'")
                cursor.execute("commit")
                con.close()
                isActiveStatus()

            else:
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("update tb_client_mail set isActive='"+ str(1) +"' where Email ='" + email + "'")
                cursor.execute("commit")
                con.close()
                isActiveStatus()
        Active_btn = Button(frame, text="Change Active Status", bg="dark slate blue", fg="snow", command=is_change)
        Active_btn.place(relx=0, rely=0, width=285, height=30)

        Active_btn = Button(frame, text="Cancel", bg="sandy brown", command=isActiveStatus)
        Active_btn.place(x=285, rely=0, width=60, height=30)

    scrollbar = Scrollbar(frame)
    scrollbar.place(x=345, rely=0, relheight=1)
    List_of_Active_status = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=SINGLE, bg="lavender")
    List_of_Active_status.place(x=0, y=30, height=390, width=345)

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_client_mail")
    row = cursor.fetchall()
    con.close()
    c = 1
    for i in row:
        if i[5]:
            active = 'ON'
        else:
            active = 'OFF'
        email = str(c) + '. ' + active.ljust(20) + i[3]

        List_of_Active_status.insert(END, email)
        c = c + 1
    List_of_Active_status.bind('<<ListboxSelect>>', cb)
    scrollbar.config(command=List_of_Active_status.yview)


serverlog = True
def Server():
    global serverlog
    global th_stop
    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_server_mail")
    row = cursor.fetchall()
    con.close()

    if not row:
        MessageBox.showinfo("Server Mail", "Server Mail is Empty!\nPlease Set Server Mail")
        ServerSetup()
    else:
        global stop
        global counter
        global on_closing
        counter = 0
        while True:

            serverlog = False
            def on_closing():
                global stop
                stop = True
                root.quit()
                root.destroy()
            if stop:
                break
            root.protocol("WM_DELETE_WINDOW", on_closing)


            # global log
            # log.set("Server is running"+ "*"*counter)
            # counter += 1
            # if counter == 5:
            #     counter = 0


            con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
            cursor = con.cursor()
            cursor.execute("select * from tb_server_mail")
            row = cursor.fetchall()
            con.close()

            if not row:
                MessageBox.showinfo("Server Mail", "Server Mail is Empty!\nPlease Set Server Mail")
                ServerSetup()
                break


            con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
            cursor = con.cursor()
            cursor.execute("select * from tb_client_mail where isActive = '"+str(1)+"'")
            client_mail = cursor.fetchall()
            # print(client_mail[0][3])
            con.close()

            if not client_mail:
                MessageBox.showinfo("Client Mail", "Client Mail is Empty!\nPlease Add Client Mail")
                AgentSerevr()
                break


            subject = ""
            msg = ""
            receivers = []

            TAG_RE = re.compile(r'<[^>]+>')

            def remove_tags(text):
                return TAG_RE.sub('\n', text)

            # Defined Server Mail
            sender = row[0][1]
            password = row[0][2]
            HOST = row[0][3]
            PORT = row[0][4]

            # Agent Mail ID
            for i in client_mail:
                receivers.append(i[3])

            n = random.randint(0, len(receivers)-1)
            # print(receivers[n])
            # lable = Label(frame, text=receivers[n])
            # lable.pack()

            # Mail Host Server Login
            mail = imaplib.IMAP4_SSL(HOST)
            mail.login(sender, password)

            # Check Server inbox
            mail.select('INBOX')

            # check new mail
            _, search_unseen_mail = mail.search(None, 'UNSEEN')
            a = not search_unseen_mail[0]
            # print(a)

            if a:
                print('New Email Not Found!!!')
            else:
                for num in search_unseen_mail[0].split():
                    _, data = mail.fetch(num, '(RFC822)')
                    _, b = data[0]
                    email_message = email.message_from_bytes(b)
                    subject = email_message['subject']
                    From = email_message['From']
                    # print(From)

                    for part in email_message.walk():
                        if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
                            body = part.get_payload(decode=True)
                            msg = body.decode()
                            # print(body.decode())
                # print(remove_tags(msg))

                # Server Email Send To Random Client
                content = remove_tags(msg)
                email_message = EmailMessage()
                email_message.add_header('To', receivers[n])
                email_message.add_header('From', sender)
                email_message.add_header('Subject', subject)
                email_message.add_header('X-Priority', '1')
                email_message.set_content(content)

                now = datetime.now()
                now = now.strftime("Date : %B %d %Y, Time : %I:%M:%S %p")

                # Receiving Mail Log for mysql database #
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("insert into tb_receiving_log values('','" + now + "','" + From + "','" + sender + "','" + subject + "', '" + content + "')")
                cursor.execute("commit")
                # MessageBox.showinfo("Send Mail", "Send Mail Successfully To "+receivers[n])
                con.close()



                # Sending Mail Log for mysql database #
                con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
                cursor = con.cursor()
                cursor.execute("insert into tb_sending_log values('','" + now + "','" + sender + "','" + receivers[n] + "','" + subject + "', '" + content + "')")
                cursor.execute("commit")
                # MessageBox.showinfo("Send Mail", "Send Mail Successfully To "+receivers[n])
                con.close()


                # Connect, authenticate, and send mail
                server = SMTP_SSL('smtp.gmail.com', PORT)
                # server.set_debuglevel(1)
                server.login(sender, password)

                # server.sendmail(sender, receivers[n], email_message.as_bytes())
                print(f'Send Mail Successfully To : {receivers[n]}')
                MessageBox.showinfo("Send Mail To : ", receivers[n])

                # Disconnect
                server.quit()
            time.sleep(1)
        serverlog = True


def ServerLog():
    global log_stop
    log_stop = False
    global th_stop
    th_stop = True
    for canv in canvas.winfo_children():
        canv.destroy()
    canvas.pack()
    for widge in frame.winfo_children():
        widge.destroy()

    label = Label(canvas, text="Server Log", font=('Helvetica', 13))
    label.pack()


    def LOG():
        global serverlog
        global log_stop
        counter = 0
        while True:

            def on_closing():
                global stop
                stop = True
                root.quit()
                root.destroy()
            if log_stop:
                break
            if stop:
                break
            if serverlog:
                lable = Label(frame, text="Server is Stop!!!", font=("ITALIC", 12, "bold"), bg="dark slate gray", fg="snow")
                lable.place(x=120, y=15)
                break

            root.protocol("WM_DELETE_WINDOW", on_closing)
            pb1['value'] += 10
            counter += 1

            lable = Label(frame, text="Server is Running", font=("ITALIC", 12, "bold"), bg="dark slate gray", fg="snow")
            lable.place(x=100, y=15)

            Clable = Label(frame, text="." * counter, font=("ITALIC", 14, "bold"), bg="dark slate gray", fg="green2")
            Clable.place(x=240, y=15)

            if counter == 5:
                Clable = Label(frame, text="." * counter, font=("ITALIC", 14, "bold"), bg="dark slate gray", fg="dark slate gray")
                Clable.place(x=240, y=15)
                counter = 0

            sleep(1)

    pb1 = Progressbar(frame, orient=HORIZONTAL, length=200, mode='indeterminate')
    pb1.place(x=80, y=50)

    button = Button(root, command=Thread(target=LOG).start())
    button.pack()
    button.pack_forget()


def SendingLog():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    for canv in canvas.winfo_children():
        canv.destroy()
    canvas.pack()
    for f in frame.winfo_children():
        f.destroy()

    label = Label(canvas, text="Sending Mail Log", font=('Helvetica', 13))
    label.pack()

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_sending_log")
    sendingMailLog = cursor.fetchall()
    con.close()
    # print(sendingMailLog[0][1])


    # DateandTime = sendingMailLog[0][1]
    # From = sendingMailLog[0][2]
    # To = sendingMailLog[0][3]
    # Subject = sendingMailLog[0][4]
    # Body = sendingMailLog[0][5].rstrip()
    # print(DateandTime)
    # print(From)
    # print(To)
    # print(Subject)
    # print(Body)


    scrollbar = Scrollbar(frame)
    scrollbar.place(x=345, rely=0, relheight=1)
    list_for_sending_log = Listbox(frame, yscrollcommand=scrollbar.set, bg="lavender")
    list_for_sending_log.place(relx=0, rely=0, relheight=1, width=345)
    c = 1
    for i in sendingMailLog:
        list_for_sending_log.insert(END, str(c) + '. ' + i[1],
                                    "               From : " + i[2],
                                    "               To : " + i[3],
                                    "               Subject : " + i[4],
                                    "               Body : " + i[5])
        c = c + 1
    # list_for_sending_log.configure(state=DISABLED)
    scrollbar.config(command=list_for_sending_log.yview)


def ReceivingLog():
    global log_stop
    log_stop = True
    global th_stop
    th_stop = True
    for canv in canvas.winfo_children():
        canv.destroy()
    canvas.pack()
    for f in frame.winfo_children():
        f.destroy()

    label = Label(canvas, text="Receiving Mail Log", font=('Helvetica', 13))
    label.pack()

    con = mysql.connect(host="localhost", user="root", password="", database="db_serveremail")
    cursor = con.cursor()
    cursor.execute("select * from tb_receiving_log")
    receivingMailLog = cursor.fetchall()
    con.close()
    # print(receivingMailLog[0][1])

    # DateandTime = receivingMailLog[0][1]
    # From = receivingMailLog[0][2]
    # To = receivingMailLog[0][3]
    # Subject = receivingMailLog[0][4]
    # Body = receivingMailLog[0][5].rstrip()
    # print(DateandTime)
    # print(From)
    # print(To)
    # print(Subject)
    # print(Body)

    scrollbar = Scrollbar(frame)
    scrollbar.place(x=345, rely=0, relheight=1)
    list_for_sending_log = Listbox(frame, yscrollcommand=scrollbar.set, bg="lavender")
    list_for_sending_log.place(relx=0, rely=0, relheight=1, width=345)

    c = 1
    for i in receivingMailLog:
        list_for_sending_log.insert(END, str(c) + '. ' + i[1],
                                    "               To : " + i[2],
                                    "               From : " + i[3],
                                    "               Subject : " + i[4],
                                    "               Body : " + i[5])
        c = c + 1
    # list_for_sending_log.configure(state=DISABLED)
    scrollbar.config(command=list_for_sending_log.yview)


stop = False
def onExit():
    global stop
    stop = True
    root.quit()
    root.destroy()




menubar = Menu(root)

Home = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", command=HOME)

server = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Server", menu=server)
server.add_command(label="Server Setup", command=ServerSetup)
# server.add_command(label="Edit Server Email", command=editServerMail)
# server.add_command(label="Delete Server Email", command=deleteServerMail)
# server.add_command(label="Show Server Email", command=showServerMail)
server.add_separator()
# server.add_command(label="Exit", command=root.destroy)
server.add_command(label="Exit", command=onExit)

client = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Agent", menu=client)
client.add_command(label="Agent", command=AgentSerevr)
# client.add_command(label="Add Client Email", command=AddAgentMail)
# client.add_command(label="Edit Client Email", command=UpdateAgentMail)
# client.add_command(label="Delete Client Email", command=DeleteAgentMail)
client.add_command(label="Active Status", command=isActiveStatus)
client.add_command(label="Show All", command=ShowAgentMail)

Log = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Log", menu=Log)
Log.add_separator()
Log.add_command(label="Show Server Log", command=ServerLog)
Log.add_separator()
Log.add_command(label="Show All Sending Log", command=SendingLog)
Log.add_separator()
Log.add_command(label="Show All Receiving Log", command=ReceivingLog)
Log.add_separator()

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About")


button_server = Button(root, command=Thread(target=Server).start())
button_server.place()
button_server.place_forget()


root.config(menu=menubar)
root.mainloop()