import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList


def main():
    
    n =[100,500,1000,2000,2500]
    listMerge = []
    listSelection= []
            
    for i in n:
        select  = []
        select.append(random.randint(1,500))

        start = time.time()
        selectionSort(select)
        stop = time.time()
        time1 = stop - start
        listSelection.append(time1)

    total1 = 0
    for time1 in listSelection:
        total1 = total1 + time1
    avgTime1 = total1/10
    

    for i in n:
        merge = []
        merge.append(random.randint(1,500))

        start2 = time.time()
        mergeSort(merge)
        stop2 = time.time()
        time2 = stop - start
        listMerge.append(time2)

    total2 = 0
    for time2 in listMerge:
        total2 = total2 + time2
    avgTime2 = total2/10
    

    print("Number of sort" + "       " + "Selection Sort" + "                   " + "Merge Sort")
    print("-----------------------------------------------------")
    for k in n:
        print(str(k)+ "            " + str(avgTime1) + "            " + str(avgTime2))
        print("-----------------------------------------------------")

if __name__ == "__main__":
    main()
