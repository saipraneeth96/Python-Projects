# LOVE CALCULATOR

name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")

name = name1 + name2

lower_case_string = name.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l+o+v+e

love_score = str(true) + str(love)

if 10 > int(love_score) > 90:
    print(f"Your score is {love_score}")
    print("YOU GO TOGETHER LIKE COKE AND MENTOS")
elif 40 <= int(love_score) <= 50:
    print(f"Your score is {love_score}")
    print("YOU ARE ALRIGHT TOGETHER")
else:
     print(f"Your score is {love_score}")
