import sys

n = int(sys.stdin.readline())

card_dict = {}
for i in range(n):
    card = int(sys.stdin.readline())
    if  card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

card_list = sorted(card_dict.items())
print(sorted(card_list, key=lambda x : (-x[1],x[0]))[0][0])