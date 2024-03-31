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
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
print(prime_number(n))