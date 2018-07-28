# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = int(input())
for i in range(input_lines):
    x = int(input().rstrip())
    moji = ' is not a leap year'
    if (x % 4 == 0):
        moji = ' is a leap year'
        if (x % 100 == 0):
            moji = ' is not a leap year'
            if (x % 400 == 0):
                moji = ' is a leap year'

    print(str(x) + moji)
