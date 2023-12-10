# Python 练习作业


这份练习作业旨在帮助初学者熟悉Python编程，并包含了涵盖函数、字符串、运算符、集合、列表等基础技能的多项选择题。

通过这个练习，你可以提高对Python变量赋值、类型转换、运算符和表达式、输入输出、函数、流程控制、字符串、列表、字典等方面的理解。这将有助于夯实你在Python编程中的基础知识，并为进一步的学习奠定基础。

## 1. 

```python
sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1, "Vicki")
print(sampleSet)
```

上面的代码会打印出来什么？

```text
A:  {‘Vicki’, ‘Jodi’, ‘Garry’, ‘Eric’}
B:  {‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}
C:  会报错。
```

## 2.

```python
for i in range(1, 5):
    print(i)
else:
    print("这是else块的语句")
```

上面的for循环中"else"块内的代码会执行吗？


```text
A: 否
B: 是
```

## 3.

```python
def calculate (num1, num2=4):
    res = num1 * num2
    print(res)

calculate(5, 6)
```

上面函数的输出结果是？
```text
A: 20
B: 会报错。
C: 30
```

## 4.

在以下选项中，哪个运算符具有更高的优先级？

```text
A: %（取模运算）
B: &（位与运算）
C: **（指数运算）
D: >（比较运算）
```

## 5.

```python
for x in range(0.5, 5.5, 0.5):
    print(x)
```

上面代码的输出结果是？

```text
A: [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
B: [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
C: 会报错
```

## 6. 

```python
salary = 8000

def printSalary():
    salary = 12000
    print("Salary:", salary)

printSalary()
print("Salary:", salary)
```

上面代码的输出结果是？

```text
A: 
Salary: 12000 
Salary: 8000

B: 
Salary: 8000 
Salary: 12000

C: 
会报错
```

## 7.

```python
var = "James" * 2  * 3
print(var)
```

上面代码的输出结果是？

```text
A: JamesJamesJamesJamesJamesJames
B: JamesJamesJamesJamesJames
C: 会报错
```

## 8.

```python
valueOne = 5 ** 2
valueTwo = 5 ** 3

print(valueOne)
print(valueTwo)
```

上面代码的输出结果是？

```text
A: 10
   15
B: 25
   125
C: Error: invalid syntax
```

9. 

```python
listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)
```

上面代码的输出结果是？

```text
A: True
   True
B: True
   False
C: False
   True
```

## 10. 

```python
str = "pynative"
print (str[1:3])
```

上面代码的输出结果是？

```text
A: py
B: yn
C: pyn
D: yna
```

## 11.

```python
p, q, r = 10, 20 ,30
print(p, q, r)
```

上面代码的输出结果是？

```text
A: 10 20
B: 10 20 30
C: Error: invalid syntax
```

## 12.

```python
var= "James Bond"
print(var[2::-1])
```

上面代码的输出结果是？

```text
A: Jam
B: dno
C: maJ
D: dnoB semaJ
```

## 13.

```python
for i in range(10, 15, 1):
    print( i, end=', ')
```

上面代码的输出结果是？

```text
A: 10, 11, 12, 13, 14,
B: 10, 11, 12, 13, 14, 15,
```


## 14.

```python
var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)
```

上面代码的输出结果是？


```text
A: 6
B: 33
C: 123
D: Error
```

## 15.

```python
x = 36 / 4 * (3 +  2) * 4 + 2
print(x)
```

上面代码的输出结果是？

```text
A: 182.0
B: 37
C: 117
D: The Program executed with errors
```

## 16. 

```python
sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)
```

上面代码的输出结果是？

```text
A: The program executed with errors
B: [‘Jon’, ‘Kelly’, ‘Scott’, ‘Jessa’]
C: [‘Jon’, ‘Kelly’, ‘Jessa’, ‘Scott’]
D: [‘Jon’, ‘Scott’, ‘Kelly’, ‘Jessa’]
```

## 17.

每次修改字符串时，Python总是会创建一个新的字符串并将新字符串分配给该变量。

```text
A: 对
B: 错
```

## 18.

```python
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))
```

上面代码判断的数据类型是？

```text
A: list
B: complex
C: tuple
```

