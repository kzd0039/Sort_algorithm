def bubble_sort(array):
    if array:
        l = len(array)

        for j in range(l-1,-1,-1):
            for i in range(j):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
            

def main():
    lists = [int(x) for x in input('please enter number:').split()]
    bubble_sort(lists)
    for ele in lists:
        print(ele, end=' ')

if __name__=='__main__':
    main()

    