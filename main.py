import random
n = int(input('Введіть значення n:'))
print('Список а):')
a_list = []
for i in range(n):
    a_list.append(random.random())
print(a_list)
m = n // 2 if n % 2 == 0 else n // 2 + 1
result_list = []
for i in range(m):
    result_list.append(a_list[i])
    if i + m < n:
        result_list.append(a_list[i + m])
print(result_list)