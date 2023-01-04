def AgeCalculator(Y,M, D):
    import datetime
    today=datetime.datetime.now().date()
    DOB=datetime.date(Y,M,D)
    Age=int((today-DOB).days/365.25)
    print("Your Age is:", Age)
Y=int(input("Enter your Birth Year:"))
M=int(input("Enter your Birth month(1-12):"))
D=int(input("Enter your Birth Date(1-31):"))
AgeCalculator(Y,M,D)

import



