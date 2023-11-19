import random # 랜덤 모듈

sorted_list = [] # 정렬된 결과를 저장할 리스트를 초기화

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
    return A

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def quick_sort(A, left, right):
    if left < right:
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1 
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        A[left], A[j] = A[j], A[left]
        quick_sort(A, left, j-1)
        quick_sort(A, j+1, right)

def merge(array, left, mid, right):
    global sorted_list
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            sorted_list[k] = array[i]
            i, k = i + 1, k + 1
        else:
            sorted_list[k] = array[j]
            j, k = j + 1, k + 1
    if i > mid:
        sorted_list[k : k + right - j + 1] = array[j : right + 1]
    else:
        sorted_list[k : k + mid - i + 1] = array[i : mid + 1]
    array[left : right + 1] = sorted_list[left : right + 1]

def merge_sort(array, left, right):
    global sorted_list
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1 and n > heap[i//2]:
        heap[i] = heap[i//2]
        i//=2
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    p = 1
    i = 2
    root = heap[1]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i+1]:
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i]
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root

def heap_sort(data):
    heap = [0]
    for e in data:
        heappush(heap, e)
    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap)
    return data

print("***********************************")
print("*** 여러가지 정렬 프로그램 구현 ***")
print("***                             ***")
print("*** 1. 선택(selection) 정렬     ***")
print("*** 2. 삽입(insertion) 정렬     ***")
print("*** 3. 버블(bubble)    정렬     ***")
print("*** 4. 퀵(quick)       정렬     ***")
print("*** 5. 합병(merge)     정렬     ***")
print("*** 6. 힙(heap)        정렬     ***")
print("*** 7. 종료(quit)               ***")
print("***********************************")

while True:
    array = [random.randint(0, 100) for _ in range(25)]

    sel = int(input("번호 입력: "))

    if sel == 1:
        print("<선택 정렬>")
        print("정렬 전:", array)
        print("정렬 후:", selection_sort(array.copy()))

    elif sel == 2:
        print("<삽입 정렬>")
        print("정렬 전:", array)
        print("정렬 후:", insertion_sort(array.copy()))

    elif sel == 3:
        print("<버블 정렬>")
        print("정렬 전:", array)
        print("정렬 후:", bubble_sort(array.copy()))

    elif sel == 4:
        print("<퀵 정렬>")
        print("정렬 전:", array)
        quick_sort(array, 0, len(array)-1)
        print("정렬 후:", array)

    elif sel == 5:
        print("<합병 정렬>")
        print("정렬 전:", array)
        sorted_list = [0] * len(array)
        merge_sort(array, 0, len(array) - 1)
        print("정렬 후:", array)
    
    elif sel == 6:
        print("<힙 정렬(1)>")
        print("정렬 전:", array)
        result = heap_sort(array.copy())
        print("정렬 후:", result)

        print("<힙 정렬(2)>")
        print("정렬 전:", array)
        result = heap_sort(array.copy())
        print("정렬 후:", result)

    elif sel == 7:
        print("<종료>")
        break

    else:
        print("<번호 오류>")