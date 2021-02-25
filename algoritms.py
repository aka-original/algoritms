# решето эратосфена
def simple_number(N:int):
    """
    Решето эратосфена осуществляет поиск всех простых чисел до N элемента
    """
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for i in range(k+k, N, k):
                A[i] = False
    for k in range(N):
        #print(k, '-', 'простое' if A[k] else 'составное')
        if A[k]: print(k, end='-')
  
# Квадратичные сортировки (означает, что для сортировки массива из N элементов примерно необходимо O(N**2) операций)
# 1 - сортировка вставками (insert sort) 
#асимптотика = N*(N-1)/2
def insert_sort(A:list):
    """сортировка списка А методом вставок (insert sort)"""
    for top in range(1, len(A)):
        k = top
        while(k>0 and A[k-1]>A[k]):
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1

# 2 - сортировка методом выбора (choise sort)
def choise_sort(A:list):
    """сортировка списка А методом выбора (choise_sort)"""
    for pos in range(len(A)-1):
        for i in range(pos+1, len(A)):
            if A[pos]>A[i]:
                A[pos], A[i] = A[i], A[pos]

# 3 - сортировка методом пузырька (bubble sort)
#формала подсчета выполнения действий (асимптотика) 1+2+...+N-1 = N*(N-1)/2
def bubble_sort(A:list):
    """сортировка списка А методом пузырьков (bubble sort)"""
    for bypass in range(1, len(A)):
        for i in range(len(A)-bypass):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

# Сортировка подсчетом (count sort) для сортировки необходимо примерно O(N) сортировка работает в допустимом, маленьком диапозоне цифр (0-9), эти данные должны быть известны заранее
# Подсчитывает, сколько раз в массиве встречается каждое значение, и заполняем массив подсчитанными элементами в соответствующих количествах
def countin_sort(A:list):
    tmp_arr = []
    for i in range (len(A)):
        tmp_arr += [0]
    for i in A:
        tmp_arr[i] += 1

    j = 0
    for i in range(len(tmp_arr)):
        if tmp_arr[i]>0:
            for k in range(tmp_arr[i]):
                A[j] = i
                j += 1 

                

# тесты работоспособности-------------------------------------------------------------------------------------------------------------

def test_sort(sort_algorithm): #тесты сортировок (вставка, выбор, пузырьковая)
    print('тестирую - ', sort_algorithm.__doc__)
    print("testcase 1 - ", end="")
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')

    print("testcase 2 - ", end="")
    A = list(range(10,20)) + list(range (10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')

    print("testcase 3 - ", end="")
    A = [4,2,4,2,1]
    A_sorted = [1,2,2,4,4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')

def test_countin_sort(sort_algorithm): #тес сортировки подсчетом
    print('Тестирую - ', sort_algorithm.__doc__)
    print("testcase 1 - ", end="")
    A = [2,5,7,2,8,0,8,0,2,9]
    A_sorted = [0,0,2,2,2,5,7,8,8,9]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')


# вызовы функций------------------------------------------------------------------------------------------
#simple_number(100)
#test_sort(insert_sort)
#test_sort(choise_sort)
#test_sort(bubble_sort)
#test_countin_sort(countin_sort)