## 19.

`print(type(0xFF))` 的数据类型是？

```text
A: number
B: hexint
C: hex
D: int
```

## 20.

`print(type([]) is list)` 的输出结果是？

```text
A: False
B: True
```

## 21.

以下合法的字符串初始化是？

```text
A: str1 = 'str1'
   str1 = "str1"
   str1 = '''str'''

B: str1 = 'str1'
   str1 = "str1""
   str1 = '''str1''

C: str1 = str(Jessa)
```

## 22.

```python
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
```

上面代码的输出结果是？

```text
A: False True False True
B: True True False True
C: True True False True
D: False True True True
```

## 23.

```python
x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)
```

上面代码的输出结果是？

```text
A: NameError
B: 25
   25
C: 25
   50
```

## 24.

```python
x = 75
def myfunc():
    x = x + 1
    print(x)

myfunc()
print(x)
```

上面代码的输出结果是？

```text
A: Error
B: 76
C: 1
D: None
```

## 25.

```python
x = 50
def fun1():
    # your code to assign global x = 20
fun1()
print(x) # it should print 20
```

请选择正确的表达式，在函数 `fun1()` 中将全局变量 "x" 重新赋值为 20。

```text
A: global x =20
 
B: global var x
   x = 20

C: global.x = 20
 
D: global x
   x = 20
```

## 26.

```python
def func1():
    x = 50
    return x
func1()
print(x)
```

上面代码的输出结果是？

```text
A: 50
B: NameError
C: None
D: 20
```

## 27.

以下哪一个可以初始化这样的字符串： `Ault'Kelly`

```text
A: str1 = 'Ault\\'Kelly'
B: str1 = 'Ault\'Kelly'
C: str1 = """Ault'Kelly"""
```

## 28.

```python
print(type({}) is set)
```

上面代码的输出结果是？

```text
A: True
B: False
```

## 29.

```python
print(2 * 3 ** 3 * 4)
```

上面代码的输出结果是？

```text
A: 216
B: 864
```

## 30.

```python
y = 10
x = y += 2
print(x)
```

上面代码的输出结果是？

```text
A: 12
B: 10
C: SynatxError
```

## 31.

```python
print(2%6)
```

上面代码的输出结果是？

```text
A: ValueError
B: 0.33
C: 2
```

## 32.

```python
print(-18 // 4)
```

上面代码的输出结果是？

```text
A: -4
B: 4
C: -5
D: 5
```

## 33.

```python
print(2 ** 3 ** 2)
```

上面代码的输出结果是？

```text
A: 64
B: 512
```

## 34.

```python
x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)
```

上面代码的输出结果是？


```text
A: 100 500
B: 10 50
C: None
```

## 35.

```python
x = 100
y = 50
print(x and y)
```

上面代码的输出结果是？

```text
A: True
B: 100
C: False
D: 50
```

## 36.

Bitwise shift operators (<<, >>) has higher precedence than Bitwise And(&) operator

```text
A: False
B: True
```

## 37.

```python
a = 4
b = 11
print(a | b)
print(a >> 2)
```

上面代码的输出结果是？

```text
A: 15
   1
B: 14
   1
```

## 38.

Which of the following operators has the highest precedence?

```text
A: not
B: &
C: *
D: +
```

## 39.

```python
x = 6
y = 2
print(x ** y)
print(x // y)
```

上面代码的输出结果是？

```text
A: 66
   0
B: 36
   0
C: 66
   3
D: 36
   3
```

## 40.

```python
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
```

上面代码的输出结果是？

```text
A: [10, 20, 30, 40]
   [10, 20, 30, 40]
B: [10, 20]
   [10, 20, 30, 40]
```

## 41.

```python
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
```

上面代码的输出结果是？

```text
A: True True False True
B: False True True True
C: True True False True
D: False True False True
```

## 42.

```python
print(36 / 4)
```

上面代码的输出结果是？

```text
A: 9.0
B: 9
```

## 43.

```python
print('[%c]' % 65)
```

上面代码的输出结果是？

```text
A: 65
B: A
C: [A]
D: Syntax Error
```

## 44.

```python
x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))
```

上面代码的输出结果是？

