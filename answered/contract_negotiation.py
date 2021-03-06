"""
D137:契約の交渉
あなたはある会社と取引をしていて、先日 10 個の要求を提出したところ、ちょうど今要求の可否を書いた紙が送られてきました。
その紙には相手方が承諾した要求については yes の頭文字 "y"、承諾しなかった要求については no の頭文字 "n" として、"y" と "n" のみが 10 個並んでいました。

このとき、いくつの要求が承諾されたかを返すプログラムを作成してください。

例えば、入力例 1 では相手方の返答が "yyyynnnnny" なので承諾された要求は 5 つであり、5 を表示します。

入力例1
yyyynnnnny
出力例1
5
入力例2
nnnnnnnnnn
出力例2
0
"""


# a = input()
a = "yyyynnnnny"

# ['y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'y']リストで分ける
c = [str(i) for i in a]

# "y"の文字を選出する
print(a.count("y"))
