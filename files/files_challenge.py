import os


def main():
    totalbytes = 0

    # get a list of all files in current directory.
    dirlist = os.listdir()
    for eachFile in dirlist:
        # verify it's a file
        if os.path.isfile(eachFile):
            filesize = os.path.getsize(eachFile)
            totalbytes += filesize

    # make a new directory
    os.mkdir("../resultsdir")

    # create the output file
    resultsfile = open('../resultsdir/results.txt', 'w+')
    if resultsfile.mode == 'w+':
        resultsfile.write("Total bytecount:" + str(totalbytes) )
        resultsfile.write("Files list:\n")
        for entry in dirlist:
            resultsfile.write(entry + '\n')

        resultsfile.close()

if __name__ == '__main__':
    main()