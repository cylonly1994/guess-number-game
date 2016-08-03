#!/usr/bin/python
# -*- coding:utf8 -*-
#多人玩游戏：仿照单人玩游戏：不同的是若没有这个人的数据时，需要将其添加到数据中

f = file('game.txt')
lines = f.readlines() #变成一个list，每个元素是每一行的内容，是字符串如：['zgl 0 0 0',...]
name = raw_input('请输入姓名的英文简称：')
scores = {} #用一个字典来记录所有的成绩，key为玩家姓名，value是由剩下的数据组成的数组（不是字符串）

#Codes below is vital:
for l in lines:
    s = l.split()  #不能写成lines[l]，因为l已经是每个元素了，不是序号！
    scores[s[0]] = s[1:] #给字典添加元素，键是姓名，其值为一个list
score = scores.get(name)
if score is None:
   score = [0, 0, 0]
f.close()

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times != 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print '你已经玩了：%d次，最少轮数：%d，平均轮数：%d' %(game_times, min_times, avg_times)

times = 0
from random import randint  #记录玩的次数、最快猜出来的轮数、平均每次猜对所用次数
num = randint(1,100)
print 'Guess what I think?'
answer = input()
times += 1
result = False                 #这是布尔值，不是字符串
while result == False:
    if answer < num:
        print '%d is too small!' %answer
        answer = input()
        times += 1
    if answer > num:
        print str(answer) + ' is too big!'
        answer = input()
        times += 1
    if answer == num:
        print 'BINGO, %d is the right answer!' %answer
        result = True

game_times += 1
if times < min_times or game_times == 1: #合一起写
    min_times = times
total_times += times

#接下来要保存数据了！
score[0] = str(game_times)  #int型要改成string型
score[1] = str(min_times)
score[2] = str(total_times)
scores[name] = score
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line

f = open('game.txt','w')
f.write(result)
f.close()