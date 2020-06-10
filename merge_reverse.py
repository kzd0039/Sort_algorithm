def merge_revstr(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_revstr(left)
        merge_revstr(right)

        i = j = k = 0

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        


def main():
    test = [1,2,3,4,5,6,7]
    merge_revstr(test)
    print(test)

if __name__ == "__main__":
    main()