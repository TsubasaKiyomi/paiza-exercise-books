"""
D126:点数の計算

Paiza くんが参加するコーディングコンテストではコードの正確性、実行時間、綺麗さの 3 つの項目がそれぞれ 10 点満点で評価され、それらの合計点数が得点となります。

Paiza くんのコンテスト結果が、正確性、実行時間、きれいさの 3 つで与えられるので、彼の得点を出力してください。

ただし、各項目の点数は 0 以上の整数です。

入力例1
8 7 9
出力例1
24
入力例2
10 10 0
出力例2
20

"""

# a = input()
a = "8 7 9"
s = a.split()
x = int(s[0]) + int(s[1]) + int(s[2])
print(x)
