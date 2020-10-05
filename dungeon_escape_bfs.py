import sys


# find reachable states from current point
def find_reachable_points(current_point, ACTIONS_MAP):
    reachable_points_from_action = {}
    for action in ACTIONS_MAP:
        next_state = tuple(map(lambda i, j: i + j, current_point, action))

        if next_state in set_of_valid_points:
            reachable_points_from_action[next_state] = current_point

    return reachable_points_from_action


def create_environment(formatted_input, R, C):
    set_of_valid_points = set()
    for i in range(R):
        for j in range(C):
            if formatted_input[i][j] in ['.', 'S', 'E', 's', 'e']:
                set_of_valid_points.add((i, j))
                if formatted_input[i][j] in ['S', 's']:
                    entrance_location = (i, j)
                if formatted_input[i][j] in ['E', 'e']:
                    goal_location = (i, j)

    return set_of_valid_points, entrance_location, goal_location


def backtrack_path(entrance_location, goal_location, adjacency_map):
    current_state = goal_location
    traced_path = set()
    traced_path.add(goal_location)

    while current_state != entrance_location:
        current_state = adjacency_map.get(current_state, (-1, -1))
        traced_path.add(current_state)

    return traced_path


def bfs(entrance_location, goal_location, ACTIONS_MAP):
    # initialize the adjacency map
    adjacency_map = {
        entrance_location: (-1, -1)
    }

    visited, bfs_queue = {entrance_location}, []
    reached_goal = False
    bfs_queue.append(entrance_location)
    while bfs_queue:
        current_state = bfs_queue.pop(0)
        if current_state == goal_location:
            reached_goal = True
            break
        reachable_states = find_reachable_points(
            current_state, ACTIONS_MAP
        )
        for state in reachable_states:
            if state not in visited:
                visited.add(state)
                adjacency_map[state] = reachable_states[state]
                bfs_queue.append(state)

    if reached_goal:
        return reached_goal, backtrack_path(entrance_location, goal_location, adjacency_map)
    else:
        return reached_goal, []


# Read input on HireVuew
# formatted_input = []
# for line in sys.stdin:
#     formatted_input.append(list(line.strip()))

# this input is for testing on local machine
with open('input.txt') as i_f:
    input_case = i_f.read()

formatted_input = [list(x) for x in input_case.split('\n')]

# declare variables
R = len(formatted_input)
C = len(formatted_input[0])
ACTIONS_MAP = {(1, 0), (-1, 0), (0, 1), (0, -1)}

# create the set of reachable states
set_of_valid_points, entrance_location, goal_location = create_environment(formatted_input, R, C)

# starting BFS search
reached_goal, path = bfs(entrance_location, goal_location, ACTIONS_MAP)

# check if goal reached : print output accordingly
if reached_goal:
    for i in range(R):
        line = ''
        for j in range(C):
            if (i, j) == goal_location:
                line += 'E'
            elif (i, j) == entrance_location:
                line += 'S'
            elif (i, j) in path:
                line += '*'
            elif (i, j) in set_of_valid_points:
                line += '.'
            else:
                line += '#'
        print(line)

else:
    print('Trapped')
