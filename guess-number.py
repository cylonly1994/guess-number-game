from random import randint
num = randint(1,100)
print 'Guess what I think?'
answer = input()
result = False                        #若False外要加""，则while里的也要加，这时其表示字符串而非布尔值
while result == False:
    if answer<num:
        print 'too small!'
        answer = input()
    if answer>num:
        print 'too big!'
        answer = input()
    if answer==num:
        print 'BINGO!'
        result = True
