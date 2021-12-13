print("Hey User")
b = int(input("Enter your age or year of birth."))
if b < 150:
    b = 2021 - b
a = int(input("Do you want to know the year when you will turn 100? if yes enter 1, if no enter 2."))

if a == 1:

    if b < 2021 and b >= 1921:
        d = b + 100
        print("You will turn 100 in year,",d)
    if b <= 1921:
        print("Hey! you seems to be the oldest human alive.")

    if b > 2021:
        print("Hey! Unborn child")
elif a == 2:
    print("Come on user! Be exited about your century.")
else:
    print("Invalid input. Are you kidding with me.")
