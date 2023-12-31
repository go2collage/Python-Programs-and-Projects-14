# Python Program / Project

def BinarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    m = 0
    while(low <= high):
        m = (low + high) // 2
        if (key < arr[m]):
            high = m - 1 
        elif (key > arr[m]):
            low = m + 1
        else:
            return m
    return -1

def FibSearch(arr, key, n):
    b = 0
    a = 1
    f = b + a
    while(f < n):
        b = a
        a = f
        f = b + a
        offset = -1
    while(f>1):
        i = min(offset+b, n-1)
        if(arr[i]<key):
            f = a
            a = b
            b = f - a
            offset = i
        elif (arr[i]>key):
            f = b
            a = a - b
            b = f - a

        else:
            return i
    if( a and arr[offset+1] == key):
        return offset + 1
    return -1
        

# Driver Code
n = int(input("How many students joining Training Program: "))
arr = []
i = 0
for i in range(n):
    item = int(input("Enter student roll number: "))
    arr.append(item)

while(True):
    print("********** Menu **********")
    print("1. Binary Search.")
    print("2. Fibonacci Search.")
    print("3. Exit.")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        key = int(input("Enter student roll number to search from training program or not: "))
        loc = BinarySearch(arr, key)
        if (loc != -1):
            print("Yes, Student attended the training program.")
        else:
            print("Student not attended training program.")
        
    elif(choice == 2):
        key = int(input("Enter student roll number to search from training program or not: "))
        loc = FibSearch(arr, key, n)
        if (loc != -1):
            print("Yes, Student attended the training program.")
        else:
            print("Student not attended training program.")
        
    else:
        print("Exit.")
        break