```text
A: nan, nan, NAN, NAN
B: nan, NaN, nan, NaN
C: NaN, NaN, NaN, NaN,
```

## 45.

```python
print('PYnative ', end='//')
print(' is for ', end='//')
print(' Python Lovers', end='//')
```

上面代码的输出结果是？

```text
A:
PYnative /
is for /
Python Lovers /

B:
PYnative //
is for //
Python Lovers //

C:
PYnative // is for // Python Lovers//

D:
PYnative / is for / Python Lovers/
```

## 46.

```python
print('%x, %X' % (15, 15))
```

上面代码的输出结果是？

```text
A: 15 15
B: F F
C: f f
D: f F
```

## 47.

In Python3, Whatever you enter as input, the `input()` function converts it into a string

```text
A: False
B: True
```

## 48.

```python
print(sep='--', 'Ben', 25, 'California')
```

上面代码的输出结果是？

```text
A: Syntax Error
B: Ben–25–California
C: Ben 25 California
D: Ben–25 California
```

## 49.

```python
print('%d %d %.2f' % (11, '22', 11.22))
```

上面代码的输出结果是？

```text
A: 11 22 11.22
B: TypeError
C: 11 ’22’ 11.22
```

## 50.

```python
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
```

上面代码的输出结果是？

```text
A: Emma 25
B: Emma 20
```

## 51.

```python
def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")
```

上面代码的输出结果是？

```text
A: TypeError
B: Emma
   25
C: name
   age
```

## 52.

```python
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
```

上面代码的输出结果是？

```text
A: 15
B: Syntax Error
C: (5, 10)
```

## 53.

```python
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)
```

上面代码的输出结果是？

```text
A: 5
B: 15
C: (15, 5)
D: Syntax Error
```

## 54.

```python
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)
```

上面代码的输出结果是？

```text
A: TypeError
B: Kelly
   9000
C: (’emp’, ‘Kelly’)
   (‘salary’, 9000)
D: emp
   salary
```

## 55.

Choose the correct function declaration of `fun1()` so that we can execute the following function call successfully

```python
fun1(25, 75, 55)
fun1(10, 20)
```

```text
A: def fun1(**kwargs)
B: No, it is not possible in Python
C: def fun1(args*)
D: def fun1(*data)
```

## 56.

Python function always returns a value.

```text
A: False
B: True
```

## 57.

```python
for num in range(10, 14):
    for i in range(2, num):
        if num%i == 1:
            print(num)
            break
```

上面代码的输出结果是？

```text
A: 10
   11
   12
   13
B: 11
   13
```

## 58.

```python
x = 0
while (x < 100):
    x+=2
print(x)
```

上面代码的输出结果是？

```text
A: 101
B: 99
C: None of the above, this is an infinite loop
D: 100
```

## 59.

```python
for l in 'Jhon':
    if l == 'o':
        pass
    print(l, end=", ")
```

上面代码的输出结果是？

```text
A: J, h, n,
B: J, h, o, n,
```

## 60.

```python
for num in range(2,-5,-1):
    print(num, end=", ")
```

上面代码的输出结果是？


```text
A: 2, 1, 0
B: 2, 1, 0, -1, -2, -3, -4, -5
C: 2, 1, 0, -1, -2, -3, -4
```

## 61.

```python
x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)
```

上面代码的输出结果是？


```text
A: 99
B: 90
C: 100
```

## 62.

```python
a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')
```

上面代码的输出结果是？

```text
A: False
B: True
```

## 63.

```python
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
```

上面代码的输出结果是？

```text
A: 2
B: 0
C: 3
D: 4
```

## 64.

```python
x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
```

上面代码的输出结果是？


```text
A: 0
B: 4
C: 2
D: 3
```

## 65.

`if -3` will evaluate to True.

```text
A: True
B: False
```

## 66.

```python
for num in range(-2,-5,-1):
    print(num, end=", ")
```

上面代码的输出结果是？

```text
A: -2, -1, -3, -4
B: -2, -1, 0, 1, 2, 3,
C: -2, -1, 0
D: -2, -3, -4,
```

## 67.

```python
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
    for y in items:
        print(x, y)
```

上面代码的输出结果是？

