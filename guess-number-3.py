#!/usr/bin/python
# -*- coding:utf8 -*-
from random import randint
num = randint(1,100)
print 'Guess what I think?'
answer = input()
result = False                   #若False外要加""，则while里的也要加，这时其表示字符串而非布尔值
while result == False:
    if answer < 0:               #如果放在最后，那么第一次就输入负数是不能跳出循环的（4个if按顺序依次判断）；这样写比在>或<后面写简洁
        print'Exit Game'
        break
    if answer < num:
        print '%d is too small!' %answer
        answer = input()
    if answer > num:
        print str(answer) + ' is too big!'
        answer = input()
    if answer == num:
        print 'BINGO, %d is the right answer!' %answer
        result = True
