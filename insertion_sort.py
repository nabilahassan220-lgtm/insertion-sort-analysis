def insertion_sort(arr):
  a = arr.copy()
  for i in range(1,len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j+1] = a[j]
      j -= 1
    a[j+1] = key
  return a

if __name__== "__main__"
    test = [5, 2, 9, 1, 7]
    print("Before:", test)
    print("After:",insertion_sort(test))
    print("Sorted:",insertion_sort([1, 2, 3]))
    print("Reverse:"insertion_sort([3, 2, 1]))
    
