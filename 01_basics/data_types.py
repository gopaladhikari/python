x = 4

y = 5.0

x = float(x)  # convertinttofloat

z = x + y

int(y)  # 5

x, y, z  # (4,3,4)//GivesTuple

x**2  # 16//Powerofxby2

10 % 3  # 1//Givesremainder

1 / 3.0  # 0.33333333

repr("Gopal")  # "'Gopal'"

str("Gopal")  #'Gopal'

print("Gopal")  # Gopal

print(1 < 2)  # True//Checksif1islessthan2
print(1 > 2)  # False//Checksif1isgreaterthan2

print(1 == 2)  # False//Checksif1isequalto2

print(1 != 2)  # True//Checksif1isnotequalto2

x = 2
y = 3
z = 4

x < y < z  # True//Checksifxislessthanyandyislessthanzi.ex<yandy<z

1 == 2 < 3  # False//Checksif1isequalto2and2islessthan3i.e1==2and2<3

import math

math.floor(3.5)  # 3
math.floor(-3.5)  # -4//-4isnearestsmallednumberto-3.5
math.floor(-3.9)  # -4//-4isnearestsmallednumberto-3.9

math.trunc(2.8)  # 2//truncisusedtoremovedecimal
math.trunc(-2.8)  # -2//truncbringstowardszero

print(99999999999999999999 + 1)  # 100000000000000000000

print(999999999999999999999 * 2.1)  # 2.1e+21

print(2 + 1j)  # (2+1j)//complexnumberoriota

print((6 + 2j) * 3)  # (18+6j)//complexnumbermultiplication

print(0o20)  # 16//octalof20is16

print(0xFF)  # 255//hexof255isFF

print(0b101)  # 5//binaryof5is101

print(oct(16))  #'0o20'//octalof16is20
print(hex(255))  #'0xff'//hexof255isFF
print(bin(5))  #'0b101'//binaryof5is101
print(int("64", 8))  # 52//64inoctalis52
print(int("64", 16))  # 100//64inhexis100

print(1 << 2)  # 4//bitwiseleftshift1by2

import random

random.random()  # 0.7000959205389718//Givesrandomevaluebetween0and1

random.randint(1, 10)  # 4//Randomnumberbetween1and10

random.choice([1, 2, 3, 4])  # 3//Randomnumberfromlist


0.1 + 0.1 + 0.1  # 0.30000000000000004
0.1 + 0.1 + 0.4  # 0.6000000000000001
0.1 + 0.1 + 0.1 - 0.3  # 5.551115123125783e-17

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))  # Decimal('0.3')
print(
    Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
)  # Decimal('0.0')


from fractions import Fraction

myFrac = Fraction(2, 7)
myFrac  # Fraction(2,7)


# Strings
