print ("Enter marks obtained in 5 subjects:")
Coding = int(input("Coding:"))
Maths = int(input("Maths:"))
Physics = int(input("Physics:"))
Chemistry = int(input("Chemistry:"))
English = int(input("English:"))
Total = Coding + Maths + Physics + Chemistry + English
Average = Total / 5

if Average >= 90 and Average <= 100:
    Grade = 'A'
elif Average >= 80 and Average < 90:
    Grade = 'B'
elif Average >= 70 and Average < 80:
    Grade = 'C'
elif Average >= 60 and Average < 70:
    Grade = 'D'
elif Average >= 40 and Average < 60:
    Grade = 'E'
else:
    Grade = 'F'
print("Your Grade is:", Grade)