```text
A: 10 Chair
   10 Table
   20 Chair
   20 Table
B: 10 Chair
   10 Table
```

## 68.

```python
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)
```

上面代码的输出结果是？

```text
A: 20
B: 21
C: 10
D: 30
```

## 69.

```python
complex(1.25)
```

上面代码的输出结果是？

```text
A: (1.25+0j)
B: Value Error: Missing an imaginary part of a complex number
```

## 70.

In Python 3, the integer ranges from -2,147,483,648 to +2,147,483,647.

```text
A:  False
B:  True
```

## 71

```python
from numbers import Number
from decimal import Decimal
from fractions import Fraction

print(isinstance(2.0, Number))
print(isinstance(Decimal('2.0'), Number))
print(isinstance(Fraction(2, 1), Number))
print(isinstance("2", Number))
```

上面代码的输出结果是？


```text
A: True
   False
   True
   True
   
B: True
   True
   True
   True
   
C: True
   False
   True
   False
   
D: True
   True
   True
   False
```

## 72. 

```python
print( (1.1 + 2.2) == 3.3 )
```

上面代码的输出结果是？

```text
A: True
B: False
```

## 73.

```python
import math
print(math.ceil(252.4))
print(math.floor(252.4))
```
上面代码的输出结果是？

```text
A: 252
   252
B: 252
   253
C: 253
   252
```

## 74.

```python
print(abs(-45.300))
```

上面代码的输出结果是？

```text
A: 45.3
B: -45.3
C: -45.300
D: 45.300
```

## 75.

```python
print(round(100.2563, 3))
print(round(100.000056, 3))
```

上面代码的输出结果是？


```text
A: 100.256
   100
B: 100.256
   100.000
C: 100.256
   100.0
```

## 76.

```python
str1 = 'Welcome'
print (str1[:6] + ' PYnative')
```

上面代码的输出结果是？

```text
A: Welcome PYnative
B: WelcomPYnative
C: Welcom PYnative
D: WelcomePYnative
```

## 77. 

```python
str = "My salary is 7000";
print(str.isalnum())
```

上面代码的输出结果是？


```text
A: True
B: False
```

## 78.

```python
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)
```

上面代码的输出结果是？

```text
A: True
   False
B: True
   True
```

## 79.

```python
str1 = "my name is James bond";
print (str1.capitalize())
```

上面代码的输出结果是？

```text
A: My Name Is James Bond
B: TypeError: unsupported operand type(s) for * or pow(): 'str' and 'int'
C: My name is james bond
```

## 80.

```python
print("John" > "Jhon")
print("Emma" < "Emm")
```

上面代码的输出结果是？

```text
A: True
   False
B: False
   False
```

## 81.

```python
strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)
```

上面代码的输出结果是？

```text
A: False False
B: True True
C: True False
D: False True
```

## 82.

```python
str1 = 'Welcome'
print(str1*2)
```

上面代码的输出结果是？



```text
A: WelcomeWelcome
B: TypeError unsupported operand type(s)
```

## 83.

```python
str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
```

上面代码的输出结果是？

```text
A: PYn PYnat ive PYnativ vitanYP
B: Yna PYnat tive PYnativ vitanYP
C: Yna PYnat tive PYnativ PYnativ
```

## 84.

```python
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))
```
上面代码的输出结果是？
```text
A: 5
B: 6
C: 7
```

## 85.

```python
l = [None] * 10
print(len(l))
```

上面代码的输出结果是？

```text
A: 10
B: 0
C: Syntax Error
```

## 86.

```python
sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)
```

上面代码的输出结果是？

```text
A: [20, 30, 40, 50]
   [10, 20, 40]
B: [10, 20, 30, 40]
   [10, 20, 30, 50]
C: [10, 20, 30, 40]
   [10, 20, 40]
```

## 87.

```python
aList = [5, 10, 15, 25]
print(aList[::-2])
```

上面代码的输出结果是？

```text
A: [15, 10, 5]
B: [10, 5]
C: [25, 10]
```

## 88.

```python
list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))
```

上面代码的输出结果是？

```text
A: PYnative
B: zara
```

## 89.

```python
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)
```

上面代码的输出结果是？

