# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

defnum = input().rstrip().split(' ')
input_lines = int(defnum[0])
r = int(defnum[1])

text = ''
for i in range(input_lines):
    s = input().rstrip().split(' ')

    if (min([int(s[0]), int(s[1]), int(s[2])]) >= r * 2):
        print (i + 1)