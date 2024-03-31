# a = input("aの値を入力: ")
# b = input("bの値を入力: ")

# TODO
<<<<<<< HEAD
a = int(a)
b = int(b)

if a % 2 == 0:
    print("素数ではありません")
elif a == 1:
    print("素数ではありません")
else:
    print("素数です")

if b % 2 == 0:
    print("素数ではありません")
elif b == 1:
    print("素数ではありません")
else:
    print("素数です")
=======
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
>>>>>>> 61eac50c7235b2cf8421d34a41983b7e83c3b2ef
