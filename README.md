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

```
>>> setone = {1,2,3,4 }
>>> setone &  { 1,3 } ==>{1, 3} // Gives intersection
>>> setone |  { 5 } ==>{1, 2, 3, 4, 5} // Gives union
>>> myset - {1, 2, 3, 4, 5} ==> set() // Gives difference, result is set() not {} because {} is used to denote dictionary
```

### Boolean

```
>>> type(True)
<class 'bool'>

True == 1 ==> True // Python treats True as 1

True + 4 ==> 5 //  Python treats True as 1


```
