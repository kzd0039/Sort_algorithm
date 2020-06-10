def merge_revstr(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_revstr(left)
        merge_revstr(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        


def main():
    test = [7,6,5,2,1,66,2]
    merge_revstr(test)
    print(test)

if __name__ == "__main__":
    main()