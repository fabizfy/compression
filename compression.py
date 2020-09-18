import csv


def main():
    # convert to 0's and 1's from unsorted file
    bitmap('animals.txt', 'unsorted_Animals_Bits.txt')
    # sorts the animals
    sortingAnimals('animals.txt', 'sorted_Animals.txt')
    # convert to 0's and 1's from sorted file
    bitmap('sorted_Animals.txt', 'sorted_Animals_Bits.txt')
    # reads through the columns from sorted file
    columns('sorted_Animals_Bits.txt', 'Ucolumn_sorted.txt')
    # reads through the columns from unsorted file
    columns('unsorted_Animals_Bits.txt', 'Ucolumn_unsorted.txt')
    # reads through the sorted column and do 32bit compression
    compress32('Ucolumn_sorted.txt', 'Ucompressed_sorted32.txt')
    # reads through the unsorted column and do 32bit compression
    compress32('Ucolumn_unsorted.txt', 'Ucompressed_unsorted32.txt')
    # reads through the sorted column and do 64bit compression
    compress64('Ucolumn_sorted.txt', 'Ucompressed_sorted64.txt')
    # reads through the unsorted column and do 64bit compression
    compress64('Ucolumn_unsorted.txt', 'Ucompressed_unsorted64.txt')


def bitmap(rd, wrt):  # checks the content on file and will generate the bitmap
    with open(rd) as f:
        content = list(csv.reader(f))
        # checks if file is on system, if not it creates it
        file = open(wrt, 'a')
        file.seek(0)  # beggining of file
        file.truncate()  # erases the data

        flagLine = 0

        for i in range(len(content)):  # flag will be 1 after and will be added
            if flagLine == 1:
                file.write("\n")
            flagLine = 1

            if 'cat' in content[i]:  # check if is cat
                # print(content[i])
                # print("1000")
                file.write("1000")  # write this to file

            if 'dog' in content[i]:  # check if is dog
                # print(content[i])
                # print("0100")
                file.write("0100")  # write this to file

            if 'turtle' in content[i]:  # check if is turtle
                # print(content[i])
                # print("0010")
                file.write("0010")  # write this to file

            if 'bird' in content[i]:  # check if is bird
                # print(content[i])
                # print("0001")
                file.write("0001")  # write this to file

            age = int(content[i][1])

            # the if statements will check the age number and will
            # deterfiles which bit to set to 1 and write into the file
            if 0 < age and age < 11:
                # print(age)
                file.write("1000000000")
            if 10 < age and age < 21:
                # print(age)
                file.write("0100000000")
            if 20 < age and age < 31:
                # print(age)
                file.write("0010000000")
            if 30 < age and age < 41:
                # print(age)
                file.write("0001000000")
            if 40 < age and age < 51:
                # print(age)
                file.write("0000100000")
            if 50 < age and age < 61:
                # print(age)
                file.write("0000010000")
            if 60 < age and age < 71:
                # print(age)
                file.write("0000001000")
            if 70 < age and age < 81:
                # print(age)
                file.write("0000000100")
            if 80 < age and age < 91:
                # print(age)
                file.write("0000000010")
            if 90 < age and age < 101:
                # print(age)
                file.write("0000000001")

            # check the true or false statements
            if 'True' in content[i][2]:
                # print("10")
                file.write("10")
            if 'False' in content[i][2]:
                # print("01")
                file.write("01")

            i += 1


def sortingAnimals(rd, wrt):
    with open(rd) as f:  # reads from file
        oldLines = f.readlines()  # reads line by line
        files = open(wrt, 'a')  # creates/open file
        # print(oldLines)
        files.seek(0)  # beggining of file
        files.truncate()  # erases the data
        oldLines.sort()  # sorts the data

        for i in range(len(oldLines)):  # writes to the file sorted
            files.write(oldLines[i])


def columns(rd, wrt):
    with open(rd) as f:  # reads from file
        oldLines = f.readlines()  # reads line by line
        # print(oldLines)
        files = open(wrt, 'a')  # creates/open file
        files.seek(0)  # beggining of file
        files.truncate()  # erases the data

        firstline = True

        for j in range(0, 16):  # loop through my columns

            flag = 0

            for i in range(len(oldLines)):

                if flag % 31 == 0 and firstline == False:  # check to add new line and reads 31 bits
                    files.write("\n")

                if(oldLines[i][j]):  # writes what was read through the columns
                    files.write(oldLines[i][j])

                firstline = False

                flag = flag + 1


