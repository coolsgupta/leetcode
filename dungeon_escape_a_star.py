from collections import deque
from queue import PriorityQueue
import sys
#import traceback
#import time


class Constants:
    LAST_STATE = 'last_state'
    ACTION_TAKEN_TO_REACH = 'action_taken_to_reach'
    COST_OF_LAST_STEP = 'cost_of_last_step'
    COST_TILL_CURRENT_STEP = 'cost_till_current_path'
    D1_dist = 10
    D2_dist = 14


class PathFinder:
    def __init__(self, data):
        self.input = data
        self.ACTIONS_MAP = {(1, 0),(-1, 0),(0, 1),(0,-1)}
        self.entrance_location = None
        self.goal_location = None
        self.set_of_valid_points = {}
        self.create_graph()
        self.adjacency_map = {
            self.entrance_location: {
                Constants.LAST_STATE: (-1, -1),
                Constants.ACTION_TAKEN_TO_REACH: -1,
                Constants.COST_OF_LAST_STEP: 0,
                Constants.COST_TILL_CURRENT_STEP: 0
            }
        }
        self.reached_goal = False
        self.path = []

    def create_graph(self):
        set_of_valid_points = set()
        R = len(self.input)
        C = len(self.input[0])
        for i in range(R):
            for j in range(C):
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
                cost_to_reach_from_last_state = 1
                reachable_points_from_action[next_state] = {
                    Constants.LAST_STATE: current_point,
                    Constants.ACTION_TAKEN_TO_REACH: action,
                    Constants.COST_OF_LAST_STEP: cost_to_reach_from_last_state,
                    Constants.COST_TILL_CURRENT_STEP: self.adjacency_map
                        .get(current_point, {}).get(Constants.COST_TILL_CURRENT_STEP, 0) + cost_to_reach_from_last_state
                }

        return reachable_points_from_action

    def backtrack_path(self):
        current_state = self.goal_location
        traced_path = deque()
        traced_path.append(self.goal_location)

        while current_state != self.entrance_location:
            current_state = self.adjacency_map.get(current_state, {}).get(Constants.LAST_STATE, (-1, -1))
            cost_to_reach = self.adjacency_map.get(current_state, {}).get(Constants.COST_OF_LAST_STEP, 0)
            traced_path.append(current_state)

        return traced_path, self.adjacency_map.get(self.goal_location, {}).get(Constants.COST_TILL_CURRENT_STEP, 0)

    def heuristic_function(self, state):
        return sum(map(lambda i, j: abs(i - j), state, self.goal_location))

    def find_path(self):
        visited, a_star_queue = {self.entrance_location}, PriorityQueue()
        a_star_queue.put((0, self.entrance_location))

        while not a_star_queue.empty():
            current_state = a_star_queue.get()[1]

            if current_state == self.goal_location:
                self.reached_goal = True
                break

            reachable_states = self.find_reachable_points(
                current_state
            )

            for state in reachable_states:
                if state not in visited or self.adjacency_map[state][Constants.COST_TILL_CURRENT_STEP] > reachable_states[state][Constants.COST_TILL_CURRENT_STEP]:
                    visited.add(state)
                    self.adjacency_map[state] = reachable_states[state]
                    a_star_queue.put(
                        (
                            reachable_states[state][Constants.COST_TILL_CURRENT_STEP] + self.heuristic_function(state),
                            state
                        )
                    )

        if self.reached_goal:
            traced_path, traced_path_cost = self.backtrack_path()
            self.path = traced_path

        else:
            raise Exception('Path not found')

    def print_output(self, fail=False):
        if fail:
            print('Trapped')
            # output = 'Trapped'

        else:
            # output = ''
            for i in range(len(self.input)):
                line = ''
                for j in range(len(self.input[0])):
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
                # output += line + '\n'
                print(line)

        # with open('cal_output2.txt', 'w') as res_file:
        #     res_file.write(output)


if __name__ == '__main__':
    # formatted_input = []
    # for line in sys.stdin:
    #     formatted_input.append(list(line))


    with open('input2.txt') as i_f:
        input_case = i_f.read()

    formatted_input = [list(x) for x in input_case.split('\n')]
    finder = PathFinder(formatted_input)
    try:
        finder.find_path()
        finder.print_output()
    except:
        finder.print_output(fail=True)