"""
D123:自動でチャージ
電子決済サービス Paiza Pay は、残高が 10,000 円を切っていると自動で 10,000 円をチャージするサービスを始めることになりました。

残高が入力されるので、チャージするべきかどうか判断をし、チャージする場合はチャージ後の残高、必要ない場合はそのままの残高を出力してください。

入力例1
2980
出力例1
12980
入力例2
15000
出力例2
15000
"""

a = 2
# a = input
# 変数aに入っている金額が10000を切ったら +10000円チャージする。


def if_num(a):
    if a < 10000:
        print(a + 10000)
    elif a > 10000:
        print(a)


if_num(a)
