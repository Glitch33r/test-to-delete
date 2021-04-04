


my_variable = 100
my_variable_2 = -55.5
my_variable_3 = 'Hello'     # "HELLO"
my_variable_4 = True

print(my_variable, my_variable_2, my_variable_3, my_variable_4)

my_variable = my_variable + my_variable_2

print(my_variable)

print(
    type(100),            # integer
    type(my_variable_2),  # float
    type(my_variable_3),  # string
    type(my_variable_4),  # boolean
)

print(10 + 5)   # 15
print(10 - 5)   # 5
print('/', 10 / 3)   # 2.0
print(10 * 5)   # 50

print('//', 10 // 3)  # 2
print(10 ** 2)  # 100_000
print(10 % 3)   # 0

print(10 > 5)   # True
print(10 < 10)   # False
print(10 <= 10)    # False
print(10 >= 5)    # True
print(10 == 10)   # False
print(10 != 10)   # True

print(
    str(100) + 'apple'
)

# x = int(input('Введите число: '))
#
# if x == 1:
#     print(1)
# elif x == 2:
#     print('apple')
# else:
#     print('I do not know')

# elif <условие>: => else:
#                      if <условие>:


print('Hello ' + str(100) + ' world')
print('Hello {} world'.format(100))
print(f'Hello {100} world')
print(f'Hello {100 + 1} world')
print(f'Hello {my_variable * 2 - 10} world')

import datetime

print(
    datetime.datetime.now()
)

# range(start, stop, step)
# range(0, 10) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(100, 5, -5):
    print(i)


x = 0
while x != 10:
    print(x)
    x += 1  # x = x + 1
