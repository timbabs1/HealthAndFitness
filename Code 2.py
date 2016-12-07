"""This first part of the code imports the csv file and creates arrays so that we don't need to import the file multiple times"""
import csv              #Import the csv module
import statistics       #Import the statistics module
with open('sleepexport2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        L1 = []
        L2 = []
        for row in readCSV:
                L1.append(row[5])
                L2.append(row[11])
        L3 = tuple(L1)
        L4 = tuple(L2)
        
"""This function calculates the average of the sleeping hours for the last x number of days""" 
def average(n):
        M1 = L3[-n:]                    #This subtracts the number of days required from the specific array
        M1 = [float(x) for x in M1]     #Shows the use of for loop statements
        avg = statistics.mean(M1)       #This uses the statitics module which we imported to calculate the mean value
        return avg                      #This returns the average

"""This function calculates the heartrate average for the last y number of days"""     
def heartrate(m):
        M2 = L4[-m:]
        M2 = [float(x) for x in M2]     #This line of codes means to turn the values of M2 to floats
        avgh = statistics.mean(M2)
        return avgh
"""This function calculates the BMI of the user based on the values he enters"""
def BMI(mass, height):
    bmin = mass / (height)**2
    return bmin

def BMIRec(bmi):
    if bmi>=25 and bmi<29:
        print("You are overweight. Need more Gym!")
    elif bmi<18.5:
        print("You are underweight. Eat more!")
    elif bmi>=18.5 and bmi<24.9:
        print("This is considered healthy")
    elif bmi>30:
        print("You are obese my friend")

"""This function classifies the different ranges of your heart rate and tells you if heeart rate recorded over time is healthy or not"""
def heartrec(avgh):
    if avgh<50:
        print("Your heartrate is very low")
    elif avgh>=50 and avgh<=80:
        print("You are quite relaxed during your sleep")
    elif avgh>80:
        print("Your heartrate is very high! You are too stressed.")

def age_and_sleep(age, avg):
    if age<=5 and age>0 and avg<12:                     #The if statement which states calculates the paremeters and prints the output based on them
        print("You need to sleep more!")
    elif avg>=12 and avg<=15:                           #Also shows the use of the if statements
        print("You slept enough this week!")
    elif avg>15:
        print("You are oversleeping!")
    elif age>5 and age<=13 and avg<9:
        print("You need to sleep more!")
    elif avg>=9 and avg<=11:
        print("You slept enough this week!")
    elif avg>11:
        print("You are oversleeping!")
    elif age>13 and age<=18 and avg<8:
        print("You need to sleep more!")
    elif avg>=8 and avg<=10:
        print("You slept enough this week!")
    elif avg>10:
        print("You are oversleeping!")
    elif age>18 and age<=25 and avg<7:
        print("You need to sleep more!")
    elif avg>=7 and avg<=9:
        print("You slept enough this week!")
    elif avg>9:
        print("You are oversleeping!")
    elif age>25 and age<=110 and avg<7:
        print("You need to sleep more!")
    elif avg>=7 and avg<=8:
        print("You slept enough this week!")
    elif avg>8:
        print("You are oversleeping!")

"""This function makes sure that the user doesn't input an invalid age number"""
def ask_age():
    test = False
    while test == False:                        #Shows the use of while loops
        try:
            age = int(input("Enter your age: "))
            if age <= 0 or age >= 110:
                test = False
                print("Please enter a valid age! ")
            else:
                test = True
        except ValueError:
            print("This is not a number! ")
            test = False
    return age

"""The next 4 functions make sure that the user can't input an invalid number of days"""
def datainput1():
    tester = False
    while tester == False:
        try:
            n = int(input("Calculate sleep hours average of the last how many days? "))
            if n <= 0 or n>20:
                tester = False
                print("This is not a valid number.")
            else:
                tester = True
        except ValueError:
            print("That is not a valid number.")
            tester = False
    return n

def datainput2():
    tester = False
    while tester == False:
        try:
            m = int(input("Calculate heartrate average of the last how many days? "))
            if m <= 0 or m>20:
                tester = False
                print("This is not a valid number.")
            else:
                tester = True
        except ValueError:
            print("That is not a valid number.")
            tester = False
    return m
def datainput3():
        tester = False
        while tester == False:
            try:
                    mass = int(input("What is user mass in kg? "))              #This is the input function that accepts only ints
                    if mass <= 0 or mass>110:
                            tester = False
                            print("Enter a valid mass")
                    else:
                            tester = True
            except ValueError:
                    print("Enter a valid number")
                    tester = False
        return mass

def datainput4():
        tester = False
        while tester == False:
                try:
                        height = float(input("What is user height in meters? "))
                        if height <= 0 or height>2.72:
                                tester = False
                                print("This is not a valid height ")
                        else:
                                tester = True
                except ValueError:
                    print("Enter a valid number")
                    tester = False
        return height
"""This is a class for the age groups"""
class agegroup:
        def __init__(self, name, age):
                self.name = name
                self.age = age
"""This is the primary class"""
class primary(agegroup):
        def group(self):
            if self.age>0 and self.age<15:
                        return "You are a primary"
            elif self.age>15:
                        return("Move onto the next group please!")

"""This is the adolescent classes and its different attributes"""
class adolescent(agegroup):
        def group(self):
            if self.age>15 and self.age<20:
                        return "You are an adolescent"
            elif self.age>20:
                        return("Move onto the next group please!")
"""This is the adult agegroup"""
class adult(agegroup):
        def group(self):
            if self.age>20 and self.age<65:
                        return "You are an adult"
            elif self.age>65:
                        return("Move onto the next group please!")
"""This is the elderly agegroup"""
class elderly(agegroup):
        def group(self):
            if self.age>65 and self.age<110:
                return "You are an elderly"
            elif self.age>20:
                return("Move onto the next group please!")
    
"""These are the function calls"""
age_and_sleep(ask_age(), average(datainput1()))
heartrec(heartrate(datainput2()))
BMIRec(BMI(datainput3(), datainput4()))
