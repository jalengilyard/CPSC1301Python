

def bubbleSort(myList):
    for i in range(0, len(myList) - 1):
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList
def main():
    lis = [3, 4, 99, 0, 2, 7]
    print(bubbleSort(lis))
main()
