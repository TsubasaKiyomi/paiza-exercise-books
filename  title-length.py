"""
あなたは本の表紙を作っています。本の表紙は最大で10文字分の幅しかありません。
表紙に印刷する文字列 S が与えられるので 10 文字ごとに改行して出力するプログラムを作成してください。

例えば入力例 1 では
PaizaPaizaPaiza
と入力されるので
PaizaPaiza
Paiza
と出力してください。

入力例1
PaizaPaizaPaiza
出力例1
PaizaPaiza
Paiza
# titleの長さを出す。
# titleの長さは最大１０文字
# titleに対して１０文字ごとに\nを挿入し改行する。　＊分からない
# １１文字目に\nを記入する。　＊分からない
"""


# title_name = "PaizaPaizaPaiza"


# def cut_off_title():
#     cut_off = title_name
#     return cut_off


# result = cut_off_title()
# int(result).enplace("paizapaiza", "\npaiza")
# # \nでのやり方が分からなかったのでリストにして文字数を取得した。
# print(result)
# # print(result[10:])
# input_line = input()
# input = "PaizaPaizaPaiza"
input_line = "PaizaPaizaPaiza"

while(10 < len(input_line)):
    print(input_line[:10])
    input_line = input_line[10:]

print(input_line)
