#import tkinter module
from tkinter import Tk, Label, Button, END, W, E, N, S, StringVar, IntVar
#import random module
import random
#import timeit module
import timeit

#create a new class
class Math:
    #define a constructor (__init__)
    def __init__(self,master):

        self.master=master              #set the value of self.master
        master.title("Math Is Easy")    #set the name of the GUI

        self.total=''           #default value of total (string)
        self.entered_number=0   #default value of entered number (integer)
        self.nentry=''          #default value of entered number (string)
        self.x = 0              #default vlaue of variable x (integer)
        self.greet1=''          #default value of variable greet1 (string)
        self.greet2=''          #default value of variable greet2 (string)

        self.r = 0
        self.w = 0
        self.df = ''
        
        #create and set the properties of every label   
        self.right_label=Label(master,text='Right:',font=('Comic Sans MS',10),bg='black',fg='white')
        self.wrong_label=Label(master,text='Wrong:',font=('Comic Sans MS',10),bg='black',fg='white')
       
        self.r_label_text=IntVar()
        self.r_label_text.set(self.r)
        self.r_label=Label(master,textvariable=self.r_label_text,font=('Comic Sans MS',10),bg='black',fg='white')

        self.w_label_text=IntVar()
        self.w_label_text.set(self.w)
        self.w_label=Label(master,textvariable=self.w_label_text,font=('Comic Sans MS',10),bg='black',fg='white')
        
        self.total_label_text=StringVar()
        self.total_label_text.set(self.total)
        self.total_label=Label(master,textvariable=self.total_label_text,width=13,justify='center',font=('Cambria Math',30,'bold'),bg='black',fg='white')

        self.label1=Label(master,text="\nMath Is Easy", font=('Comic Sans MS',20,'bold') , justify='center', bg='#ccd8ff')
        self.label2=Label(master,text='''In this simulator, there will be 5
problems for every round, including
addition, subtraction, or
multiplication between numbers.

Happy calculating!''', justify='center', font=('Comic Sans MS',12), bg='#ccd8ff')

        self.greet1_label_text=StringVar()
        self.greet1_label_text.set(self.greet1)
        self.greet1_label=Label(master,textvariable=self.greet1_label_text, font=('Comic Sans MS',20), justify='center', bg='#809dff')

        self.greet2_label_text=StringVar()
        self.greet2_label_text.set(self.greet2)
        self.greet2_label=Label(master,textvariable=self.greet2_label_text, font=('Comic Sans MS',12), justify='center', bg='#809dff')

        self.emptylabel1=Label(master,text='', width = 2, bg='#ccd8ff')
        self.emptylabel2=Label(master,text='', width = 2, bg='#ccd8ff')
        self.emptylabel3=Label(master,text='', width = 2, bg='#ccd8ff')
        self.emptylabel4=Label(master,text='', width = 2, bg='#ccd8ff')
        self.emptylabel5=Label(master,text='', width = 2, bg='#ccd8ff')
        self.emptylabel6=Label(master,text='', width = 2, bg='#809dff')
        self.emptylabel7=Label(master,text='', width = 2, bg='#ccd8ff')
    
        self.entry_label_text=StringVar()
        self.entry_label_text.set(self.nentry)
        self.entry=Label(master, textvariable=self.entry_label_text, font=('Arial', 20, 'bold'), justify='center', bg='white')
        
        #create and set the properties of every button (number and operator)
        self.one=Button(master,text="1",font=('Arial',18,'bold'), width = 3, bg='#809dff', command=lambda:self.validate(1))
        self.two=Button(master,text="2",font=('Arial',18,'bold'), width = 3, bg='#809dff',command=lambda:self.validate(2))    
        self.three=Button(master,text="3",font=('Arial',18,'bold'), width = 3, bg='#809dff',command=lambda:self.validate(3))  
        self.four=Button(master,text="4",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(4))   
        self.five=Button(master,text="5",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(5))  
        self.six=Button(master,text="6",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(6))    
        self.seven=Button(master,text="7",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(7))  
        self.eight=Button(master,text="8",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(8))  
        self.nine=Button(master,text="9",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(9))   
        self.zero=Button(master,text="0",font=('Arial',18,'bold'), bg='#809dff',command=lambda:self.validate(0))
        self.submit_button=Button(master,text="Enter",font=('Arial',13,'bold'), bg='#809dff',command=lambda:self.update("submit"))
        self.delete_button=Button(master,text="Del",font=('Arial',13,'bold'), bg='#809dff',command=lambda:self.update("delete"))
        self.reset_button=Button(master,text="RESET",font=('Arial',13,'bold'), bg='#809dff',command=lambda:self.update("reset"))
        self.start_button=Button(master,text="START",font=('Arial',13,'bold'), bg='#809dff',command=lambda:self.initnumber(0))
        self.minus_button=Button(master,text='-',font=('Arial',18,'bold'), width = 4, bg='#809dff',command=lambda:self.validate('-'))

        self.easy_button=Button(master,text='Easy',font=('Arial',11,'bold'), width = 4, bg='#809dff',command=lambda:self.level('easy'))
        self.medium_button=Button(master,text='Medium',font=('Arial',11,'bold'), width = 4, bg='#809dff',command=lambda:self.level('medium'))
        self.hard_button=Button(master,text='Hard',font=('Arial',11,'bold'), width = 4, bg='#809dff',command=lambda:self.level('hard'))
        self.q_button=Button(master,text='?',font=('Arial',11,'bold'), width = 4, bg='#809dff',command=lambda:self.level('question'))
        
        #set the position of every label
        self.label1.grid(row=1,column=1,columnspan=4, sticky=W+E+N+S)
        self.label2.grid(row=2,column=1,columnspan=4, rowspan=3, sticky=W+E+N+S)
        
        self.emptylabel1.grid(row=0, column=0, columnspan=16, sticky=W+E+N+S)
        self.emptylabel2.grid(row=0, column=5, rowspan=6, sticky=W+E+N+S)
        self.emptylabel3.grid(row=0, column=10, rowspan=6, sticky=W+E+N+S)
        self.emptylabel4.grid(row=0, column=15, rowspan=6, sticky=W+E+N+S)
        self.emptylabel5.grid(row=6, column=0, columnspan=16, sticky=W+E+N+S)
        self.emptylabel6.grid(row=7, column=0, columnspan=16, sticky=W+E+N+S)
        self.emptylabel7.grid(row=0, column=0, rowspan=6, sticky=W+E+N+S)

        self.total_label.grid(row=1, column=6, columnspan=4, rowspan = 3, sticky=W+E+N+S)

        self.right_label.grid(row=4, column=6, sticky=W+E+N+S)
        self.wrong_label.grid(row=4, column=8, sticky=W+E+N+S)
        self.r_label.grid(row=4, column=7, sticky=W+E+N+S)
        self.w_label.grid(row=4, column=9, sticky=W+E+N+S)
        
        self.greet1_label.grid(row=8,column=0,columnspan=16, sticky=W+E+N+S)
        self.greet2_label.grid(row=9,column=0,columnspan=16, sticky=W+E+N+S)
        self.entry.grid(row=1,column=11,columnspan=4, sticky=W+E+N+S)

        #set the position of every button (number and operator)
        self.submit_button.grid(row=4,column=14, rowspan=2, sticky=W+E+N+S)
        self.delete_button.grid(row=3,column=14, sticky=W+E+N+S)
        self.reset_button.grid(row=5,column=8,columnspan=2, sticky=W+E+N+S)
        self.one.grid(row=2,column=11, sticky=W+E+N+S)
        self.two.grid(row=2,column=12, sticky=W+E+N+S)
        self.three.grid(row=2,column=13, sticky=W+E+N+S)
        self.four.grid(row=3,column=11, sticky=W+E+N+S)
        self.five.grid(row=3,column=12, sticky=W+E+N+S)
        self.six.grid(row=3,column=13, sticky=W+E+N+S)
        self.seven.grid(row=4,column=11, sticky=W+E+N+S)
        self.eight.grid(row=4,column=12, sticky=W+E+N+S)
        self.nine.grid(row=4,column=13, sticky=W+E+N+S)
        self.zero.grid(row=5,column=11, columnspan=3, sticky=W+E+N+S)
        self.start_button.grid(row=5,column=6,columnspan=2, sticky=W+E+N+S)
        self.minus_button.grid(row=2,column=14, sticky=W+E+N+S)

        self.easy_button.grid(row=5, column=1, sticky=W+E+N+S)
        self.medium_button.grid(row=5, column=2, sticky=W+E+N+S)
        self.hard_button.grid(row=5, column=3, sticky=W+E+N+S)
        self.q_button.grid(row=5, column=4, sticky=W+E+N+S)

    def level(self,h):
        if h == 'easy':
            self.df = 'Easy'
            self.greet1='Easy'
            self.greet2=''
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            self.nentry = ''                        #clear the value of nentry
            self.total = ''                         #clear the value of total
            self.total_label_text.set(self.total)   #set the text of total label
            self.entry_label_text.set(self.nentry)
            
        elif h == 'medium':
            self.df = 'Medium'
            self.greet1='Medium'
            self.greet2=''
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            self.nentry = ''                        #clear the value of nentry
            self.total = ''                         #clear the value of total
            self.total_label_text.set(self.total)   #set the text of total label
            self.entry_label_text.set(self.nentry)
            
        elif h == 'hard':
            self.df = 'Hard'
            self.greet1='Hard'
            self.greet2=''
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            self.nentry = ''                        #clear the value of nentry
            self.total = ''                         #clear the value of total
            self.total_label_text.set(self.total)   #set the text of total label
            self.entry_label_text.set(self.nentry)
            
        else:
            self.greet1='Description'
            self.greet2='''Easy: equation between two numbers range from 0-10
Medium: equation between two numbers range from 11-20
Hard: equation between two numbers range from 21-30\n'''
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            self.nentry = ''                        #clear the value of nentry
            self.total = ''                         #clear the value of total
            self.total_label_text.set(self.total)   #set the text of total label
            self.entry_label_text.set(self.nentry)
        self.greet1_label_text.set(self.greet1)
        self.greet2_label_text.set(self.greet2)
            
        
    #define a function    
    def initnumber(self,x):
        if self.df == 'Easy':
            self.start = timeit.default_timer() #start the timer
            self.a = str(random.randint(0,10))  #random a number between 0-10
            self.b = '+','-','*'                #set the operand options
            self.c = str(random.randint(0,10))  #random a number between 0-10
            self.d = random.choice(self.b)      #random the operands
            self.e = self.a+self.d+self.c       #combine the random number and operand
            self.total = self.e                 #set the value of self.total

            self.x=0                                #set the value of x (zero iteration)
            self.total_label_text.set(self.total)   #set the text of total label
            self.nentry=''                          #set the value of nentry
            self.entry_label_text.set(self.nentry)  #set the text of entry label
            self.greet1='Easy'                          #set the value of greet1
            self.greet1_label_text.set(self.greet1) #set the text of greet1 label
            self.greet2=''                          #set the value of greet2
            self.greet2_label_text.set(self.greet2) #set the text of greet2 label
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            
        elif self.df == 'Medium':
            self.start = timeit.default_timer() #start the timer
            self.a = str(random.randint(11,20))  #random a number between 0-10
            self.b = '+','-','*'                #set the operand options
            self.c = str(random.randint(11,20))  #random a number between 0-10
            self.d = random.choice(self.b)      #random the operands
            self.e = self.a+self.d+self.c       #combine the random number and operand
            self.total = self.e                 #set the value of self.total

            self.x=0                                #set the value of x (zero iteration)
            self.total_label_text.set(self.total)   #set the text of total label
            self.nentry=''                          #set the value of nentry
            self.entry_label_text.set(self.nentry)  #set the text of entry label
            self.greet1='Medium'                          #set the value of greet1
            self.greet1_label_text.set(self.greet1) #set the text of greet1 label
            self.greet2=''                          #set the value of greet2
            self.greet2_label_text.set(self.greet2) #set the text of greet2 label
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            
        elif self.df == 'Hard':
            self.start = timeit.default_timer() #start the timer
            self.a = str(random.randint(21,30))  #random a number between 0-10
            self.b = '+','-','*'                #set the operand options
            self.c = str(random.randint(21,30))  #random a number between 0-10
            self.d = random.choice(self.b)      #random the operands
            self.e = self.a+self.d+self.c       #combine the random number and operand
            self.total = self.e                 #set the value of self.total

            self.x=0                                #set the value of x (zero iteration)
            self.total_label_text.set(self.total)   #set the text of total label
            self.nentry=''                          #set the value of nentry
            self.entry_label_text.set(self.nentry)  #set the text of entry label
            self.greet1='Hard'                          #set the value of greet1
            self.greet1_label_text.set(self.greet1) #set the text of greet1 label
            self.greet2=''                          #set the value of greet2
            self.greet2_label_text.set(self.greet2) #set the text of greet2 label
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            
        else:
            self.x=0                                #set the value of x (zero iteration)
            self.total_label_text.set(self.total)   #set the text of total label
            self.nentry=''                          #set the value of nentry
            self.entry_label_text.set(self.nentry)  #set the text of entry label
            self.greet1=''                          #set the value of greet1
            self.greet1_label_text.set(self.greet1) #set the text of greet1 label
            self.greet2=''                          #set the value of greet2
            self.greet2_label_text.set(self.greet2) #set the text of greet2 label
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)

    #define a function        
    def randomnumber(self,x):
        #create a control statement (if iteration is lower than 5 times)
        if self.df == 'Easy':
            if x<5:
                self.a = str(random.randint(0,10))  #random a number between 0-10
                self.b = '+','-','*'                #set the operand options
                self.c = str(random.randint(0,10))  #random a number between 0-10
                self.d = random.choice(self.b)      #random the operands
                self.e = self.a+self.d+self.c       #combine the random number and operand
                self.total = self.e                 #set the value of self.total
                self.greet1='Easy'                          #set the value of greet1
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2=''                          #clear the value of greet2
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            #create a control statement (if iteration is equal to 5)
            elif x==5:
                self.stop = timeit.default_timer()      #stop the timer
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.settime=str(round(self.stop-self.start,2))                                         #calculate the calculation time
                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            else:
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
        elif self.df == 'Medium':
            if x<5:
                self.a = str(random.randint(11,20))  #random a number between 0-10
                self.b = '+','-','*'                #set the operand options
                self.c = str(random.randint(11,20))  #random a number between 0-10
                self.d = random.choice(self.b)      #random the operands
                self.e = self.a+self.d+self.c       #combine the random number and operand
                self.total = self.e                 #set the value of self.total
                self.greet1='Medium'                          #set the value of greet1
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2=''                          #clear the value of greet2
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            #create a control statement (if iteration is equal to 5)
            elif x==5:
                self.stop = timeit.default_timer()      #stop the timer
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.settime=str(round(self.stop-self.start,2))                                         #calculate the calculation time
                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            else:
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
        elif self.df == 'Hard':
            if x<5:
                self.a = str(random.randint(21,30))  #random a number between 0-10
                self.b = '+','-','*'                #set the operand options
                self.c = str(random.randint(21,30))  #random a number between 0-10
                self.d = random.choice(self.b)      #random the operands
                self.e = self.a+self.d+self.c       #combine the random number and operand
                self.total = self.e                 #set the value of self.total
                self.greet1='Hard'                          #set the value of greet1
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2=''                          #clear the value of greet2
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            #create a control statement (if iteration is equal to 5)
            elif x==5:
                self.stop = timeit.default_timer()      #stop the timer
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.settime=str(round(self.stop-self.start,2))                                         #calculate the calculation time
                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
                
            else:
                self.total = ''                         #clear the value of total
                self.nentry = ''                        #clear the value of nentry
                self.entry_label_text.set(self.nentry)  #set the text of entry label

                self.greet1 = "Good Job!"                                                             #set the value of greet1
                self.greet2 = "Your calculation time: "+self.settime+" seconds"+"\nKeep practicing!\n"  #set the value of greet2
            
                self.greet1_label_text.set(self.greet1) #set the text of greet1 label
                self.greet2_label_text.set(self.greet2) #set the text of greet2 label
        else:
            self.total=''
            
        self.total_label_text.set(self.total)   #set the text of total label
        
    #define a function when number or minus buttons are clicked
    def validate(self,new_text):
        if new_text == '-':                         #if the clicked button is minus button
            self.nentry += str(new_text)            #update the value of entered number
            self.entry_label_text.set(self.nentry)  #update the text of entry label
        else:
            self.nentry += str(new_text)            #update the value of entered number (string)
            self.entered_number = int(self.nentry)  #update the value of entered number (integer)
            self.entry_label_text.set(self.nentry)  #update the text of entry label
     
    #define a function when operator buttons are clicked    
    def update(self, method):
        if method == "submit":              #if submit button is clicked
            try:
                if self.d == '+':                               #if the operand is plus
                    self.total = int(self.a) + int(self.c)      #add the two random numbers
                    #if the value of total is equal with the number that is inputted by the user
                    if self.total == int(self.entered_number):  
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.randomnumber(self.x+1)     #move to the next problem
                            self.nentry=''                  #clear the value of nentry
                            self.x = self.x+1               #add the value of x by one after every iteration
                            self.r = self.r+1
                            self.w = self.w
                                                
                    else:
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.nentry=''                  #if the answer is wrong, clear the value of nentry
                            self.w = self.w+1
                            self.r = self.r
                        
                if self.d == '-':                               #if the operand is minus
                    self.total = int(self.a) - int(self.c)      #subtract the two random numbers
                    #if the value of total is equal with the number that is inputted by the user
                    if self.total == int(self.entered_number):
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.randomnumber(self.x+1)     #move to the next problem
                            self.nentry=''                  #clear the value of nentry
                            self.x = self.x+1               #add the value of x by one after every iteration
                            self.r = self.r+1
                            self.w = self.w
                        
                    else:
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.nentry=''                  #if the answer is wrong, clear the value of nentry
                            self.w = self.w+1
                            self.r = self.r
                        
                if self.d == '*':                               #if the operand is star (multiplication)
                    self.total = int(self.a) * int(self.c)      #multiply the two random numbers
                    if self.total == int(self.entered_number):
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.randomnumber(self.x+1)     #move to the next problem
                            self.nentry=''                  #clear the value of nentry
                            self.x = self.x+1               #add the value of x by one after every iteration
                            self.r = self.r+1
                            self.w = self.w
                        
                    else:
                        if self.greet2 != '':
                            self.nentry=''
                            self.w = self.w
                            self.r = self.r
                        elif self.nentry == '':
                            self.w = self.w
                            self.r = self.r
                        else:
                            self.nentry = ''                  #if the answer is wrong, clear the value of nentry
                            self.w = self.w+1
                            self.r = self.r
                else:
                    self.nentry = ''
                    self.w = self.w
                    self.r = self.r
                      
                self.r_label_text.set(self.r)
                self.w_label_text.set(self.w)

            #create an exception handler if there is an Attribute Error
            except AttributeError:
                self.nentry=''                          #clear the value of nentry
                self.w = self.w
                self.r = self.r
                self.r_label_text.set(self.r)
                self.w_label_text.set(self.w)
                
        if method == 'delete':              #if delete button is clicked
            try:
                self.nentry = list(self.nentry)         #change the equation into a list 
                del self.nentry[-1]                     #delete the last character
                self.nentry = ''.join(self.nentry)      #re-join all characters in the list
                self.entered_number = int(self.nentry)  #update the value of entered_number

            #create an exception handler if there is an Index Error or Value Error
            except (IndexError, ValueError):
                self.nentry=''              #clear the value of nentry

        if method == 'reset':                       #if reset button is clicked
            self.nentry = ''                        #clear the value of nentry
            self.total = ''                         #clear the value of total
            self.total_label_text.set(self.total)   #set the text of total label
            self.greet1=''                          #clear the value of greet1
            self.greet1_label_text.set(self.greet1) #set the text of greet1 label
            self.greet2=''                          #clear the value of greet2
            self.greet2_label_text.set(self.greet2) #set the text of greet2 label
            self.w = 0
            self.r = 0
            self.r_label_text.set(self.r)
            self.w_label_text.set(self.w)
            self.df = ''

        self.entry_label_text.set(self.nentry)  #update the text of entry label

root=Tk()                                   #create an tk/tcl interpreter
my_gui=Math(root)                           #set the root as parameter of the class
root.resizable(width=False, height=False)   #the calculator cannot be resized
root.mainloop()                             #the code loops until the window is closed

#References
#Code Review. (2016). Python Calculator using tkinter. [Online] Retrieved from https://codereview.stackexchange.com/questions/141633/python-calculator-using-tkinter [Accessed 19 December 2017].
#Stack Overflow. (2014). What does calling Tk() actually do?. [Online] Retrieved from https://stackoverflow.com/questions/24729119/what-does-calling-tk-actually-do [Accessed 19 December 2017].
