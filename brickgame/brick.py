#!/usr/bin/python3

class State:
    def __init__(self, value, opt_score, opt_steps):
        self.value = value 
        self.opt_score = opt_score 
        self.opt_steps = opt_steps 
    
    def __str__(self):
        return str(self.value)

    def __repr__(self): # for the printing of elements in a list
        return str(self.value)

def main():
    in_data = input("Input to the BricksGame, example 1 2 3 4 5 : \n")
    arr = list(map(int, in_data.split(" "))) # TODO: add error handling 
    
    N = len(arr)
    for i in range(N-1, -1, -1):
        v = arr[i] # save value
        opt_score, opt_steps = get_opt(v, i, arr, N)
        arr[i] = State(v, opt_score, opt_steps)     # save each state in the same list 
        
    print("Maximum score = ", arr[0].opt_score)


def get_opt(value, index, arr, N):
    opt_score = value
    opt_steps = 1
    if index == N - 1: # one element left 
        pass
    elif index >= N-3: # three or less elemnts left
        opt_score += arr[index+1].opt_score
        opt_steps += arr[index+1].opt_steps
    else:
        # we can choose to remove 1, 2 or 3 bricks
        score = []
        for num_bricks in range(1,4):
            s = 0 
            for i in range(1, num_bricks):
                s += arr[index + i].value
            opponents_move = arr[index+num_bricks].opt_steps 
            next_index = opponents_move + index + num_bricks 
            if next_index < N:
                s += arr[next_index].opt_score
            score.append(s)
        opt_score += max(score)
        opt_steps += score.index(max(score))

    return opt_score, opt_steps



main()
