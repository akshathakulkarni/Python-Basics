def palindromecheck(testinput):
    reversedvalue = testinput[::-1]

    if testinput == reversedvalue:
        print("True")
    else:
        print("False")


run = True

while (run):
    userinput = input("Please enter a value or type exit: ")
    if userinput == "exit":
        run = False
        break
    else:
        # convert to lowercase
        lowercaseinput = userinput.lower()
        # stripe out all spaces and punctuations
        testinput = ''
        for x in lowercaseinput:
            if x.isalnum():
                testinput += x

        palindromecheck(testinput)
