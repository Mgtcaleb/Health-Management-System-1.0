#This is the code to execute simple data whiuch is based on food and exercise of individual person
#Author:Caleb Gore; Date of Code Creation: 11:50 A.M, 20.08.2020.
"""
Notes:
    1.Time stamp contains both number and : so predefine the data type as string
    2. It is important to import built-in function (datetime) so that we don't create another same function and waste time.
"""
#_______________________Part 2___________________________________
import datetime #datetime is built-in function
def gettime():#user has defined
    return datetime.datetime.now()
try:#to handle error
#_______________________Part 3.1___________________________________
    def logs(l):
        if l==1:
            a=int(input("Enter any one number below:\n 1-Exercise\n 2-Food\nEnter Here:"))
            if a==1:
                exercise1=input("Enter here:\n")
                with open("Caleb's Log.txt","a")as f:
                    a1=f.write(str([str(gettime())])+"\n"+"Exercise:"+exercise1+"\n")
                    print("Logged Successfully")
            elif a==2:
                food1=input("Enter Here:\n")
                with open("Caleb's Log.txt","a")as f:
                    a1 = f.write(str([str(gettime())])+"\n"+"Food:"+food1+"\n")
                    print("Logged Successfully")
        elif l==2:
            a = int(input("Enter any one number below:\n 1-Exercise\n 2-Food\n Enter Here:"))
            if a == 1:
                exercise1 = input("Enter here:\n")
                with open("Harry's Log.txt", "a")as f:
                    a1 = f.write(str([str(gettime())])+"\n"+"Exercise:"+ exercise1+"\n")
                    print("Logged Successfully")
            elif a==2:
                food1 = input("Enter Here:\n")
                with open("Harry's Log.txt", "a")as f:
                    a1 = f.write(str([str(gettime())]) +"\n"+"Food:"+ food1+"\n")
                    print("Logged Successfully")

    def retrive(r):
        if r==1:
             with open("Caleb's Log.txt") as f:
                    a1=f.read()
                    print(a1)
        elif r==2:
            with open("Harry's Log.txt") as f:
                     a1 = f.read()
                     print(a1)
    #_______________________Part 1___________________________________
    print("Current Timestamp:",gettime())
    #Front-end of the code, which user can see.
    print("Welcome to Health Management System: 1.0\n")
    a=int(input("Please enter the input\n 1-Log\n 2-Retrive\nEnter Here:"))
    if a==1:#since we provide two options 1-Log and 2-Retrive,hence developed condition statement.
        b=int(input("Please choose the number below to enter the log\n1-Caleb\n2-Harry\nEnter only number here:"))
        logs(b)#user defined function to enter the log in text file with time stamp.
    elif a==2:#if first condition is false (i.e. a==1) exceute second condition if it is true (i.e a==2)
        b=int(input("Please choose the number below to retrive the log\n1-Caleb\n2-Harry\nEnter only number here:"))
        retrive(b)#user defined function to retrive log with time stamp.
except Exception as e:
    print(e,"Kindly Restart the program because you have entered string or float")
