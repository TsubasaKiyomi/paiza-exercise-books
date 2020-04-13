"""
D033:頭文字

あなたは半角アルファベットの苗字と名前からそれぞれ 1文字目を取りイニシャルを作ることにしました。
半角スペース区切りで苗字と名前が入力されるので、1文字目を取り "." (半角ドット)で区切った文字列を出力してください。

例えば以下の様な入力の場合
Paiza Tarou
以下の様に出力してください
P.T
入力例1 Midorikawa Tsubame

出力例1 M.T

入力例2 Paiza Tarou

出力例2 P.T
"""

# capitalizeされている文字を"."で区切り出力する。
# import re
# a = "Paiza Tarou"
name_list = "Midorikawa Tsubame"


name = name_list
rename = name.split(" ")
re_name_1 = ".".join(list(map(lambda item: item[0], rename)))
print(re_name_1)

# str = " "
# list = ["a", "b", "c"]
# print("".join(list))


# name = a
# rename = name.split(" ")
# re_name_1 = ".".join(list(map(lambda item: item[0], rename)))
# print(re_name_1)
