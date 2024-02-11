# Object Type / Data Type

- Numebr : 1234, -1234, 3+4i, Decimal(), Fraction()

- String : "a", "Gopal's"

- List : [ 1, 2, 3 ], [ [a, b], c ]

- Tuple : ( 1, 2, 3 ), ( [a, b], c )

- Dictionary : { "key": "value", "key2": "value2" }

- Set : { 1, 2, 3 }

- Boolean : True, False

- File : open("file.txt")

- None : None

- Advance : Decorators, Generators, Iterators, MetaProgramming

---

## Get started with data types

### Numbers

---

```
x = 4

y = 5.0

x = float(x) # convert int to float

z = x + y

>>> int( y ) ==> 5

x , y , z ==> (4, 3, 4) // Gives Tuple

x ** 2 ==> 16 // Power of x by 2

10 % 3 ==> 1 // Gives remainder

1 / 3.0 ==> 0.33333333

>>> repr("Gopal")  ==> "'Gopal'"

>>> str("Gopal") ==> 'Gopal'

>>> print("Gopal") ==> Gopal

1 < 2 ==> True // Checks if 1 is less than 2

1 > 2 ==> False // Checks if 1 is greater than 2

1 === 2 ==> False // Checks if 1 is equal to 2

1 != 2 ==> True // Checks if 1 is not equal to 2

x = 2
y = 3
z = 4

x < y < z ==> True // Checks if x is less than y and y is less than z i.e x < y and y < z

1 == 2 < 3 ==> False // Checks if 1 is equal to 2 and 2 is less than 3 i.e 1 == 2 and 2 < 3

>>> import math
>>> math.floor(3.5) ==> 3
>>> math.floor(-3.5) ==> -4 // -4 is nearest smalled number to -3.5
>>> math.floor(-3.9) ==> -4 // -4 is nearest smalled number to -3.9

>>> math.trunc(2.8) ==> 2 // trunc is used to remove decimal
>>> math.trunc(-2.8) ==> -2 // trunc brings towards zero

99999999999999999999 + 1 ==> 100000000000000000000

999999999999999999999 * 2.1 ==> 2.1e+21

2 + 1j ==> (2+1j) // complex number or iota

( 6 + 2j ) * 3 ==> (18+6j) // complex number multiplication

0o20 ==> 16 // octal of 20 is 16

0xFF ==> 255 // hex of 255 is FF

0b101 ==> 5 // binary of 5 is 101

>>> oct(16) ==> '0o20' // octal of 16 is 20
>>> hex(255) ==> '0xff' // hex of 255 is FF
>>> bin(5) ==> '0b101' // binary of 5 is 101
>>> int("64",8) ==> 52 // 64 in octal is 52
>>> int("64",16) ==> 100 // 64 in hex is 100

1 << 2 ==> 4 // bitwise left shift 1 by 2

>>> import random

>>> random.random() ==> 0.7000959205389718 // Gives randome value between 0 and 1

>>> random.randint(1,10) => 4 // Random number between 1 and 10

>>> random.choice([1,2,3,4]) ==> 3 // Random number from list


0.1 + 0.1 + 0.1 ==> 0.30000000000000004
0.1 + 0.1 + 0.4 ==> 0.6000000000000001
0.1 + 0.1 + 0.1 - 0.3 ==> 5.551115123125783e-17

from decimal import Decimal
>>> Decimal("0.1") + Decimal("0.1") + Decimal("0.1") ==> Decimal('0.3')
Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3") ==> Decimal('0.0')


>>> from fractions import Fraction
>>> myFrac = Fraction(2,7)
>>> myFrac ==> Fraction(2, 7)

```

### Set

---

```
>>> setone = {1,2,3,4 }
>>> setone &  { 1,3 } ==>{1, 3} // Gives intersection
>>> setone |  { 5 } ==>{1, 2, 3, 4, 5} // Gives union
>>> myset - {1, 2, 3, 4, 5} ==> set() // Gives difference, result is set() not {} because {} is used to denote dictionary
```

### Boolean

---

```
>>> type(True)
<class 'bool'>

True == 1 ==> True // Python treats True as 1

True + 4 ==> 5 //  Python treats True as 1


```

### Strings

---

