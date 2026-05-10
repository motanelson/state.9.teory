import time

def state9_change(state9):
    state9=state9+1
    if state9 >8:
        state9=0
    return state9     


print("\033c\033[40;37m\nemulator of a state9\n")
states=0
for a in range (20):
     print(states)
     states=state9_change(states)
     
