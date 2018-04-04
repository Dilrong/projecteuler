'''
- Largest prime factor -
"The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"
(https://projecteuler.net/problem=3)
'''

x = 600851475143
d = 2

while d <= x:
    if x % d == 0:
        print(d)
        x = x / d
    else:
        d = d + 1