"""あなたは2つの文字列の長さを目で比較していましたが長い文字では目視で確認するのが辛くなってきました。
2つの文字列が入力されるので文字列の長さが一致していれば "Yes" 、違う場合は "No" と出力するプログラムを作成してください。

入力例 1 の場合

Paiza
Pizza
それぞれの文字列の長さは 5 文字なので以下のように出力して下さい。

Yes

入力例1
Paiza
Pizza

出力例1
Yes
"""

# 入力例の「Paiza」と「Pizza」の"文字数が同じ"ならYesと表示させる。
# 文字では無く「文字数」が一致。

# x = "Paiza"
# y = "Pizza"

# x = "Coding"
# y = "Programming"

x = input()
y = input()

if len(x) == len(y):
    print("Yes")
elif len(x) != len(y):
    print("No")
