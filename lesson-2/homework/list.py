### 1st link

#1st ex

# count = 1

# while 1==1:
#     print(count)
#     count +=1
#     if count == 11:
#         break

#2nd ex

# n = 5

# for i in range(1,n+1,1):
#     for a in range(1,i+1):
#         print(a,end='')
#     print("")

# 3rd ex

# a = int(input('Enter number: '))

# s = 0
# i = 1

# while i <= a:
#     s += i
#     i += 1

# print(f'Your sum: {s}')

#4th ex

# n = 2

# while n <= 20:
#     print(n)
#     n +=2

#5th ex

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

# 6th ex

# num = 75869
# c = 0

# while num != 0:
#     num = num // 10

#     c = c + 1
#     print(c)

# 7th ex

# n = 5
# a = 5
# for i in range(0,n+1):
#     for b in range(a-i,0,-1):
#         print(b,end=' ')
#     print()

# 8th ex

# list1 = [10, 20, 30, 40, 50]
# a = reversed(list1)
# for i in a:
#     print(i)

# 9th ex

# for i in range(-10,0,1):
#     print(i)

# 10th ex

# for i in range(5):
#     print(i)
# else:
#     print('done')


# 11th ex

# start = 25
# end = 50
# print(f'Prime number between {start} and {end} are: ')

# for i in range(start, end + 1):
#     if i > 1:
#         for a in range(2,i):
#             if (i % a) == 0:
#                 break
#         else:
#             print(i)

#  12th ex

# num1 = 0
# num2 = 1

# for i in range(10):
#     print(num1)
#     r = num1 + num2

#     num1 = num2
#     num2 = r


# 13 th ex

# f = 1
# n = 5
# for i in range(1,n+1):
#     f = f * i
# print(f)

# 14th ex

# num = 76542
# r = int(str(num)[::-1])
# print(r)

# 15th ex

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# a = my_list[1::2]
# print(a)

# 16th ex

# n = 6

# for i in range(1,n+1):
#     print(i and i**3)

# 17th ex

# n = 5
# s = 2
# a = 0

# for i in range(0,n):
#     print(s, end='+')
#     a += s
#     s = s * 10 + 2
# print(a)


# 18 th  ex

# r = 5
# for i in range(0,r):
#     for a in range(0,i+1):
#         print('*',end=' ')
#     print('\r')


# for i in range(r,0, -1):
#     for a in range(0,i-1):
#         print('*', end=' ')
#     print('\r')


### 2nd link

# 1st ex

# list1 = [100, 200, 300, 400, 500]

# list1.reverse()
# print(list1)

# 2nd ex

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# a = [i+n for i,n in zip(list1,list2)]
# print(a)

# 3rd ex

# numbers = [1, 2, 3, 4, 5, 6, 7]

# a = [i ** 2 for i in numbers]
# print(a)

# 4th ex

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# a = [i+n for i in list1 for n in list2]
# print(a)

# 5th ex

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i,n in zip(list1,list2[::-1]):
#     print(i,n)

# 6th ex

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# a = list(filter(None,list1))
# print(a)

# 7th ex

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list1[2][2].append(7000)

# print(list1)

# 8th ex

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)

# 9th ex

# list1 = [5, 10, 15, 20, 25, 50, 20]

# index = list1.index(20)

# list1[index] = 200
# print(list1)

# 10th ex

# list1 = [5, 20, 15, 20, 25, 50, 20]

# a = [i for i in list1 if i != 20]
# print(a)



