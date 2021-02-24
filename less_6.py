#List comprehension
'''A = [x**2 for x in range(10)] '''
#тоже самое что
'''B = []
for x in range(10):
    B.append(x**2)'''
#print(A)
#print(B)
#сгенерировать список В из четных элементов списка  А, возведенных в квадрат
'''A = [2,5,7,1,7,4,8]
B = [x**2 for x in A if x%2 == 0]'''
# пример тернарного условия if
# B = [0 if x<0 else x**2 for x in A if x%2 == 0]

# A = [4,2,5,1,3]
def insert_sort(A):
    """ сортировка списка А вставками """
    N = len(A)
    for top in range(1,N):
        k = top
        while(k > 0 and A[k] < A[k-1]):
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """ сортировка списка А выбором"""
    pass

def bubble_sort(A):
    """ сортировка списка А методом пузырька"""
    pass

def test_sort(sort_algorithm):
    print('тестирую - ', insert_sort.__doc__)
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



test_sort(insert_sort)