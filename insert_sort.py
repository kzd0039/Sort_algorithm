
def insert_sort(array):
    for i in range(1,len(array)):
        key, j = array[i], i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def main():
    lists = [int(x) for x in input('please enter number:').split()]
    insert_sort(lists)
    for ele in lists:
        print(ele, end=' ')

if __name__ == '__main__':
    main()