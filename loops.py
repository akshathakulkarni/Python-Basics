def main():
    x = 0

    # while loop
    while(x < 5):
        print(x)
        x = x + 1

    # for loop
    for x in range(5, 10):
        print(x)

    # for loop over a collection\
    days = ["Monday", "Tuesday", "Wednesday"]
    for d in days:
        print(d)

    for x in range(5, 10):
        # if x == 7:
        #     break
        if x % 2 == 0:
           continue
        print(x)

    # enumerate() function
    days = ["Monday", "Tuesday", "Wednesday"]
    for i,d in enumerate(days):
        print(i,d)




    return x

main()