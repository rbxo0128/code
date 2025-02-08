from itertools import combinations
def solution(coin, cards):
    c = len(cards)
    s = c//3
    dess = c-s
    
    rounds=1
    card = cards[0:s]
    while cards:
        isbool = False
        deck = cards[0:s+2]
        arr = list(combinations(deck,2))
        for j in arr:
            if sum(j) == c+1:
                count = len(set(card) & set(j))
                result = len(j) - count
                if result <= coin:
                    cards.remove(j[0])
                    cards.remove(j[1])
                    coin -= result
                    isbool = True
                    break
            
        if not isbool:
            break
        else:
            rounds+=1
            if rounds == dess//2+1:
                break
        
        
    
    answer = 0
    return rounds