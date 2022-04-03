def  game():
    return 69

score = game()
with open('D:\CODE\Python\highscore.txt') as f:
    hs = f.read()
    
if hs == '':
    with open('highscore.txt','w') as f:
        f.write(str(score))

elif int(hs)<score:
    with open('highscore.txt','w') as f:
        f.write(str(score))
