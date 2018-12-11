#Bubble Sort Code in Python
def BubbleSort(arr):

    for iter_num in range(len(arr)-1,0,-1):
        for index in range(iter_num):
            if arr[index]>arr[index+1]:
                temp = arr[index]
                arr[index]=arr[index+1]
                arr[index+1]=temp

arr  = [20,35,69,1,22,5]

BubbleSort(arr)

print(arr)
