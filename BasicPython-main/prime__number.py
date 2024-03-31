# a = input("aの値を入力: ")
# b = input("bの値を入力: ")
# TODO
n = input("nの値を入力: ")
try:
    n = int(n)
except:
    print("nは整数で入力してください")
    exit()

def prime_number(n):
    if n < 2:
        return "素数ではありません"
    else:
        for i in range(2, n):
            if i == n-1:
                return True
            elif n % i == 0:
                return False

result = prime_number(n)
if result is None: #これがないと2がNoneになる
    result = True

print(result)