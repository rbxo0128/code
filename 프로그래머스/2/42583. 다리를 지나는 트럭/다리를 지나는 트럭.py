from collections import deque
def solution(bridge_length, weight, truck_weights):
    stack = deque([0 for i in range(bridge_length)])
    truck = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    time = 0
    while True:
        time+=1
        if(not stack):
            for i in range(bridge_length):
                stack[i] += 1
                bridge[i] += truck_weights[0]
        else:
            cur_stack = stack.popleft()
            cur_truck = truck.popleft()
            cur_bridge = bridge.popleft()
            stack.append(0)
            bridge.append(0)
            if cur_truck + cur_bridge > weight:
                truck.appendleft(cur_truck)
                
            else:
                if (cur_stack == bridge_length):
                    truck.appendleft(cur_truck)
                    continue
                
                for i in range(bridge_length-1):
                    bridge[i] += cur_truck
                    stack[i] += 1
                    
        if(not truck):
            break

        
        
        
        

    return time+bridge_length