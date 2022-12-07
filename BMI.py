print("                                         Hello Mr/Mis i am Mohammadreza yaghoobi")
print(help)
print("Enter your height(M) : ")
# if  Height > 10:
#     ( Height / 100)

Height = input()
print("Enter your weight(KG) : ")
Weight = input()
BMI = (float(Weight) / float(Height)**2)
print("Your BMI : " , round(BMI,2))
if BMI > 30:
    print("Shoma kheili chagh hastid.")
elif 30>BMI>25:
    print("Shoma kami chagh hastid.")
elif 25>BMI>18.5:
    print("Vazn shoma GOOD hast.")
elif BMI < 18.5:
    print("shoma kheili laghar hastid.")