import csv

def average(n):
    with open('sleepexport2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        L = [] 
        for row in readCSV:
                L.append(row[5])
        M = L[-n:]
        import statistics
        M = [float(x) for x in M]
        avg = statistics.mean(M)
        return avg
def age_and_sleep(age, avg):
    if age<=5 and age>0 and avg<12:
        print("You need to sleep more!")
    elif avg>=12 and avg<=15:
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
def ask_age():
    test = False
    while test == False:
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
def tester():
    tester = False
    while tester == False:
        try:
            n = int(input("Calculate average of the last how many days? "))
            if n <= 0:
                tester = False
                print("This is not a valid number.")
            else:
                tester = True
        except ValueError:
            print("That is not a valid number.")
            tester = False
    return n

age_and_sleep(ask_age(), average(tester()))
