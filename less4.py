#определить число простое или составное, если простое вывести True
def is_number(x):
    divisor=2
    while divisor<x:
        if x%divisor==0:
            return False
        divisor+=1
    return True
def factorize_number(x):
    divisor=2
    while x>1:
        if x%divisor==0:
            x//=divisor
            print(divisor)
        else: divisor+=1

x=int(input())
#print(is_number(x))
print(factorize_number(x))