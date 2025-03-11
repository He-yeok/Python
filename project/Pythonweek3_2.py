import random

answer = random.randint(0,100)
min = 0; max= 99

for i in range(10): 
    guess = int(input('숫자를 입력하세요. 10번의 기회가 있습니다. (범위:%d ~%d): '%(min,max)))
    if answer == guess:
        print('\n정답입니다. %d번만에 맞추셨습니다.\n게임이 끝났습니다.'%i)
        break
    elif answer > guess:
        print('아닙니다. 더 큰 숫자 입니다!' )
        min = guess
    else:
        print('아닙니다. 더 작은 숫자 입니다!' )
        max = guess
    if i == 10:
        print('\n주어진 기회를 다 소모하셨습니다. \n게임이 끝났습니다.')
