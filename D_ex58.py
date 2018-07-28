# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

s = input().rstrip().split(' ')
text = ''
for i in range(int(s[0])):
    text = text + 'A'
for j in range(int(s[1])):
    text = text + 'B'
for k in range(int(s[2])):
    text = text + 'A'
print (text)