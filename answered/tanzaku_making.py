"""
 D099:短冊づくり
 7月7日は七夕です。
あなたは短冊を印刷するプログラムを作成することにしました。

文字列 S が入力されるので1文字ずつ改行し縦書きに出力して下さい。

例えば以下のような入力の場合

paiza
以下のように出力して下さい

p
a
i
z
a

入力例1
paiza
出力例1
p
a
i
z
a
入力例2
coding
出力例2
c
o
d
i
n
g



"""

# a = input()
a = "paiza"
b = a.split()

for i in b[0]:
    print(i)
