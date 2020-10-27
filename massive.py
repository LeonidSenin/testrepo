# a = [1, 2, 3, 5, 6, 2, 0, 1, 4]
# for i in range(len(a)):
#     print(a[i], end=' ')

# a=list(input())
# for i in range(len(a)):
#     print (a[i],end='')

# Пример на подсчет строк
#
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# sum=0
# for i in range(3):
#     sum_row=0
#     for j in range(len(a)):
#         sum+=a[i][j]
#         sum_row+=a[i][j]
#         print (a[i][j],end = ' ')
#     print()
#     print('Сумма строки',sum_row)
# print ('Общая сумма',sum)


# Пример заполнения матрицы(массива)
# a=[]
# n=int(input('Введите количество строк'))
# m=int(input('Введите количество столбцов'))
# for i in range(n):
#     b=[]
#     for i in range(m):
#         b.append(int(input('Введите элемент:')))
#     a.append(b)
# for i in a:
#     print(i)


# Пример
# a = []
# n=int(input('Введите количество строк'))

# # Цикл заполнения массива
# for i in range(n):
#     a.append([0]*n)

# # Цикл обработки информации
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j]=10
#         if i > j:
#             a[i][j] = 3
#         if i < j:
#             a[i][j] = 5

# # Цикл вывода
# for i in a:
#     print(i)


# Задана целочисленная квадратная матрица размером N x N. Требуется транспонировать ее относительно главной диагонали.
# 3 4 9 1 2   # 3 8 4 7 5
# 8 2 0 5 1   # 4 2 7 1 6
# 4 7 4 8 7   # 9 0 4 3 3
# 7 1 3 3 8   # 1 5 8 3 7
# 5 6 3 7 0   # 2 1 7 8 0
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#  ]
# c=0
#  # Цикл обработки информации
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i>j:
#             c=a[i][j]
#             a[i][j]=a[j][i]
#             a[j][i]=c
# # Цикл вывода
# for i in a:
#     print(i)



