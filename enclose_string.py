"""
D107:文字列を囲う

あなたは入力された文字列 S をある文字 c で囲うプログラムを作ることになりました。
文字列 S と文字 c が改行区切りで与えられるので、文字列 S の前後を1文字ずつ文字 c で囲った文字列を出力して下さい。

例えば入力例 1 の場合

Paiza
X
以下のように出力して下さい。

XPaizaX

入力例1 Paiza
       X

出力例1 XPaizaX

入力例2 code
       C

出力例2 CcodeC
"""

# 入力された文字列　s を文字 c で囲う。
s = "Paiza"
c = "X"
# print(s)
# print(c)


def strings(x, y, z):
    return c + s + c


print(strings(c, s, c))
