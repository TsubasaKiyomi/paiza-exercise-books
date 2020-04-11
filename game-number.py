"""
あなたの通う Paiza 小学校では、10 回同じ単語を言った後にひっかけクイズに答える十回ゲームの変則版である N 回ゲームがはやっています。
N 回ゲームでは、 N 回同じ単語を言った後にクイズに答えます。

そこで、言うべき単語と繰り返すべき回数が与えられるのでクイズに答える前に発言すべき文字列を出力してください。

入力例1
3
elbow
出力例1
elbowelbowelbow
"""

# 指定回数をループさせる。　指定回数は「３回」
# いうべき単語は「elbowe」　出力例　「elbowelbowelbow」

# a = 3
# b = "elbow"

a = input()
b = input()


for elbows in range(1):
    if b == 0:
        break
    print(b * int(a))
