menu = {
    
    'antelope' : ['grass'],
    'big-fish' : ['little-fish'],
    'bug' : ['leaves'],
    'bear' : ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
    'chicken' : ['bug'],
    'cow' : ['grass'],
    'fox' : ['chicken', 'sheep'],
    'giraffe' : ['leaves'],
    'lion' : ['antelope', 'cow'],
    'panda' : ['leaves'],
    'sheep' : ['grass'],

}


def who_eats_who(zoo):
    
    result = [zoo]
    zoo = zoo.split(',')
    i = 0
    

    while is_sorted(zoo) == False:
        eater = zoo[i]
        changed = False
        if eater not in menu.keys():
            i += 1
        else:
            if i in range(1, len(zoo)):
                food = zoo[i-1]

                if food in menu[eater]:
                    result.append(f'{eater} eats {food}')
                    del zoo[i-1]
                    changed = True
                    i = 0
                    continue
            
            if i in range(0, len(zoo)-1):
                food = zoo[i+1]

                if food in menu[eater]:
                    result.append(f'{eater} eats {food}')
                    del zoo[i+1]
                    changed = True

                    
            if changed == False:
                i += 1
            else:
                i = 0

    result.append(','.join(zoo))
    print(zoo)
    print(result)
    return result

def is_sorted(zoo):
    
    for i in range(len(zoo)):
        eater = zoo[i]
        if eater not in menu.keys():
            continue
        if i in range(1, len(zoo)+1):
            food = zoo[i-1]
            if food in menu[eater]:
                return False
            
        if i in range(0, len(zoo)-1):
            food = zoo[i+1]
            if food in menu[eater]:
                return False

    return True