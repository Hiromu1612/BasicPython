# a = input("aの値を入力: ")
# b = input("bの値を入力: ")

# TODO
<<<<<<<<< Temporary merge branch 1
n = input("nの値を入力: ")
try:
    n = int(n)
except:
    print("nは整数で入力してください")

def prime_number(n):
    if n < 2:
        return "判定不可"
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            elif i == n-1:
                return True

print(prime_number(n))
=========
import math

n = int(input("nの値を入力: "))

if n <= 1:
    print("素数ではありません")
else:
    for i in range(2, math.isqrt(n) + 1): #2からその数の平方根までの全ての数で割り切れるかどうかを調べる
        if n % i == 0:
            print("素数ではありません")
            break
    else:
        print("素数です")
>>>>>>>>> Temporary merge branch 2
