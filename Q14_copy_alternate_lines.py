
def copy_file(file1,file2):
    try:
        f1 = open(file1, "r")
        f2 = open(file2, "w")

        k=1

        for char in f1.read():
            if(k%2 != 0):
                f2.write(char)
            if(char == "\n"):
                k += 1

        f1.close()
        f2.close()
    except IOError as io:
        print(io)


file1 = str(input("Enter the Name of Source File : "))
file2 = str(input("Enter the Name of Destination File : "))
copy_file(file1,file2)
