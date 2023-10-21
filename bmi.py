def bmi(name, h, w):
    bmi = w/(h**2)
    if(bmi<18.5):
        result = "underweight"
    elif(bmi>=18.5 and bmi<=24.9):
        result = "healthy"
    elif(bmi>=25 and bmi<=29.9):
        result = "overweight"
    else:
        result = "super very much overweight"
    print('='*20)
    print("Hello, {}".format(name))
    print("Your BMI value is {:.2f} --> You are {}".format(bmi, result))
    print('='*20)
while True:
    mode = int(input("Enter Mode [Anonymous:0, Name:1, Exit:2]: "))
    if(mode==0):
        name = "Anonymous"
    elif(mode==1):
        name = input("Enter your name: ")
    elif (mode==2):
        break
    else:
        continue
    h = float(input("Enter your height(m): "))
    w = float(input("Enter your weight(kg): "))
    bmi(name, h, w)

