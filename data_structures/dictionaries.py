def main():
    myDict = {'a': 1, 'b': 2}
    myDict['c'] = 3
    print('d' in myDict)
    print(myDict.get('a'))
    for item in myDict:
        print(item)

if __name__ == '__main__':
    main()