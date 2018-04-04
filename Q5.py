'''
- Smallest multiple -
"2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
(https://projecteuler.net/problem=5)
'''


def getgcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

lcm=1
for i in range(1, 21):
    gcd = getgcd(lcm, i)
    lcm = lcm*i/gcd
print(i,gcd,lcm)

int
n = 20;
int
c = 1;

num = 1
