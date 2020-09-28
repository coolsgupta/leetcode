from collections import deque
from queue import PriorityQueue
import sys
#import traceback
#import time


class PathFinder:
    def __init__(self, data):
        self.input = data
        self.R = len(self.input)
        self.C = len(self.input[0])
        self.ACTIONS_MAP = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        self.entrance_location = None
        self.goal_location = None
        self.set_of_valid_points = {}
        self.create_graph()
        self.adjacency_map = {
            self.entrance_location: (-1, -1)
        }
        self.reached_goal = False
        self.path = []

    def create_graph(self):
        set_of_valid_points = set()
        for i in range(self.R):
            for j in range(self.C):
                if self.input[i][j] in ['.', 'S', 'E', 's', 'e']:
                    set_of_valid_points.add((i, j))

                    if self.input[i][j] in ['S', 's']:
                        start = (i, j)

                    if self.input[i][j] in ['E', 'e']:
                        goal = (i, j)

        self.set_of_valid_points = set_of_valid_points
        self.entrance_location = start
        self.goal_location = goal

    def add_action_step(self, current_point, action):
        return tuple(map(lambda i, j: i + j, current_point, action))

    def find_reachable_points(self, current_point):
        reachable_points_from_action = {}
        for action in self.ACTIONS_MAP:
            next_state = self.add_action_step(current_point, action)

            if next_state in self.set_of_valid_points:
                reachable_points_from_action[next_state] = current_point

        return reachable_points_from_action

    def backtrack_path(self):
        current_state = self.goal_location
        traced_path = deque()
        traced_path.append(self.goal_location)

        while current_state != self.entrance_location:
            current_state = self.adjacency_map.get(current_state, (-1,-1))
            traced_path.append(current_state)

        self.path = traced_path

    def find_path(self):
        visited, bfs_queue = {self.entrance_location}, deque()
        bfs_queue.append(self.entrance_location)

        while bfs_queue:
            current_state = bfs_queue.popleft()

            if current_state == self.goal_location:
                self.reached_goal = True
                break

            reachable_states = self.find_reachable_points(
                current_state
            )

            for state in reachable_states:
                if state not in visited:
                    visited.add(state)
                    self.adjacency_map[state] = reachable_states[state]
                    bfs_queue.append(state)

        if self.reached_goal:
            self.backtrack_path()

        else:
            raise Exception('Path not found')

    def print_output(self, fail=False):
        if fail:
            print('Trapped')

        else:
            for i in range(self.R):
                line = ''
                for j in range(self.C):
                    if (i, j) == self.goal_location:
                        line += 'E'

                    elif (i, j) == self.entrance_location:
                        line += 'S'

                    elif (i, j) in self.path:
                        line += '*'

                    elif (i, j) in self.set_of_valid_points:
                        line += '.'

                    else:
                        line += '#'

                print(line)


if __name__ == '__main__':
    formatted_input = []
    for line in sys.stdin:
        formatted_input.append(list(line))

    finder = PathFinder(formatted_input)
    try:
        finder.find_path()
        finder.print_output()

    except:
        finder.print_output(fail=True)
