"""
D102:運賃の計算
あなたは単純な運賃計算のプログラムを作成しています。

その運賃計算は以下のルールで行われます。

・初乗り運賃 100 円
・1 区間ごとに 10 円ずつ加算

ある乗客の乗った区間数 N が与えられるので運賃がいくらかを出力するプログラムを作成してください。

例えば入力例 1の場合

3
3 区間乗ったので 100 + 3 × 10 という計算となるので、以下のように出力してください。

130
入力例1
3
出力例1
130
入力例2
19
出力例2
290
"""

# a = input()
a = 3
b = (int(a) * 10) + 100
print(b)
