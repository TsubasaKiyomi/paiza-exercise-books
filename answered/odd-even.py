"""
D008:奇数か偶数か

正の整数 N が入力されるので、N が奇数ならば"odd" 偶数ならば"even" と出力するプログラムを作成して下さい。
入力例1
4
出力例1
even
入力例2
5
出力例2
odd
入力例3
2
出力例3
even
"""
number = 6

# n(number部分)が偶数なら"even"奇数なら"odd"と表示させる
# paizaではint()にしないとエラーとなる
if int(number) % 2 == 0:
    print("even")
else:
    print("odd")
