"""
>>> meuObjeto = 10
>>> type(meuObjeto)
<class 'int'>
>>> base = 10
>>> altura = 4
>>> area = base * altura
>>> print(area)
40
>>> type(base)
<class 'int'>
>>> type(altura)
<class 'int'>
>>> type(area)
<class 'int'>
>>> base = 10.2
>>> altura = 4.0
>>> area = base * altura
>>> print(area)
40.8
>>> type(base)
<class 'float'>
>>> type(altura)
<class 'float'>
>>> type(area)
<class 'float'>
>>> a = 3.6
>>> b = 4
>>> c = a * b
>>> type(c)
<class 'float'>
>>> 
================================ RESTART: Shell ================================
>>> a = 3
>>> b = 4
>>> c = a*b
>>> type(c)
<class 'int'>
>>> a = 3.6
>>> print(c)
12
>>> type(c)
<class 'int'>
>>> c = a*b
>>> type(c)
<class 'float'>
>>> print(c)
14.4
>>> d = 3x + 5
SyntaxError: invalid syntax
>>> d = 3j + 5
>>> type(d)
<class 'complex'>
>>> type(D)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    type(D)
NameError: name 'D' is not defined
>>> id(d)
62596904
>>> id(c)
61783504
>>> id(b)
1745528800
>>> id(a)
57940928
>>> 
================================ RESTART: Shell ================================
>>> a = 10
>>> id(a)
1745528896
>>> b = a
>>> id(b)
1745528896
>>> b = 50
>>> id(b)
1745529536
>>> l = [12,24,36]
>>> id(l)
66103304
>>> m = l
>>> id(m)
66103304
>>> m[0] = 0
>>> print(m)
[0, 24, 36]
>>> print(l)
[0, 24, 36]
>>> c = a*2
>>> id(c)
1745529056
>>> d = 'texto'
>>> type(d)
<class 'str'>
>>> from math import sqrt
>>> x = 25
>>> y = sqrt(x)
>>> y
5.0
>>> type(y)
<class 'float'>
>>> type(x)
<class 'int'>
>>> 
================================ RESTART: Shell ================================
>>> a = b = c = 1
>>> id(a)
1745528752
>>> id(b)
1745528752
>>> id(c)
1745528752
>>> 
>>> a, b, c = 1, 2, 3
>>> id(a)
1745528752
>>> id(b)
1745528768
>>> id(c)
1745528784
>>> 
>>> x, y, z = 0, -10, 10
>>> print(x, y)
0 -10
>>> x, y = y, x
>>> print(x, y)
-10 0
>>> print(x, y, z)
-10 0 10
>>> 
>>> x, y, z = y, z, x
>>> print(x, y, z)
0 10 -10
>>> 
>>> 
================================ RESTART: Shell ================================
>>> a =14
>>> b = 5
>>> c = a+b
>>> print(c)
19
>>> c = a-b
>>> print(c)
9
>>> c = a*b
>>> print(c)
70
>>> c = a/b
>>> print(c)
2.8
>>> c = a // b
>>> print(c)
2
>>> c = a%b
>>> print(c)
4
>>> c = -a
>>> print(c)
-14
>>> type(a)
<class 'int'>
>>> id(a)
1745528960
>>> id(c)
59675520
>>> c = a**b
>>> print(c)
537824
>>> r = 2*a+b
>>> print(r)
33
>>> r = 2*(a+b)
>>> print(r)
38
>>> a = 10
>>> id(a)
1745528896
>>> a
10
>>> a += 1
>>> a
11
>>> a-=5
>>> a
6
>>> a*=2
>>> a
12
>>> a/=4
>>> a
3.0
>>> a = 10
>>> p = 4
>>> a+=p
>>> a
14
"""

"""
from math import sqrt
x = 9
r = sqrt(x)
print(r)
3.0

import math
x = 9
r = math.sqrt(x)
print(r)
3.0

>>> print('Este é o capítulo 02 do livro')
Este é o capítulo 02 do livro
>>> a = 21
>>> print(a)
21
>>> a = 12
>>> b = 19
>>> print(a, b)
12 19
>>> print('Valor de a=', a)
Valor de a= 12
>>> print('Valor de a = {0} e valor de b = {1}'.format(a, b))
Valor de a = 12 e valor de b = 19
>>> print(a, b, sep = '-')
12-19
>>> print(a, b, sep = ', ')
12, 19

>>> dado = 9
>>> print('Dado = {0:d}'.format(dado))
Dado = 9
>>> print('Dado = {0:5}'.format(dado))
Dado =     9
>>> print('Dado = {0:f}'.format(dado))
Dado = 9.000000
>>> print('Dado = {0:2f}'.format(dado))
Dado = 9.000000
>>> print('Dado = {0:.2f}'.format(dado))
Dado = 9.00
>>> print('Dado = {0:6.3f}'.format(dado))
Dado =  9.000
>>> print('qq{:7d}qq'.format(dado))
qq      9qq
>>> print('qq{:<7d}qq'.format(dado))
qq9      qq
>>> print('qq{:^7d}qq'.format(dado))
qq   9   qq
>>> 

>>> x = input('Digite algo: ')
Digite algo: pizza de sardinha
>>> x
'pizza de sardinha'
>>> n = print('Digite um número inteiro: ')
Digite um número inteiro: 
>>> n = input('Digite um número inteiro: ')
Digite um número inteiro: 2
>>> n
'2'
>>> type(n)
<class 'str'>
>>> f = input('Digite um número real: ')
Digite um número real: 2.55
>>> f
'2.55'
>>> type(f)
<class 'str'>
>>> a = int(n)
>>> type(a)
<class 'int'>
>>> a
2
>>> b = float(f)
>>> b
2.55
>>> type(b)
<class 'float'>
>>> c = a + b
>>> print(c)
4.55
>>> s = str(c)
>>> print(s)
4.55
>>> type(s)
<class 'str'>
"""
