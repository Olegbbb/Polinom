from random import randint
while True:
    try:
        k = int(input("Введите коэффициент k: "))
        break
    except: 
        print("Введите целое число!!!")

my_list = []
for _ in range(0, k + 1):
    b = f"x**{_}"
    a = randint(-100, 100)
    print(a, end = ' ')
    if a == 0:
        continue
    elif _ == 0:
        if a > 0:
            my_list.insert(0, '+ ' + str(a))
        if a < 0:
            my_list.insert(0, '- ' + str(abs(a)))
    elif _ == 1:
        if a > 0:
            my_list.insert(0, '+ ' + str(a) + 'x')
        if a < 0:
            my_list.insert(0, '- ' + str(abs(a)) + 'x')
    elif a == 1 and _ == k:
        my_list.insert(0, (b))
    elif a == 1 :
        my_list.insert(0,'+ ' + (b))
    elif a == -1:
        my_list.insert(0, ('- ' + b))
    elif a > 0 and _ == k :
        my_list.insert(0, (str(a) + b))
    elif a > 0 :
        my_list.insert(0, ("+ " + str(a) + b))
    else:
        my_list.insert(0, ( "- " + str(abs(a)) + b))

my_polinom = ' '.join(my_list)
with open('polynomial.txt', 'w', encoding = 'UTF-8') as data:
    data.write(my_polinom + ' = 0')





