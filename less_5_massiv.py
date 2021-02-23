A = [1,2,3,4,5] #Является списком list (list - является объектом)
for i in A:
    print(i,end='*')
    #в данном примере i является ссылкой на элементы массива, и изменяя i, например i+=1 не изменит значения элементов массива А
    # для того чтобы изменить сами элементы в массиве A необходимо к ним обращаться по индексу
    '''
    for k in range(5):
        A[k]=A[k]*3
    '''
    # A=[0]*1000 - создаст пустой массив на 1000 элементов
    # копирование одного массива в другой
    '''
    A = [1,4,6,78]
    B = [0]*4
    for k in range(4):
        B[k] = A[k]
    '''
    #более правильное копирование будет B=list(A)

    #добавление объекта в список с помощью метода append
    """
    A = []
    x = int(input())
    A.append(x)
    len(A) - вернет значение количества хранимых элементов
    x = A.pop() - удаляет последнее значение из массива и возвращает его значение (которое удалил).
    """




#линейный поиск в массиве с примером тестирования функции
def array_search(A:list, N:int, x:int):
    '''
    Осуществляет поиск числа х в массиве А с размерностью от 0 до N-1.
    Если искомое число не найдено, вернуть -1, если найдено вернуть индекс в массиве
    '''
    for i in range(N):
        if A[i]==x:
             return i
    return -1

#переворот массива
def invert_array(A:list, N:int):
    """
    Обращение массива (поворот задом-наперед)
    """
    for i in range(N//2):
        A[i],A[N-1-i]=A[N-1-i],A[i]
    print(A)

#циклический сдвиг массива влево или вправо
def shift_left(A:list, N:int):
    """
    сдвиг массива влево на 1 значение
    """
    tmp = A[0]
    for i in range(N-1):
        A[i]=A[i+1]
    A[N-1] = tmp
    print(A)

def shift_right(A:list, N:int):
    """
    сдвиг массива вправо на 1 значение
    """
    tmp = A[N-1]
    for i in range(N-2,-1,-1):
        A[i+1]=A[i]
    A[0]=tmp
    print(A)


#тестирование функции
def test_array_search():
    A1=[1,2,3,4,5]
    m=array_search(A1,5,3)
    if m==2:
        print('Test1 ok')
    else:
        print('Test1 fail')
         
    m=array_search(A1,5,-2)
    if m==-1:
        print('Test2 ok')
    else:
        print('Test2 fail')

def test_invert_array():
    A1=[1,2,3,4,5]
    invert_array(A1,5)
    if A1==[5,4,3,2,1]:
        print('Test1 ok')
    else:
        print('Test1 fail')

A=[1,2,3,4,5]
#вызовы функций
#test_array_search()
#test_invert_array()
#shift_left(A,5)
#shift_right(A,5)