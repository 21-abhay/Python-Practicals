def linearSearch(str_arr,key):
    for i in range(len(str_arr)):
        if str_arr[i] == key:
            return i
    return -1

def binarySearch(str_arr,key):
    high = len(str_arr) - 1
    low = 0
    while low <= high:
        mid = (high + low)//2
        if str_arr[mid] == key:
            return mid
        elif str_arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1 ):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Bubble Sorting :")
    print("Sorted List : ",arr)
    return arr


def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print("Insertion Sorting :")
    print("Sorted List : ",arr)
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Selection Sorting :")
    print("Sorted List : ",arr)
    return arr

def menu():
    print("*******  MENU  *******\n")
    print("1) Linear Search ")
    print("2) Binary Search ")
    print("3) Bubble sorting ")
    print("4) Insertion Sorting ")
    print("5) Selection Sorting ")
    print("6) Exit \n")



l = [2,5,7,22,56,67,33]
key = True
while(key):
    menu()
    n=int(input("Enter You choice : "))
    if(n==1):
        n=int(input("Enter the number want to search : "))
        index = linearSearch(l,n)
        if index >= 0:
            print("Element found at index",index)
        else:
            print("Element not found")
    elif(n==2):
        n=int(input("Enter the number want to search : "))
        l = bubbleSort(l)
        index = binarySearch(l,n)
        if index >= 0:
            print("Element found at index",index)
        else:
            print("Element not found")
    elif(n==3):
        l=bubbleSort(l)
    elif(n==4):
        l=insertionSort(l)
    elif(n==5):
        l=selectionSort(l)
    elif(n==6):
        key=False
    else:
        print("Invalid Choice")
        print("Do you want to \n1.Exit\n2.Continue")
        n=int(input("Enter Your choice : "))
        if(n==2):
            continue
        else:
            print("You exit from the programm")
            key=False
            break

