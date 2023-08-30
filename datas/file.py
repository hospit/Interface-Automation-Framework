
def tt(num, num2=2, *args):
    print(num, num2, args)

tt(1)
tt(1, 3)
# tt(1, 3, 3, 3, 3, 3, 3)
# tt(1, *(2, 3, 4, 5))
# tt(1, *[2, 3, 4, 5])

def myfun(a, *b):
    print(a)
    print(b)


myfun(1, 4)

list1 = [1,2]
list2 = [3,4]
list3 = list2+list1
print(list3)
f = lambda n: n if n < 2 else 2 * f(n - 1)
g= f(5)
print(g)