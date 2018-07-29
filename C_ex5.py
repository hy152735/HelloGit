# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = int(input())
for i in range(input_lines):
    ipList = input().rstrip().split('.')
    ans = 'True'

    for ipaddr in ipList:
        # nullチェック
        if ipaddr == '':
            ans = 'False'
            continue

        if (0 > int(ipaddr) or int(ipaddr) > 255):
            ans = 'False'
    print (ans)