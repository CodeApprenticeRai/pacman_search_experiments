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
import heapq

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


    startingState = problem.getStartState()
    actionHistory = []
    visited = []

    return _depthFirstSearch( startingState, actionHistory, visited, problem )


def _depthFirstSearch( currentState, actionHistory, visited, problem ):
    # print currentPoint
    if problem.isGoalState( currentState ):
        return actionHistory

    visited.append( currentState )

    # print problem.getSuccessors( currentPoint )
    for successor in problem.getSuccessors( currentState ):
        if successor[0] not in visited:
            actionHistory.append( successor[1] )

            solution_candidate = _depthFirstSearch( successor[0], actionHistory, visited, problem)

            if ( len(solution_candidate) > 0 ):
                return solution_candidate

            actionHistory.pop()

    return []


def breadthFirstSearch(problem):
    startingState = problem.getStartState()
    queue = util.Queue() #deque( (startingState, []) )  #
    queue.push( (startingState, []) )
    visited = []

    while (True):
        currentState, currentStateActionHistory = queue.pop()

        if currentState not in visited:
            visited.append( currentState )

            #print(currentState, currentStateActionHistory )

            if problem.isGoalState( currentState ):
                return currentStateActionHistory

            for successor in problem.getSuccessors( currentState ):
                # if successor[0] not in visited:
                queue.push( ( successor[0], currentStateActionHistory + [ successor[1] ] )  )



    raise AssertionError("The problem is malformed. Problem has no solution.")


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    heap = []
    startingState = problem.getStartState()
    visited = []

    heapq.heappush(heap, ( 0, id(startingState), startingState, [] ) )

    while( True ):
        accumulatedCost, priorityTieBreaker, currentState, currentStateActionHistory = heapq.heappop(heap)

        if currentState not in visited:
            visited.append( currentState )

            if problem.isGoalState( currentState ):
                return currentStateActionHistory

            for successor in problem.getSuccessors( currentState ):
                heapq.heappush(heap, ( accumulatedCost + successor[2], id(successor[0]), successor[0], currentStateActionHistory + [ successor[1] ] )  )

    raise AssertionError("The problem is malformed. It does not have a solution.")

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #heap = []
    heap = util.PriorityQueue()
    startingState = problem.getStartState()
    visited = []


    #heapq.heappush(heap, ( 0, id(startingState), startingState, [] ) )
    heap.push( ( 0, startingState, [] ),  0  )
    while( True ):
        accumulatedCost, currentState, currentStateActionHistory = heap.pop() #heapq.heappop(heap)

        if currentState not in visited:
            visited.append( currentState )

            if problem.isGoalState( currentState ):
                return currentStateActionHistory

            for successor in problem.getSuccessors( currentState ):
                #heapq.heappush(heap, ( accumulatedCost + successor[2] + heuristic( successor[0], problem ), id(successor[0]), successor[0], currentStateActionHistory + [ successor[1] ] )  )
                successorAccumulatedCost = accumulatedCost + successor[2]
                successorHeuristicCost = successorAccumulatedCost + heuristic( successor[0], problem )
                heap.push( ( successorAccumulatedCost, successor[0], currentStateActionHistory + [ successor[1] ] ), successorHeuristicCost  )

    raise AssertionError("The problem is malformed. It does not have a solution.")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
