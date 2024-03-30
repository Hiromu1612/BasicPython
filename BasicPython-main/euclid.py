a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
try:
    a = int(a)
    b = int(b)
except:
    print("aとbは整数で入力してください")
    
def euclid(a, b):
    if a < b:
        a, b = b, a
    else:
        a,b = a, b

    while b != 0: 
        a, b = b, a % b
    return a, b

a, _ = euclid(a, b)
print(f"最大公約数は{a}")


#問.4 互いに素であるか判定
def coprime(a, b):
    if euclid(a, b)[0] == 1:
        return True
    else:
        return False
print(coprime(a, b))



#エクストラ問題
import random

# 互いに素であった組の数を数える変数
count = 0

for _ in range(100000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if coprime(a, b):
        count += 1

probability = count / 100000

print(f"互いに素である確率は {probability}")