```text
A: [10, 20, 30, 40, 50, 60]
   [10, 20, 30, 40, 50, 60]
B: [10, 20, 30, 40, 50, 60]
   [10, 20, 30, 40, 50, 60, 60]
```

## 90.

```python
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)
```

上面代码的输出结果是？

```text
A: [4, 20, 24, 28, 8, 12, 16]
B: [4, 20, 24, 28]
```

## 91.

```python
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)
```

上面代码的输出结果是？

```text
A: []
B: list index out of range.
C: [10, 20]
```

## 92.

```python
aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])    
print(aList[1][3])
```

上面代码的输出结果是？

```text
A: P 8
   Y 16
B: P
   12
C: Y
   16
```

## 93.

```python
resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)
```

上面代码的输出结果是？

```text
A: [‘Hello Dear’, ‘Hello Bye’, ‘Good Dear’, ‘Good Bye’]
B: [‘Hello Dear’, ‘Good Dear’, ‘Hello Bye’, ‘Good Bye’]
```

## 94.

```python
my_list = ["Hello", "Python"]
print("-".join(my_list))
```

上面代码的输出结果是？

```text
A: HelloPython-
B: Hello-Python
C: -HelloPython
```

## 95.

```python
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)
```

上面代码的输出结果是？

```text
A: KeyError: ‘age’
B: None
```

## 96.

```python
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
```

上面代码的顶一下，下面哪个可以合法的获取到value？

```text
A: sampleDict['class']['student']['marks']['history']
B: sampleDict['class']['student']['marks'][1]
C: sampleDict['class'][0]['marks']['history']
```

## 97.

```python
dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)
```

上面代码的输出结果是？

```text
A: True
B: False
```

## 98.

```python
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
```

Select the all correct way to **remove** the key `marks` from a dictionary

```text
A: student.pop("marks")
B: student.remove("marks")
C: student.popitem("marks")
```

## 99.

```python
sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)
```

上面代码的输出结果是？

```text
A: [ (‘first’, 100), (‘second’, 200), (‘third’, 300) ]
B: Options: SyntaxError: invalid syntax
C: {‘first’: 1, ‘second’: 2, ‘third’: 3}
```

## 100.

```python
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
```

Please select all correct ways to empty the following dictionary

```text
A: del student
B: del student[0:2]
C: student.clear()
```

## 101.

```python
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)
```

上面代码的输出结果是？

```text
A: KeyError: ‘age’
B: None
```

## 102.

```python
samplelist = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
```

Which method should I use to get 4 elements from the following list randomly

```text
A: random.choice(samplelist, 4)
B: random.sample(samplelist, 4)
```

## 103.

To generate a random float number between 20.5 to 50.5, which function of a random module I need to use

```text
A: random.random(20.5, 50.5)
B: random.uniform(20.5, 50.5)
C: random.randrange(20.5, 50.5)
D: random.randfloat(20.5, 50.5)
```

## 104.

```python
numberList = [100, 200, 300, 400, 500]
```

Choose the correct function to get 3 elements from the list randomly in such a way that each element of the list has a different probability of being selected.

```text
A: random.choices(numberList, weights=(10, 5, 15, 20, 50), k=3)

B: random.choice(numberList, weights=(10, 5, 15, 20, 50), k=3)

C: random.sample(numberList, weights=(10, 5, 15, 20, 50), k=3)

```

## 105.

Choose the correct function from the following list to get the random integer between 99 to 200, which is divisible by 3.

```text
A: random.randrange(99, 200, 3)
B: random.randint(99, 200, 3)
C: random.random(99, 200, 3)
```

## 106.

`str1 = "PYnative"`. Choose the correct function to pick a single character from a given string randomly.

```text
A: random.sample(str1)
B: random.choice(str1)
C: random.get(str1, 1)
```

## 107.

`random.seed()` 方法用于初始化伪随机数生成器。random 模块使用种子值作为基础生成随机数。如果没有提供种子值，它将使用系统的当前时间。

```text
A: True
B: False
```

## 108.

Which method should i use to capture and change the current state of the random generator

```text
A: random.getstate()
   random.setstate(state)
B: random.currentstate()
   random.setcurrentstate(state)

```
