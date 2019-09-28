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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    # print problem.getStartState()
    # print problem.getSuccessors(problem.getStartState())
    # util.raiseNotDefined()

    """


    startingPoint = problem.getStartState()
    actionHistory = []
    visited = {
        startingPoint[0] : { startingPoint[1]: True }
    }

    return _depthFirstSearch( startingPoint, actionHistory, visited, problem )

import copy

def _depthFirstSearch( currentPoint, actionHistory, visited, problem ):
    # print currentPoint
    if problem.isGoalState( currentPoint ):
        return actionHistory

    if currentPoint[0] not in visited:
        visited[currentPoint[0]] = {}
    if currentPoint[1] not in visited[currentPoint[0]]:
        visited[currentPoint[0]][currentPoint[1]] = True

    # print problem.getSuccessors( currentPoint )
    for successor in problem.getSuccessors( currentPoint ):
        if not ( (successor[0][0] in visited) and (successor[0][1] in visited[successor[0][0]]) ):
            actionHistory.append( successor[1] )
            solution_candidate = _depthFirstSearch(successor[0], actionHistory, visited, problem)

            if ( len(solution_candidate) > 0 ):
                return solution_candidate

            actionHistory.pop()

    return []


def breadthFirstSearch(problem):
    from collections import deque

    startingPoint = problem.getStartState()
    queue = deque([startingPoint]) #util.Queue()

    currentPoint = queue.popleft()
    visited = {}
    get_parent = { startingPoint[0] : { startingPoint[1]: None } }
    while( not problem.isGoalState( currentPoint )  ):
        if not currentPoint[0] in visited:
            visited[currentPoint[0]] = {}
        if not currentPoint[1] in visited[currentPoint[0]]:
            visited[currentPoint[0]][currentPoint[1]] = True

        for successor in problem.getSuccessors(currentPoint):
            if not ((successor[0][0] in visited) and (successor[0][1] in visited[successor[0][0]])):
                if not successor[0][0] in get_parent:
                    get_parent[successor[0][0]] = {}
                if not successor[0][1] in get_parent[successor[0][0]]:
                    _parent =  list( currentPoint )
                    _parent.append( successor[1] )
                    get_parent[successor[0][0]][successor[0][1]] =  _parent # get parent also contains the direction from parent
                queue.append( successor[0] ) # queue[i][3] == parent_point
        currentPoint = queue.popleft()

    # currentPoint == goal_state
    action_history = deque()
    parent = get_parent[currentPoint[0]][currentPoint[1]]
    print(currentPoint)
    while ( type(parent) != type(None) ):
        action_history.appendleft( parent[2] )
        parent = get_parent[parent[0]][parent[1]]

    return  action_history


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
