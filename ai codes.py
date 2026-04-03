# A*
tree = {
    'S': [['A', 2], ['B', 5]],
    'A': [['C', 4], ['D', 1]],
    'B': [['E', 2], ['F', 6]],
    'C': [['G', 3]],
    'D': [['H', 7], ['I', 2]],
    'E': [['J', 1]],
    'F': [],
    'G': [],
    'H': [],
    'I': [['K', 5]],
    'J': [],
    'K': []
}

goal = "H"
tcost = 0
op = [["S",0]]
clo = []

def get_lowest():
    best = op[0]
    for n in op:
        if n[1] < best[1]: best = n
    
    op.remove(best)
    return best

def a8():
    while op:
        node,cost = get_lowest()
        print(node)
        clo.append(node)

        if node == goal:
            print("goal reached")
            print(f"total cost: {tcost}")
            return
        
        for child,chcost in tree[node]:
            if child not in clo:
                op.append([child,cost+chcost])


# GREEDY
goal = "H"
OPEN = [["S",0]]
CLOSED = []

def get_lowest():
    cost = 9999
    small = ""

    for n in OPEN:
        if n[1] < cost and n[0] not in CLOSED:
            small = n
            cost = n[1]
    
    return small

def check_neighbors(x):
    for n in tree[x]:
        if n not in CLOSED:
            OPEN.append(n)

def greedy():
    curr = get_lowest()
    print(curr[0])

    OPEN.remove(curr)
    CLOSED.append(curr[0])

    if curr[0] == goal:
        print("goal reached")
        return True
    
    check_neighbors(curr[0])
    greedy()


# Bredth First Search
goal = "H"
OPEN = ["S"]
CLOSED = []

def check_neighbors(x):
    for n in tree[x]:
        if n not in CLOSED and n not in OPEN:
            OPEN.append(n)

def bfs():
    curr = OPEN[0]
    print(curr)
    OPEN.remove(curr)
    CLOSED.append(curr)

    if curr == goal:
        print("reached goal")
        return True
    
    check_neighbors(curr)
    bfs()


# Limited DFS
tree = {
    'S': ['A','B'],
    'A': ['C','D'],
    'B': ['E','F'],
    'C': ['G'],
    'D': ['H','I'],
    'E': ['J'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['K'],
    'J': [],
    'K': []
}

goal = "H"
OPEN = ["S"]
CLOSED = []

def check_neighbor(curr):
    for n in tree[curr]:
        if n not in CLOSED and n not in OPEN:
            OPEN.insert(0,n)

def dfs(limit,depth=0):
    curr = OPEN[0]
    print(curr)

    if curr == goal:
        print("goal reached")
        return True
    
    if depth == limit:
        return False
    
    check_neighbor(curr)
    OPEN.remove(curr)
    
    if dfs(limit,depth+1) == True:
        return True
    
    return False

dfs(10)


# Hill Climb
tree = {
    'S': [['A', 2], ['B', 5]],
    'A': [['C', 4], ['D', 1]],
    'B': [['E', 2], ['F', 6]],
    'C': [['G', 3]],
    'D': [['H', 7], ['I', 2]],
    'E': [['J', 1]],
    'F': [],
    'G': [],
    'H': [],
    'I': [['K', 5]],
    'J': [],
    'K': []
}

OPEN = ["S"]
CLOSED = []

def get_next(curr):
    lst = tree[curr[0]]
    if not lst: return None

    best = lst[0]

    for n in lst:
        if n[1] < best[1]: best = n
    
    if best[1] < curr[1]: return best
    else: return curr

def hill_climb(curr=["S",10]):
    if curr == None: return
    print(curr[0])
    next = get_next(curr)
    if next == curr: return
    else: hill_climb(next)

hill_climb()


# Beam Search
tree = {
    'S': [['A', 2], ['B', 5]],
    'A': [['C', 4], ['D', 1]],
    'B': [['E', 2], ['F', 6]],
    'C': [['G', 3]],
    'D': [['H', 7], ['I', 2]],
    'E': [['J', 1]],
    'F': [],
    'G': [],
    'H': [],
    'I': [['K', 5]],
    'J': [],
    'K': []
}

def simple_beam(start, k):
    beam = [([start], 0)]

    while True:
        new_beam = []

        for path, cost in beam:
            current = path[-1]
            neighbors = tree[current]

            if not neighbors:
                new_beam.append((path, cost))
            else:
                for node, edge_cost in neighbors:
                    new_beam.append((path + [node], cost + edge_cost))

        new_beam.sort(key=lambda x: x[1])
        beam = new_beam[:k]

        if all(len(tree[path[-1]]) == 0 for path, _ in beam):
            break

    return beam

result = simple_beam('S', 2)
for path, cost in result:
    print("Path:", path, "Cost:", cost)


# GENETIC ALGORITHM
import random

TARGET = "10101"
POP_SIZE = 20
MUTATION_RATE = 0.1
GENERATIONS = 100

def random_individual():
    return ''.join(random.choice('01') for _ in range(len(TARGET)))

def fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

def select(population):
    return sorted(population, key=fitness, reverse=True)[:2]

def crossover(p1, p2):
    point = random.randint(0, len(TARGET) - 1)
    return p1[:point] + p2[point:]

def mutate(individual):
    return ''.join(
        c if random.random() > MUTATION_RATE else random.choice('01')
        for c in individual
    )

population = [random_individual() for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    best = max(population, key=fitness)
    print(f"Gen {gen}: {best} ({fitness(best)})")

    if best == TARGET:
        break

    p1, p2 = select(population)

    population = [
        mutate(crossover(p1, p2))
        for _ in range(POP_SIZE)
    ]


# A*
goal = (4,4)

def is_wall(node):
    return node in [(0,1),(1,1),(3,1),(2,3),(3,2),(3,3)]

def heuristic(node):
    return abs(goal[0]-node[0]) + abs(goal[1]-node[1])

OPEN = [((0,0), 0)]  # (node, g cost)
CLOSED = []

def get_neighbors(node):
    x,y = node
    neighbors = []
    if x > 0: neighbors.append((x-1,y))
    if x < 4: neighbors.append((x+1,y))
    if y > 0: neighbors.append((x,y-1))
    if y < 4: neighbors.append((x,y+1))
    return neighbors

def a_star():
    while OPEN:
        OPEN.sort(key=lambda x:x[1] + heuristic(x[0]))
        
        curr, g = OPEN.pop(0)
        CLOSED.append(curr)
        
        print(f"Visiting: {curr}, g={g}, h={heuristic(curr)}, f={g + heuristic(curr)}")

        if curr == goal:
            print("Goal reached!")
            return
        
        for n in get_neighbors(curr):
            if n not in CLOSED or not is_wall(n):
                OPEN.append((n, g+1))       
            

a_star()