```
name = "Gopal Adhikari"
name  ==> 'Gopal Adhikari'

first_char = name[0]
first_char ==> 'G' // G is first character

first_name = name[0:5]
first_name ==> 'Gopal' // Gopal is first 5 characters

number_list = "0123456789"
number_list[:] ==> '0123456789'
number_list[3:] ==> '3456789'
number_list[3:7] ==> '3456'
number_list[:7] ==> '0123456'
number_list[0:10:2] ==> '0246

x = '    Hello World   '
>>> x.strip() ==> 'Hello World'

>>> x.replace("World", "Gopal") ==>'    Hello Gopal   '

names = "Lemon, Ginger, Masala, Mint"
>>> names.split() ==> ['Lemon,', 'Ginger,', 'Masala,', 'Mint']

>>> names.split(", ")
['Lemon', 'Ginger', 'Masala', 'Mint']

>>> names.find("Lemon") ==> 0
>>> names.find("Mint")  ==> 23

>>> names.find("Minte") ==> -1

>>> name = "aaaa"
>>> name.count("a") ==> 4

>>> chai_variety = ["Lemon", "Masala","Ginger"]
chai_variety ==> ['Lemon', 'Masala', 'Ginger']

>>> print("".join(chai_variety)) ==> LemonMasalaGinger
>>> print(" ".join(chai_variety)) ==> Lemon Masala Ginger

>>> len(chai_variety) ==> 3

he = "He said, \"samosa is awesome\""
he ==> 'He said, "samosa is awesome"'

>>> name = "Gopal\nAdhikari"
>>> name ==> 'Gopal\nAdhikari'
>>> print(name)
Gopal
Adhikari

>>> name = r"Gopal\nAdhikari"
>>> print(name) ==> Gopal\nAdhikari
name ==> 'Gopal\\nAdhikari'

"Gopal" in name ==> True

```

## Lists

```
>>> tea_variety = ["Black" , "Green", "Oolong", "White"]

tea_variety[0] ==> 'Black'
tea_variety[1] ==> 'Green'
tea_variety[2] ==> 'Oolong'
tea_variety[4] ==> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
tea_variety[-1] ==> 'White'
tea_variety[:] ==> ['Black', 'Green', 'Oolong', 'White']

tea_variety[0] = "Herbal"
tea_variety ==> ['Herbal', 'Green', 'Oolong', 'White']

tea_variety[1:1] ==>[]
tea_variety[1:1] = ["test","test"] tea_variety ==> ['Herbal', 'test', 'test', 'Green', 'Oolong', 'White']

tea_variety[1:3] = []
tea_variety ===> ['Herbal', 'Green', 'Oolong', 'White'] // deleteing


myList = [1,2,3]
if 1 in myList :
    print("Yes") // Yes
>>> myList.append(4)
myList ==> [1, 2, 3, 4]
>>> if 1 in myList :
...     print("I have") ==> I have

> myList.remove(1)
myList ==> [2, 3]

myList.insert(1,10)
myList ===> [2, 10, 3]

myNewList = myList.copy()
myNewList ==> [2, 10, 3]

sqaured_nums = [ x ** 2 for x in range(10)] ==> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

### Dictionary

```
myDict = { "Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild"}

myDict.get("Masala") ==> 'Spicy'

myDict["Masala"] ==> 'Spicy'


# If key is not available, using [] syntax gives error
myDict["Masalaa"] ==> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Masalaa'

myDict.get("Masalaa") // None , if key is not available .get syntax return nothing and doesnt throw error

myDict ==> {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
myDict["Masala"] = "Fresh"
myDict ==> {'Masala': 'Fresh', 'Ginger': 'Zesty', 'Green': 'Mild'} // Changing the value


myDict ==> {'Masala': 'Fresh', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> for chai in myDict:
...     print(chai) // Prints the key
...
Masala
Ginger
Green


>>> for chai in myDict:
...     print(chai, myDict[chai]) // gives key and value
...
Masala Fresh
Ginger Zesty
Green Mild

for key,value in myDict.items(): // Acessing key value directly
...     print(key, value)
...
Masala Fresh
Ginger Zesty
Green Mild

if "Masala" in myDict:
...     print("Hurray")
...
==> Hurray

myDict.pop("Masala") // remove key value
'Fresh'
myDict ==> {'Ginger': 'Zesty', 'Green': 'Mild'}

myDict.popitem() // Delete last item
myDict ==> {'Ginger': 'Zesty'}


squared_nums = {x:x**2 for x in range(6) }
squared_nums ==> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squared_nums.clear() // clear the dictionary
squared_nums ==> {}

new_dict ==> {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
```

### Tuple

Immutable

```
person = ("Gopal", "Adhikari", 30)
person ==> ('Gopal', 'Adhikari', 30)
person[0]
'Gopal'
person[-1]
30

person[0:2] ==> ('Gopal', 'Adhikari')

person[1] = "Hello"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


len(person) ==> 3

```
