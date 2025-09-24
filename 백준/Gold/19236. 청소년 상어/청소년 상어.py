import sys
import copy

input = sys.stdin.readline

graph = []
fish = {}

for i in range(4):
    a,b,c,d,e,f,g,h = map(int, input().split())
    graph.append([a,c,e,g])
    if i != 0:
        fish[a] = (b-1,i,0)
    else:
        total = a
        fish[0] = (b-1,0,0)
    fish[c] = (d-1,i,1)
    fish[e] = (f-1,i,2)
    fish[g] = (h-1,i,3)

graph[0][0] = 0

dir_x = [-1,-1,0,1,1,1,0,-1]
dir_y = [0,-1,-1,-1,0,1,1,1]

result = []
def DFS(total,graph,fish):
    for i in range(1,17):
        if i in fish:
            dirs,x,y = fish[i]
            for j in range(8):
                dx,dy = dir_x[dirs], dir_y[dirs]
                sx,sy = x+dx,y+dy
                if 0<=sx<4 and 0<=sy<4 and graph[sx][sy] != 0:
                    if graph[sx][sy] == -1:
                        graph[sx][sy] = i
                        fish[i] = (dirs,sx,sy)
                        graph[x][y] = -1
                    else:
                        temp_fish = graph[sx][sy]
                        temp_dir, a,b = fish[temp_fish]
                        graph[sx][sy] = i
                        graph[x][y] = temp_fish
                        fish[i] = (dirs,sx,sy)
                        fish[temp_fish] = (temp_dir,x,y)
                    break
                else:
                    dirs = (dirs+1) % 8

    dirs,x,y = fish[0]
    dx,dy = dir_x[dirs], dir_y[dirs]
    is_move = False
    for i in range(1,4):
        sx, sy = x + dx*i, y + dy*i

        if 0<=sx<4 and 0<=sy<4:
            if graph[sx][sy] > 0:
                temp_fish = graph[sx][sy]
                temp_dir,a,b = fish[temp_fish]

                new_graph = copy.deepcopy(graph)
                new_fish = copy.deepcopy(fish)

                new_graph[x][y] = -1
                new_graph[sx][sy] = 0
                del new_fish[temp_fish]
                new_fish[0] = (temp_dir,sx,sy)

                DFS(total+temp_fish, new_graph, new_fish)
                is_move = True
            else:
                continue
        else:
            break

    if not is_move:
        result.append(total)

DFS(total,graph,fish)
print(max(result))