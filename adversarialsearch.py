from typing import Callable

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)


def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """

    startState = asp.get_start_state()
    player = startState.player_to_move()
    bestMove = None
    bestValue = float("-inf")

    for action in asp.get_available_actions(startState):
        nextState = asp.transition(startState, action)
        val = minVal(asp, nextState, player)
        if val > bestValue:
            bestMove = action
            bestValue = val
    return bestMove

def minVal(asp, state, player):
    if (asp.is_terminal_state(state)):
        return asp.evaluate_terminal(state)[player]
    val = float("inf")
    for action in asp.get_available_actions(state):
        newState = asp.transition(state, action)
        val = min(val, maxVal(asp, newState, player))
    return val

def maxVal(asp, state, player):
    if (asp.is_terminal_state(state)):
        return asp.evaluate_terminal(state)[player]
    val = float("-inf")
    for action in asp.get_available_actions(state):
        newState = asp.transition(state, action)
        val = max(val, minVal(asp, newState, player))
    return val

        

def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...


def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
