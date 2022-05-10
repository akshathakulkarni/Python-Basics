# Exceptional handling

try:
    x = 10 / 0
except:
    print("Can't divide number by 0")

try:
    answer = input('What should I divide 10 by?')
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by 0")
except ValueError as e:
    print("You didn't enter a valid number")
    print(e)
finally:
    print("This code always runs")

