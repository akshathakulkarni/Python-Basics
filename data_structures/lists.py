# lists is an ordered collection - its iterable and mutable
def main():
    myList = [1, 2, 3, 4, 5]
    print(myList[1:4:2])
    myList.append('6')
    myList.insert(0, '0')
    myList.pop(2)
    del myList[1:3:2]
    for i in myList:
        print('List elements are : ', i)


if __name__ == '__main__':
    main()