def compress32(rd, wrt):
    compressed = ""
    with open(rd) as f:  # reads from file
        oldLines = f.readlines()
        # print(oldLines)
        files = open(wrt, 'a')  # creates/open file
        files.seek(0)  # beggining of file
        files.truncate()  # erases the data

        lineCount = 0
        runCount = 0
        litCount = 0

        lastWasZero = True  # a flag
        # print(len(oldLines))
        for i in range(len(oldLines)):  # writes to the file sorted`
            # check if is a run
            # comparing the strings in file
            if (oldLines[i] == "0000000000000000000000000000000\n"):

                if (lastWasZero == False and lineCount > 0):  # checks if is a run of 1's

                    compressed += "11" + bin(lineCount)[2:].zfill(30)
                    # lineCount = 0

                lastWasZero = True
                lineCount += 1  # increments count if it's a run
                #runCount += 1
                # print("Run0#:", runCount)

            elif (oldLines[i] == "1111111111111111111111111111111\n"):

                if (lastWasZero == True and lineCount > 0):  # checks if is a run of 0's
                    compressed += "10" + bin(lineCount)[2:].zfill(30)
                    # lineCount = 0

                lineCount += 1
                lastWasZero = False
                #runCount += 1
                # print("Run1#:", runCount)
            else:  # checks for literal
                # print(oldLines[i])
                if (lineCount > 0):
                    #runCount += 1
                    compressed += "1" + \
                        ("0" if lastWasZero else "1") + \
                        bin(lineCount)[2:].zfill(
                            30)  # add the zero or 1 and fill the rest

                    #lineCount = 0

                # add the zero and copy the string without newline
                compressed += "0" + oldLines[i].rstrip('\n')
                # print(compressed)

            # print("Run#:", runCount)

        if (lineCount > 0):
            #litCount += 1
            compressed += "1" + \
                ("0" if lastWasZero else "1") + bin(lineCount)[2:].zfill(30)
        else:
            compressed += "0" + oldLines[i]

        #print("literals:", litCount)

        files.write(compressed)


def compress64(rd, wrt):
    compressed = ""
    with open(rd) as f:  # reads from file
        oldLines = f.readlines()
        # print(oldLines)
        files = open(wrt, 'a')  # creates/open file
        files.seek(0)  # beggining of file
        files.truncate()  # erases the data

        lineCount = 0
        lastWasZero = True  # a flag
        # print(len(oldLines))
        for i in range(len(oldLines)):  # writes to the file sorted`
            # check if is a run
            # comparing the strings in file
            if (oldLines[i] == "0000000000000000000000000000000\n"):

                if (lastWasZero == False and lineCount > 0):  # checks if is a run of 1's
                    compressed += "11" + bin(lineCount)[2:].zfill(62)
                    # lineCount = 0

                lastWasZero = True
                lineCount += 1  # increments count if it's a run
                # print("Run0#:", lineCount)

            elif (oldLines[i] == "1111111111111111111111111111111\n"):

                if (lastWasZero == True and lineCount > 0):  # checks if is a run of 0's
                    compressed += "10" + bin(lineCount)[2:].zfill(62)
                    # lineCount = 0

                lineCount += 1
                lastWasZero = False
                # print("Run1#:", lineCount)
            else:  # checks for literal
                # print(oldLines[i])
                if (lineCount > 0):
                    compressed += "1" + \
                        ("0" if lastWasZero else "1") + \
                        bin(lineCount)[2:].zfill(
                            62)  # add the zero or 1 and fill the rest

                    lineCount = 0

                # add the zero and copy the string without newline
                compressed += "0" + oldLines[i].rstrip('\n')
                # print(compressed)

        if (lineCount > 0):
            compressed += "1" + \
                ("0" if lastWasZero else "1") + bin(lineCount)[2:].zfill(62)
        else:
            compressed += "0" + oldLines[i]

        files.write(compressed)


if __name__ == '__main__':
    main()
