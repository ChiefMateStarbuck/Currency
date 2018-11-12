import sys

if len(sys.argv) > 1:
    begin = sys.argv[1]
    end = sys.argv[2]
    amount = float(sys.argv[3])
else:
    begin = 'ISK'
    end = 'JPY'
    amount = 90

def exchange(load, begin, end, amount):
    fringe = []
    visited = []
    fringe.append(load[begin][1:])
     
    while fringe:
        top = fringe.pop(0)
        visited.append(top[0])
        temp_children = load[top[0]][1:]
        
        for child in temp_children:

            if child[0] == end:
                conversion = []
                conversion.extend(load[top[0]][0])
                conversion.append(top[1])
                conversion.append(child[1])

                for con in conversion:
                    amount *= con
                return con

            if child[0] not in visited and child[0] in load: 
                fringe.append(child)
                load[child[0]][0].extend(load[top[0]][0])
                load[child[0]][0].append(top[1])
                load[child[0]][1] = top[0]
                    
    return -1

file = open('exchange.txt', 'r')

load = {}

for line in file:
    line_list =  line.split(',')
    line_list[2] = line_list[2][:-1]
   
    if line_list[0] not in load:
        # The first element in the map is a list which will hold the conversion rates 
        # of the current path. (I will be implementing a Breadth First Search to find the path)
        load[line_list[0]] = [[]]
    
    """
    The map will look like this:

    'JMD': [[],['RUB',8.2],['USD,.6]]
    'RUB':[[], ['JPY',1.9]]
    etc ..

    """
    load[line_list[0]].append([line_list[1], float(line_list[2])]) 

end_amount = exchange(load, begin, end, amount)

if end_amount == -1:
    print('No Soulution Found!!')
else:
    print('Beginning currency {}'.format(begin))
    print('Begnning amount {}'.format(amount))
    print('End currency {}'.format(end))
    print('End amount {}'.format(end_amount))