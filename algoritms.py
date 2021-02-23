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
  

simple_number(100)