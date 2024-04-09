# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    # Initialize the stack to keep track of nodes to explore
    stack = util.Stack()
    # Initialize a set to keep track of visited states
    visited = set()
    # Push the start state onto the stack along with an empty list of actions
    stack.push((problem.getStartState(), []))

    # Perform DFS
    while not stack.isEmpty():
        # Pop the top node from the stack
        current_state, actions = stack.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(current_state):
            return actions

        # Check if the current state has already been visited
        if current_state not in visited:
            # Mark the current state as visited
            visited.add(current_state)
            # Get successors of the current state
            successors = problem.getSuccessors(current_state)
            # Push each successor onto the stack with the corresponding actions
            for successor, action, _ in successors:
                stack.push((successor, actions + [action]))

    # If no solution found
    return []

from util import Queue

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # Initialize an empty queue for the frontier and a set for explored nodes
    frontier = Queue()
    explored = set()

    # Add the start state to the frontier with an empty path
    frontier.push((problem.getStartState(), []))

    while not frontier.isEmpty():
        # Pop a node from the frontier
        node, path = frontier.pop()

        # If this node is the goal, then we have found a solution
        if problem.isGoalState(node):
            return path

        # Mark the node as explored
        explored.add(node)

        # Add neighbors to the frontier
        for neighbor, direction, _ in problem.getSuccessors(node):
            if neighbor not in explored and neighbor not in (n for n, _ in frontier.list):
                frontier.push((neighbor, path + [direction]))

    # If no solution was found, return an empty path
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    explored = set()

    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)

    while not frontier.isEmpty():
        current_state, actions, cost = frontier.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in explored:
            explored.add(current_state)
            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                frontier.push((successor, new_actions, new_cost), new_cost)

    return []



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch