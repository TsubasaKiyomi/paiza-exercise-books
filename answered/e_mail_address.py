"""
D010:Eメールアドレス

Eメールアドレスはローカル部とドメインを「@」を繋いだ文字列で表されます。

ローカル部を s ,ドメインを t として、それぞれ長さ n の文字列が改行区切りで入力されます。

以下の構文に沿った文字列を出力してください。

s(ローカル部)@t(ドメイン)

例えば
info
paiza.jp
のような入力の場合

info@paiza.jp
と出力して下さい。

入力例1
paiza
example.com
出力例1
paiza@example.com
入力例2
paiza.tarou2015
paiza.jp
出力例2
paiza.tarou2015@paiza.jp
"""

# a = input()
# b = input()

a = "paiza"
b = "example.com"

print(a + "@" + b)
