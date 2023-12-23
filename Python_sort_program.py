import random # 랜덤 모듈

sorted_list = [] # 정렬된 결과를 저장할 리스트를 초기화

def selection_sort(A): # 선택 정렬
    n = len(A) # 리스트 A의 길이
    for i in range(n-1):
        least = i # 현재 인덱스를 least 변수에 저장
        for j in range(i+1, n): # 현재 인덱스 이후의 최소값을 탐색
            if A[j] < A[least]: # 만약 현재의 최소값보다 작은 값을 찾으면
                least = j # least를 해당 값의 인덱스로 저장
        A[i], A[least] = A[least], A[i] # 찾은 최소값과 현재 위치의 값을 교환
    return A # 정렬이 완료된 리스트를 반환

def insertion_sort(A): # 삽입 정렬
    n = len(A) # 리스트 A의 길이
    for i in range(1, n):
        key = A[i] # 현재 비교할 값을 key 변수에 저장
        j = i-1 # key의 왼쪽에 있는 정렬된 부분의 마지막 인덱스를 지정
        while j >= 0 and A[j] > key:
            A[j+1] = A[j] # 정렬된 부분에서 key의 적절한 위치를 찾아 삽입
            j -= 1
        A[j+1] = key # 찾은 삽입 위치에 key 값을 삽입
    return A # 정렬이 완료된 리스트를 반환

def bubble_sort(A): # 버블 정렬
    n = len(A) # 리스트 A의 길이
    for i in range(n-1, 0, -1): # 리스트의 끝부터 시작하여 정렬을 수행
        bChanged = False # 교환이 일어났는지 확인하는 변수를 초기화
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] # 현재 요소가 다음 요소보다 크면 교환
    return A # 정렬이 완료된 리스트를 반환

def quick_sort(A, left, right): # 퀵 정렬
    if left < right:
        i = left + 1 # 분할을 위한 인덱스 초기화
        j = right # 분할을 위한 인덱스 초기화
        pivot = A[left] # 피봇을 정의
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1 # 피봇보다 큰 값을 찾을 때까지 인덱스를 증가
            while j >= left and A[j] > pivot:
                j -= 1 # 피봇보다 작은 값을 찾을 때까지 인덱스를 감소
            if i < j:
                A[i], A[j] = A[j], A[i] # pivot을 기준으로 분할하여 정렬
        A[left], A[j] = A[j], A[left] # 피봇의 최종 위치를 조정
        quick_sort(A, left, j-1) # 피봇을 기준으로 좌측 부분을 정렬 (재귀함수)
        quick_sort(A, j+1, right) # 피봇을 기준으로 우측 부분을 정렬 (재귀함수)

# 합병 정렬
def merge(array, left, mid, right):
    global sorted_list
    i = left # 왼쪽 부분 배열의 시작 인덱스
    j = mid + 1 # 오른쪽 부분 배열의 시작 인덱스
    k = left # 정렬된 결과를 저장할 배열의 인덱스
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            sorted_list[k] = array[i] # 왼쪽 부분 배열의 현재 원소를 결과 배열에 추가
            i, k = i + 1, k + 1
        else:
            sorted_list[k] = array[j] # 오른쪽 부분 배열의 현재 원소를 결과 배열에 추가
            j, k = j + 1, k + 1
    if i > mid:
        sorted_list[k : k + right - j + 1] = array[j : right + 1] # 남은 오른쪽 부분 배열을 결과 배열에 추가
    else:
        sorted_list[k : k + mid - i + 1] = array[i : mid + 1] # 남은 왼쪽 부분 배열을 결과 배열에 추가
    array[left : right + 1] = sorted_list[left : right + 1] # 정렬된 결과를 원래 배열에 복사

def merge_sort(array, left, right):
    global sorted_list
    if left < right:
        mid = (left + right) // 2 # 중간 지점
        merge_sort(array, left, mid) # 왼쪽 부분 배열을 정렬 (재귀함수)
        merge_sort(array, mid + 1, right) # 오른쪽 부분 배열을 정렬 (재귀함수)
        merge(array, left, mid, right) # 정렬된 두 부분을 합병

# 힙 정렬
def heappush(heap, n):
    heap.append(n) # 힙에 원소를 추가
    i = len(heap) - 1 # 추가된 원소의 인덱스
    while i != 1 and n > heap[i//2]:
        heap[i] = heap[i//2] # 부모 노드보다 큰 경우에는 부모와 위치를 교환
        i//=2
    heap[i] = n # 최대 힙 구조를 유지하며 원소를 삽입

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    p = 1
    i = 2
    root = heap[1] # 최대값 추출
    last = heap[size] # 힙의 마지막 값
    while i <= size:
        if i < size and heap[i] < heap[i+1]:
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i] # 자식 노드 중 더 큰 값을 부모로 올리면서 위치를 조정
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root # 최대 힙에서 최대값을 추출하고 힙 구조를 유지

def heap_sort(data):
    heap = [0]
    for e in data:
        heappush(heap, e) # 힙에 모든 원소를 삽입하여 최대 힙을 만듦
    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap) # 최대 힙에서 원소를 추출하여 역순으로 정렬
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