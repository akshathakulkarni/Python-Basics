def main():
    # Open a file for writing and create if it doesn't exist
    # myfile = open('textfile.txt', "w+")

    # Open a file for appending text to the end
    # myfile = open('textfile.txt', 'a+')

    # write some data to the file-write 10 lines of text
    # for i in range(10):
    #   myfile.write("This is some new text\n")

    # Close the file
    # myfile.close()

    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        # contents = myfile.read()
        # print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)

if __name__ == '__main__':
    main()