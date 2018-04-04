'''
- Sum square difference -
"The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."
(https://projecteuler.net/problem=6)
'''

total = 0
totalsq =0
for i in range(1, 101):
    totalsq = totalsq + i **2
    total = total + i
print(totalsq, total, total**2)
print(total**2-totalsq)