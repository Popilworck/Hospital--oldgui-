import tkinter as tk
import modules as m
import csv
def login(nm,p):
    with open("logindata.csv",'r') as f:
        r=csv.reader(f,delimiter=',')
        for i in r:
            if i==[]:
                continue
            else:
                if i[1]==nm or i[0]==nm:
                        if i[2]==p:
                            tk.messagebox.showinfo("showinfo", "Login Successful")
                            if i[3]=='doctor':
                                return(0)#doctorsuccess
                            else:
                                return(1)#adminsuccess
                        else:
                            print("Invalid Password")
                            return(2)#invalid password
def signup(nm,idd,p,a):
    f = open("logindata.csv",'a',newline='')
    w = csv.writer(f)
    w.writerow([nm,idd,p,a.lower()])
    # if __name__ == '__main__':
    #     print("Signup Successful, redirectign to login page")
    f.close()
    if a=='doctor':
        with open((nm+'.txt'),'x')as f:
            pass
    tk.messagebox.showinfo("showinfo", "Login Successful")

def uppat(o,d):
    if o==1:
        with open(d+'.txt','w')as f:
            pass
    elif o==2:
        ma=tk.Tk()
        ma.geometry('400x75')
        name_label = tk.Label(ma, text='Enter patients name:', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(ma, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        def sub():
            name = name_entry.get()
            with open(d+'.txt','r') as f:
                temp1 = []
                for i in f.readlines():
                    if name in i:
                        continue
                    else:
                        temp1.append(i)
            with open(d+'.txt','w') as f:
                f.writelines(temp1)
            ma.destroy()
        sub_btn = tk.Button(ma, text='Submit', command=sub)
        sub_btn.grid(row=3, column=1)
        
#fix o==3     
    elif o==3:
        ma=tk.Tk()
        ma.geometry('100x100')
        name_label = tk.Label(ma, text='Enter patients name:', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(ma, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        def submit():
            nam = name_entry.get()
            with open(d+'.txt','r') as f:
                temp1 = []
                for i in f.readlines():
                    if nam in i:
                        #problem starts here
                        tma=tk.Tk()
                        tma.geometry('100x100')
                        nolle = tk.Label(tma, text='Enter Updated Name:', font=('calibre', 10, 'bold'))
                        nolle.grid(row=0, column=0)
                        nalle = tk.Entry(tma, font=('calibre', 10, 'normal'))
                        nalle.grid(row=0, column=1)
                        def sub():
                            mane = nalle.get()
                            temp1.append(mane)
                            tma.destroy()
                        sub_btn = tk.Button(tma, text='Submit', command=sub)
                        sub_btn.grid(row=3, column=1)
                    else:
                        temp1.append(i)
            print(temp1)
            with open(d+'.txt','w') as f:
                f.writelines(temp1)
            ma.destroy()
        sub_btn = tk.Button( ma, text='Submit', command=submit)
        sub_btn.grid(row=3, column=1)
        
#login complete
def inputlogin():
    root=tk.Tk()
    root.geometry("400x200")
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    def submit():
        name=name_var.get()
        password=passw_var.get()
        post =['doctor','admin','tech'][int(v.get())-1]
        ans=login(name,password)
        if ans == 1 or ans == 0:
            root.destroy()
        else:
            errormsg = tk.Label(root,text = "Invalid input, Please re-enter",bg = 'red',font=4)
            errormsg.grid(row = 5, column = 2)
            name_var.set("")
            passw_var.set("")
    v = tk.StringVar(root,'1')
    values = {"Doctor" : 1,
    		"Admin" : 2,
    		"Tech" : 3}
    for (text, value) in values.items():
    	tk.Radiobutton(root, text = text, variable = v,value = value, indicator = 0,background = "sky blue").grid(row=3,column=value)
    login_label = tk.Label(root,text='LOGIN',font = (20))
    name_label = tk.Label(root, text = 'Name or Id', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    login_label.grid(row=0,column= 2)
    name_label.grid(row=1,column=1)
    name_entry.grid(row=1,column=2)
    passw_label.grid(row=2,column=1)
    passw_entry.grid(row=2,column=2)
    sub_btn.grid(row=4,column=2)
    # listbox.grid(row=3,column=2)
    root.mainloop()
# print(inputlogin())

#signup completed
def inputsignup():
    root=tk.Tk()
    root.geometry("300x180")
    id_var = tk.StringVar()
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    def submit():
        idd = id_var.get()
        name=name_var.get()
        password=passw_var.get()
        post = ['doctor','admin','tech'][int(v.get())-1]
        signup(name,idd,password,post)
        root.destroy()
    v = tk.StringVar(root,'1')
    values = {"Doctor" : 1,
     		"Admin" : 2,
     		"Tech" : 3}
    for (text, value) in values.items():
     	tk.Radiobutton(root, text = text, variable = v,value = value, indicator = 0,background = "sky blue").grid(row=4,column=value)
    login_label = tk.Label(root,text='SIGN UP',font = (20))
    name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
    id_label = tk.Label(root, text = 'Id', font=('calibre',10, 'bold'))
    id_entry = tk.Entry(root,textvariable = id_var, font=('calibre',10,'normal'))
    
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    login_label.grid(row=0,column= 2)
    name_label.grid(row=1,column=1)
    name_entry.grid(row=1,column=2)
    id_label.grid(row=2,column=1)
    id_entry.grid(row=2,column = 2)
    passw_label.grid(row=3,column=1)
    passw_entry.grid(row=3,column=2)
    sub_btn.grid(row=5,column=2)
    root.mainloop()

# print(inputsignup())
def lors():
    main1=tk.Tk()
    ching=[]
    main1.geometry("350x100")
    def loginn():
        ching.append(0)
        main1.destroy()
    def signupp():
        ching.append(1)
        main1.destroy()
    def p():
        tk.messagebox.showinfo("showinfo", "Login Successful")
        ching.append(2)
        main1.destroy()
    b=tk.Button(main1,command=p)
    l_btn=tk.Button(main1,text = 'Login',font='5', command = loginn)
    s_btn=tk.Button(main1,text = 'Sign Up',font=5, command = signupp)
    lable = tk.Label(main1,text = "LOGIN or SIGN UP", font = 10)
    lable.grid(row=0,column=2)
    l_btn.grid(row=1,column=1)
    s_btn.grid(row=1,column=3)
    b.grid(row=2,column=1)
    main1.mainloop()
    return(ching)

def menu():
    def ad():
        inputsignup()
    def rd():
        rdmain = tk.Tk()
        rdmain.geometry("600x400")
        name_label = tk.Label(rdmain, text='Enter Doctors Name', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(rdmain, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        def submit():
            name = name_entry.get()
            m.remdoc(name)
        sub_btn = tk.Button(rdmain, text='Submit', command=submit)
        sub_btn.grid(row=1, column=1)
        rdmain.mainloop()
    def dd():
        tk.messagebox.showinfo("Doctor Names and Ids:",m.showdoc())
    def ds():
        tk.messagebox.showinfo("Doctor Names and Ids:",m.showstaff())
    def ud():
        def submit():
            global var
            name = name_entry.get()
            edit = edit_entry.get()
            val1 = int(v.get())
            m.updoc(name, edit, val1)   
        udmain = tk.Tk()
        udmain.geometry("600x400")
        name_label = tk.Label(udmain, text='Enter Doctors Name or Id', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(udmain, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        edit_label = tk.Label(udmain, text='Enter updated information', font=('calibre', 10, 'bold'))
        edit_label.grid(row=1, column=0)
        edit_entry = tk.Entry(udmain, font=('calibre', 10, 'normal'))
        edit_entry.grid(row=1, column=1)
        extra = tk.Label(udmain,text = 'Infotmation to Edit:‎‎‎‎‎‎‎‎‎', font=('calibre', 10, 'bold'))
        extra.grid(row = 0 ,column=2)
        sub_btn = tk.Button(udmain, text='Submit', command=submit)
        sub_btn.grid(row=3, column=1)
        v = tk.StringVar(udmain,'1')
        values = {"Name" : 1,
        		"Id" : 2,
        		"Password" : 3,
                "Profession":4}
        for (text, value) in values.items():
        	tk.Radiobutton(udmain, text = text, variable = v,value = value, indicator = 0,background = "sky blue",width=12).grid(row=value,column=2)
        
        udmain.mainloop()      
    def sdp1():
      rdmain = tk.Tk()
      rdmain.geometry("600x400")
      name_label = tk.Label(rdmain, text='Enter Doctors Name', font=('calibre', 10, 'bold'))
      name_label.grid(row=0, column=0)
      name_entry = tk.Entry(rdmain, font=('calibre', 10, 'normal'))
      name_entry.grid(row=0, column=1)
      def submit():
          name = name_entry.get()
          tk.messagebox.showinfo("Patients Assigned: ",m.sdp(name))
          rdmain.destroy()
      sub_btn = tk.Button(rdmain, text='Submit', command=submit)
      sub_btn.grid(row=1, column=1)
      rdmain.mainloop()  
    def ap():
        rdmain = tk.Tk()
        rdmain.geometry("600x400")
        name_label = tk.Label(rdmain, text='Enter Doctors Name', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(rdmain, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        a_label = tk.Label(rdmain, text='Enter Patients Name', font=('calibre', 10, 'bold'))
        a_label.grid(row=1, column=0)
        a_entry = tk.Entry(rdmain, font=('calibre', 10, 'normal'))
        a_entry.grid(row=1, column=1)
        def submit():
            name = name_entry.get()
            patn = a_entry.get()
            m.addpat(name, patn)
            rdmain.destroy()
        sub_btn = tk.Button(rdmain, text='Submit', command=submit)
        sub_btn.grid(row=2, column=1)
        rdmain.mainloop()
    def up():
        def submit():
            global var
            name = name_entry.get()
            val1 = int(v.get())
            uppat(val1, name)
            udmain.destroy()
        udmain = tk.Tk()
        udmain.geometry("600x400")
        name_label = tk.Label(udmain, text='Enter Doctors Name', font=('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(udmain, font=('calibre', 10, 'normal'))
        name_entry.grid(row=0, column=1)
        extra = tk.Label(udmain,text = 'Infotmation to Edit:‎‎‎‎‎‎‎‎‎', font=('calibre', 10, 'bold'))
        extra.grid(row = 0 ,column=2)
        sub_btn = tk.Button(udmain, text='Submit', command=submit)
        sub_btn.grid(row=3, column=1)
        v = tk.StringVar(udmain,'1')
        values = {"Remove All Patients" : 1,
        		"Remove A Patient" : 2,
        		"Update A Patients Name" : 3}
        for (text, value) in values.items():
        	tk.Radiobutton(udmain, text = text, variable = v,value = value, indicator = 0,background = "sky blue").grid(row=value,column=2)
    #code here
    menu = tk.Tk()			
    menu.geometry('400x400')
    b1 = tk.Button(menu, text = 'Add doctor', bd = 5,command=ad)
    b1.grid(row = 1, column=1)
    b2 = tk.Button(menu, text = 'Remove doctor',bd=5,command=rd)
    b2.grid(row=2,column=1)
    b3 = tk.Button(menu,text = 'Display Doctors',bd=5,command = dd)
    b3.grid(row=3,column=1)
    b4 = tk.Button(menu,text= "Display Staff",bd=5,command=ds)
    b4.grid(row=4,column=1)
    b5 = tk.Button(menu,text= "Update Doctor Information",bd=5,command=ud)
    b5.grid(row=5,column=1)
    b6 = tk.Button(menu,text="Show Patients Assigned to a Doctor",bd=5,command=sdp1)
    b6.grid(row=1,column=2)
    b7 = tk.Button(menu,text="Add patient",bd=5,command=ap)
    b7.grid(row=2,column=2)
    b8 = tk.Button(menu,text="Patient Functions",bd=5,command=up)
    b8.grid(row=3,column=2)
    menu.mainloop()

if __name__=='__main__':
    menu()