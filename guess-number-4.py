#!/usr/bin/python
# -*- coding:utf8 -*-
f = file('game.txt')
score = f.read().split()              #f.read读出来的是一个字符串（3个数据都在一起）
game_times = int(score[0]) #玩的次数      #数据读出来之后，分别存放在3个变量中
min_times = int(score[1])  #最少轮数      #Cautious:注意格式转化！注意格式转化！str→int
total_times = int(score[2]) #总轮数
if game_times > 0:
    avr_times = float(total_times)/game_times  #平均轮数
else:
    avr_times = 0
print'你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' %(game_times,min_times,avr_times)
f.close()

times = 0     #记录每次游戏所用次数，应该等于输入的次数
from random import randint  #记录玩的次数、最快猜出来的轮数、平均每次猜对所用次数
num = randint(1,100)
print 'Guess what I think?'
answer = input()
times += 1
result = False                 #这是布尔值，不是字符串
while result == False:
    if answer < 0:             #如果放在最后，那么第一次就输入负数是不能跳出循环的（4个if按顺序依次判断）；这样写比在>或<后面写简洁
        print'Exit Game'
        break
    if answer < num:
        print '%d is too small!' %answer
        times += 1
        answer = input()
    if answer > num:
        print str(answer) + ' is too big!'
        times += 1
        answer = input()
    if answer == num:
        print 'BINGO, %d is the right answer!' %answer
        result = True

game_times += 1
if game_times ==1 or min_times > times :       #两个可以合在一起写
    min_times = times
total_times += times
result = '%d %d %d' %(game_times,min_times,total_times)    #依旧保存为字符串！！
f = file('game.txt','w')
f.write(result)
f.close()