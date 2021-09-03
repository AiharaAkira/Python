import random

chance = 4
answer = random.randrange(1, 20)
challenge = 0
answer_player = -1

while(chance > challenge and answer != answer_player):


    answer_player = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance-challenge)))
    challenge += 1

    if(answer > answer_player):
        print("Up")
    elif(answer < answer_player):
        print("Down")
if(answer == answer_player):
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(challenge))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(answer))