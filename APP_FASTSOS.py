from tkinter import *
import random

class app:
    def __init__(self):

        self.destroy()

        title = Label(root, text='EMERGENCY APP')
        title.pack()

        emer = Button(root, text='EMERGENCY', font=('Arial', 90), fg='red', command=self.emergency)
        emer.pack(pady=150)

        genh = Button(root, text='GENERAL HEALTH', font=('Arial', 30),command=self.gen)
        genh.pack()
        self.s = []
        self.h = ''
        self.name = 'Rajesh'
        self.age = 25
        self.height = 175
        self.weight = 67

        root.mainloop()

    def destroy(self):
        children = root.winfo_children()
        for child in children:
            child.destroy()

    def symptoms(self, s):
        self.s.append(s)
        self.s = list(set(self.s))

    def submit(self):
        self.destroy()
        sym = Label(root, text=f'Your Symptoms: {self.s}')
        if 'ROAD ACCIDENT' in self.s:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[0][1]}')
        elif 'CHEST PAIN' in self.s or 'STROKE' in self.s:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[1][1]}')
        elif 'ROAD ACCIDENT' in self.s:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[2][1]}')
        elif 'CHEST PAIN' in self.s and 'BREATHING DIFFICULTY' in self.s:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[4][1]}')
        elif 'NAUSEA' in self.s and 'STROKE' in self.s:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[3][1]}')
        else:
            hos = Label(root, text=f'Preferred Hospital: {self.hosInfo[0][1]}')

        l = Label(root, text='Your Ambulance is on the way', font=('Arial',40))
        back = Button(root, text='BACK', command=self.emergency)
        sym.pack()
        hos.pack()
        l.pack()
        back.pack()

    def emergency(self):
        self.destroy()
        self.s = []

        resFrame = Frame(root, height=450, width=225, highlightbackground='black', highlightthickness=3)
        resFrame.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)
        l1 = Label(resFrame, text='HOSPITALS NEAR YOU', fg='black', font=('Arial', 20))
        l1.pack()

        self.hosInfo = [[8.78, 'Aakash Hospital', 45], [1.34, 'MIOT International', 7], [7.80, 'FFCS Hospital', 17],
                        [4.56, 'St. Louis Hospital', 33], [3.14, 'Apollo Hospitals', 19]]

        l = len(self.hosInfo)

        self.hosInfo.sort()

        for i in range(l):
            button = Label(resFrame, font=('Arial', 17),
                           text=f'{self.hosInfo[i][1]}\nDistance: {self.hosInfo[i][0]} km\n'
                                f'Available Beds: {self.hosInfo[i][2]}')
            button.pack()
            sep = Label(resFrame, text='--------------------------')
            sep.pack()

        symFrame = Frame(root, height=450, width=225, highlightbackground='black', highlightthickness=3)
        symFrame.grid(row=0, column=1, padx=1, pady=1, ipadx=20, ipady=20)
        l2 = Label(symFrame, text='SELECT YOUR SYMPTOMS', fg='black', font=('Arial', 20))
        l2.pack()

        b1 = Button(symFrame, text='ROAD ACCIDENT', padx=25, pady=25, command=lambda: self.symptoms('ROAD ACCIDENT'))
        b1.pack()

        b2 = Button(symFrame, text='CHEST PAIN', padx=25, pady=25, command=lambda: self.symptoms('CHEST PAIN'))
        b2.pack()

        b3 = Button(symFrame, text='BREATHING DIFFICULTY', padx=25, pady=25,
                    command=lambda: self.symptoms('BREATHING DIFFICULTY'))
        b3.pack()

        b4 = Button(symFrame, text='NAUSEA\n(VOMITING)', padx=25, pady=25, command=lambda: self.symptoms('NAUSEA'))
        b4.pack()

        b5 = Button(symFrame, text='STROKE\n(FAINTING)', padx=25, pady=25, command=lambda: self.symptoms('STROKE'))
        b5.pack()

        submit = Button(root, text='SUBMIT', command=self.submit)
        submit.grid(row=1, column=1, ipadx=75)
        back = Button(root, text='BACK', command=self.__init__)
        back.grid(row=1, column=0)

    def currentinsurance(self):
        self.destroy()
        i1 = Label(root, text='YOUR CURRENT INSURANCE DETAILS',font=('Arial',30)).pack()
        i2 = Label(root, text='Insurance Number: 12345678').pack()
        i3 = Label(root, text='Premium: Rs.35,000').pack()
        i4 = Label(root, text='Available claims amount: Rs.8,677').pack()
        i5 = Label(root, text='Coverage Duration: 25 years').pack()
        back = Button(root, text='BACK', command=self.insurance).pack()

    def buynow(self,v):
        self.destroy()
        sel = Label(root,text=f'THANK YOU FOR PURCHASING\n\n{v}\n\nINSURANCE POLICY').pack()
        back = Button(root, text='BACK', command=self.insurance).pack()

    def buyins(self):
        self.destroy()
        buy1 = Label(root, text='AVAILABLE INSURANCE PLANS', font=('Arial', 30)).pack()
        ip = ['LIC Premier Health\nPremium = Rs.40,000\nCoverage Duration: 35 years',
              'Prudential Health Plus\nPremium = Rs.65,000\nCoverage Duration: 40 years',
              'GSK MediCare\nPremium = Rs.12,000\nCoverage Duration: 8 years',
              'TATA IG MaxHealth Plan\nPremium = Rs.8,000\nCoverage Duration: 4 years',
              'Apollo HealthCare Max\nPremium = Rs.31,000\nCoverage Duration: 20 years',
              'Max Life MediMax\nPremium = Rs.10,000\nCoverage Duration: 10 years']

        var = StringVar()
        var.set(None)

        for item in ip:
            button = Radiobutton(root, text=item, variable=var, value=item)
            button.pack(anchor=CENTER)

        buy = Button(root, text='BUY NOW',command=lambda:self.buynow(var.get())).pack()
        back = Button(root, text='BACK', command=self.insurance).pack()

    def insurance(self):
        self.destroy()
        insFrame = Frame(root).pack()
       
        insLabel = Label(insFrame, text="Insurance Options ", font=('Arial',25)).pack()
        bb3 = Button(insFrame, text='View current Insurance policies', padx=25, pady=25, command=self.currentinsurance)
        bb3.pack()
        bb4 = Button(insFrame, text='View other Insurance policies', padx=25, pady=25, command=self.buyins)
        bb4.pack()
        canvas= Canvas(insFrame, width= 300, height=100, bg="SpringGreen2")
        canvas2= Canvas(insFrame, width= 300, height=100, bg="blue")
        canvas.create_text(15, 15, text="AD1", fill="black", font=('Helvetica 15 bold'))
        canvas.pack(side='left')
        canvas2.create_text(15, 15, text="AD2", fill="black", font=('Helvetica 15 bold'))
        canvas2.pack(side='right')
        back = Button(root, text='BACK', command=self.loginehs).pack()
        
       
    def ewf(self):
        self.destroy()
        emerFrame = Frame(root).pack()
       
        emerLabel = Label(emerFrame, text="Emergency Welfare Fund ", font=('Arial',25)).pack()
        amount = Label(emerFrame,text='AVAILABLE BALANCE:\nRs. 3402.50').pack()

        canvas = Canvas(root, width=300, height=100, bg="SpringGreen2")
        canvas2 = Canvas(root, width=300, height=100, bg="blue")
        canvas.create_text(15, 15, text="AD1", fill="black", font=('Helvetica 15 bold'))
        canvas.pack(side='left')
        canvas2.create_text(15, 15, text="AD2", fill="black", font=('Helvetica 15 bold'))
        canvas2.pack(side='right')
        back = Button(root, text='BACK', command=self.loginehs).pack()
      
        
    def suggests(self):
        self.destroy()
        sugFrame = Frame(root).pack()

        sugLabel = Label(sugFrame, text="Customised suggestions ", font=('Arial',25)).pack()
        ehscurr = Label(sugFrame,text=f'Current UHID: {ehs.get()}').pack()
        canvas = Canvas(root, width=300, height=100, bg="SpringGreen2")
        canvas2 = Canvas(root, width=300, height=100, bg="blue")
        canvas.create_text(15, 15, text="AD1", fill="black", font=('Helvetica 15 bold'))
        canvas.pack(side='left')
        canvas2.create_text(15, 15, text="AD2", fill="black", font=('Helvetica 15 bold'))
        canvas2.pack(side='right')
        back = Button(root, text='BACK', command=self.loginehs).pack()
        
    def edits(self):
        self.destroy()
        edFrame = Frame(root).pack()
 
        ehsLabel = Label(edFrame, text="Profile Options and Settings changes", font=('Arial',25)).pack()
        ehscurr = Label(edFrame,text=f'UHID Number: {ehs.get()}').pack()
        aadharcurr = Label(edFrame,text=f'Aadhar number: {aadhar.get()}').pack()
        name = Label(edFrame,text=f'Name: {self.name}').pack()
        age = Label(edFrame, text=f'Age: {self.age}').pack()
        height = Label(edFrame, text=f'Height: {self.height} cm').pack()
        weight = Label(edFrame, text=f'Weight: {self.weight} kg').pack()

        canvas= Canvas(root, width= 300, height=100, bg="SpringGreen2")
        canvas2= Canvas(root, width= 300, height=100, bg="blue")
        canvas.create_text(15, 15, text="AD1", fill="black", font=('Helvetica 15 bold'))
        canvas.pack(side='left')
        canvas2.create_text(15, 15, text="AD2", fill="black", font=('Helvetica 15 bold'))
        canvas2.pack(side='right')
        back = Button(root, text='BACK', command=self.loginehs).pack()

    def loginehs(self):
        if ehs.get() == '' or ehs.get().isalpha():
            err = Label(root,text='INVALID EHS NUMBER').grid(row=2,column=0)
        elif aadhar.get() == '' or aadhar.get().isalpha():
            err = Label(root, text='INVALID AADHAR NUMBER').grid(row=2,column=0)
        else:
            self.destroy()

            logFrame = Frame(root).pack()
            bf = Frame(root).pack(side='bottom')
            canvas = Canvas(root, width=300, height=100, bg="SpringGreen2")
            canvas2 = Canvas(root, width=300, height=100, bg="blue")
            welcome = Label(root,text=f'Welcome {self.name}').pack()
            b1 = Button(logFrame, text='View Insurance Options', padx=25, pady=25, command=self.insurance)
            b1.pack()
            b2 = Button(logFrame, text='Emergency welfare fund', padx=25, pady=25, command=self.ewf)
            b2.pack()
            b3 = Button(logFrame, text='Customised suggestions', padx=25, pady=25, command=self.suggests)
            b3.pack()
            b4 = Button(logFrame, text='Edit Profile and settings', padx=25, pady=25, command=self.edits)
            b4.pack()
            canvas.create_text(15, 15, text="AD1", fill="black", font=('Helvetica 15 bold'))
            canvas.pack(side='left')
            canvas2.create_text(15, 15, text="AD2", fill="black", font=('Helvetica 15 bold'))
            canvas2.pack(side='right')

            back = Button(root, text='BACK', command=self.gen).pack()
       
    def gen(self):
        self.destroy()
        global ehs
        global aadhar
        ehsLabel = Label(root, text="Enter UHID Number", font=('Arial',25)).grid(row=0, column=0)
        ehs=StringVar()
        ehsEntry = Entry(root, textvariable=ehs).grid(row=0, column=1)

        aadharLabel = Label(root, text="Enter Aadhar Number", font=('Arial',25)).grid(row=1, column=0)
        aadhar= StringVar()
        aadharEntry = Entry(root, textvariable=aadhar).grid(row=1, column=1)
        loginButton=Button(root, text="Login",fg='blue', command=self.loginehs).grid(row=3, column=0)

        back = Button(root,text='BACK',command=self.__init__).grid(row=4,column=0)




root = Tk()
root.geometry('650x600')
root.title('FASTSOS')
obj = app()



