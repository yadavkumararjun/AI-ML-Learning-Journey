from collections import deque

# Jug capacities
A_CAPACITY = 6
B_CAPACITY = 3

# Goal: 2 liters in Jug A
GOAL = 2


def get_next_states(state):
    a, b = state
    next_states = []

    # 1. Fill Jug A
    next_states.append((A_CAPACITY, b))

    # 2. Fill Jug B
    next_states.append((a, B_CAPACITY))

    # 3. Empty Jug A
    next_states.append((0, b))

    # 4. Empty Jug B
    next_states.append((a, 0))

    # 5. Pour A -> B
    transfer = min(a, B_CAPACITY - b)
    next_states.append((a - transfer, b + transfer))

    # 6. Pour B -> A
    transfer = min(b, A_CAPACITY - a)
    next_states.append((a + transfer, b - transfer))

    return next_states


def bfs():
    start = (0, 0)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        a, b = current

        if a == GOAL:
            return path

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


solution = bfs()

if solution:
    print("Solution Found:\n")
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
    print(f"\nGoal Reached! Jug A contains {GOAL} liters.")
else:
    print("No solution exists.")