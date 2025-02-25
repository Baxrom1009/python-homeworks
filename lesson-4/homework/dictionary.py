## Task 2
# 1st ex

# def is_prime(n:int):
#     if n < 2:
#         return(False)
#     for i in range(2,n):
#         if n % i == 0:
#             return(False)
#         else:
#             return(True)


# print(is_prime(6))

# 2nd ex

# def digit_sum(k:int):
#     if k == 0:
#         return 0
#     else:
#         return k % 10 + digit_sum(k // 10)

# print(digit_sum(25))

# 3rd ex

# def numbers(n):
#     num = 2
#     while num <= n:
#         print(num)
#         num *= 2
   
# n = int(input('Input_number:'))
# numbers(n)


#### Task 3

## 1st ex

# def func_tion(name, age):
#     print(f'Hi {name}. You are {age} y.o.')

# func_tion('Baxrom',28)

## 2nd ex

# def func1(*args):
#     for i in args:
#         print(i)

# func1(20,40,60)
# func1(80,100)

## 3rd ex

# def calculation(a,b):
#     c1 = a+b
#     c2 = a-b
#     print(c1,c2)

# calculation(40,10)

## 4th ex

# def show_employee(name,salary=9000):
#     print(f'Name: {name} salary: {salary}')

# show_employee('Ben', 12000)
# show_employee('Jessa')

## 5th ex

# def fucn1(a,b):
#     def func2():
#         return a + b
#     return func2() + 5

# res = fucn1(5,10)
# print(res)


## 6th ex

# def Recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + Recursive_sum(n-1)

# res = Recursive_sum(20)
# print(res)

## 7th ex

# def display_student(name, age):
#     print(name, age)

# display_student('Emma', 26)


# show_Student = display_student

# show_Student('Emma', 26)

## 8th ex

# even_numbers = list(range(4,31,2))
# print(even_numbers)

## 9th ex

# x = [4, 6, 8, 24, 12, 2]
# a= max(x)
# print(a)

##### Task 1

## 2nd ex

# d = {0: 10, 1: 20}
# d.update({2:30})
# print(d)

## 3rd ex

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# dic4 = {}

# for i in (dic1,dic2,dic3):
#     dic4.update(i)

# print(dic4)

## 6th ex

# a = int(input('Choose number: '))

# d = dict()

# for i in range(1,a+1):
#     d[i] = i * i

# print(d)

## 7th ex

# d = dict()

# for i in range(1,16):
#     d[i] = i ** 2

# print(d)

## 8th 

# d = {'a':10,'b':20}
# d1 = {'c':30,'d':40}

# d.update(d1)

# print(d)

## 9th ex

# d = {'name': 'Bruno', 'Age':28}

# for key in d:
#     print(key,' ', d[key])

## 10th ex

# d = {'a':10,'b':20, 'c':30, 'd':40}

# total = sum(d.values())
# print(total)

