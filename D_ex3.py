# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

x = int(input())
text = ''
for i in range(1,10):
    text = text + str(x*i) + ' '
text = text[:-1]

print (text)