def solution(keyinput, board):
    x = 0
    y = 0
    
    for i in keyinput:
        if x != -((board[0] - 1) / 2) and i == "left":
            x += -1
        elif x != (board[0] - 1) / 2 and i == "right":
            x += 1
        elif y != (board[1] - 1) / 2 and i == "up":
            y += 1
        elif y != -((board[1] - 1) / 2) and i == "down":
            y -= 1
        
        print(x,y)
    answer = [x, y]
    return answer