"""

D055:ワインのキャッチコピー

あなたはあるワインの銘柄のマーケティングを担当しています。良いキャッチコピーを考えるため、とりあえず「〜の中で最高」というフレーズを色々作ってみることにしました。

2 つの文字列が与えられるので、"Best in" とそれらの文字列をすべて半角スペース区切りで結合して出力してください。


例)

hundred years → Best in hundred years

the universe → Best in the universe

入力例1
a decade
出力例1
Best in a decade
入力例2
the world
出力例2
Best in the world
入力例3
history ever
出力例3
Best in history ever
"""


# a = input()
a = "a decade"
x = ("Best in " + a)
print(x)
