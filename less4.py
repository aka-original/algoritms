#определить число простое или составное, если простое вывести True
def is_number(x):
    devision=2
    while devision<x:
        if x%devision==0:
            return False
        devision+=1
    return True

x=int(input())
print(is_number(x))