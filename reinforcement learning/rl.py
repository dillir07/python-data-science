"""
Reinforcement Learning
reference: https://www.youtube.com/watch?v=psDlXfbe6ok
Status:In progress (https://youtu.be/psDlXfbe6ok?list=PLd_Oyt6lAQ8SwsLuJ912NiCagUSEa1lDx&t=7340)
TODO added QMatrix update
"""

# %%
import numpy as np
import random

# %%


class Agent:
    def __init__(self, i: int = 0, j: int = 0) -> None:
        self.i = i
        self.j = j

    @property
    def loc(self) -> tuple[int, int]:
        return (self.i, self.j)

    def vmove(self, direction: int):
        direction = 1 if direction > 0 else -1
        return Agent(self.i + direction, self.j)

    def hmove(self, direction: int):
        direction = 1 if direction > 0 else -1
        return Agent(self.i, self.j + direction)

    def __repr__(self) -> str:
        return str(self.loc)

# %%


class QMatrix:
    def __init__(self, nstates: int, nactions: int, learning_rate: float = 0.1, discount_factor: float = 1.0) -> None:
        self.q = np.zeros((nstates * nactions), dtype=float)
        self.lr = learning_rate
        self.g = discount_factor

    def updateQMatrix(self) -> None:
        """
        ref: https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686
        """
        pass

# %%


class Maze:
    """
    Maze
    ====

    States:
    ------
    0 means free
    -1 means not traversable
    1 means goal
    """

    def __init__(self, rows: int = 4, columns: int = 4) -> None:
        self.env = np.zeros((rows, columns), dtype=int)
        self.agent = Agent(0, 0)
        # Q matrix
        # --------
        # => no of possible status & no of possible actions
        # => states: (rows * columns), actions:(up, down, right, left)
        self.q = np.zeros((rows * columns, 4), dtype=float)

    def state_for_agent(self, agent: Agent) -> int:
        nr, nc = self.env.shape
        return (agent.i * nc) + agent.j

    def visualize(self) -> None:
        assert self.in_bounds(*(self.agent.loc)), "Agent is out of bounds"
        e = self.env.copy()
        e[self.agent.i, self.agent.j] = '9'
        print(e)

    def agent_in_bounds(self, agent: Agent) -> bool:
        return self.in_bounds(*(agent.loc))

    def agent_would_die(self, agent: Agent) -> bool:
        return self.env[agent.i, agent.j] == -1

    def in_bounds(self, r: int, c: int) -> bool:
        nr, nc = self.env.shape
        return 0 <= r < nr and 0 <= c < nc

    def compute_possible_moves(self) -> list[tuple[Agent, int]]:
        agent = self.agent
        agents = [
            agent.vmove(1),   # down  -> 0
            agent.vmove(-1),  # up    -> 1
            agent.hmove(1),   # right -> 2
            agent.hmove(-1)   # left  -> 3
        ]
        return [
            (agent, index) for (index, agent) in enumerate(agents)
            if self.is_new_agent_valid(agent)
        ]

    def has_won(self, agent: Agent) -> bool:
        return self.env[agent.i, agent.j] == 1

    def do_a_move(self, agent: Agent) -> float:
        assert self.is_new_agent_valid(agent), "Agent can't go there"
        self.agent = agent
        return 10.0 if self.has_won(agent) else -0.1

    def is_new_agent_valid(self, agent: Agent) -> bool:
        return self.agent_in_bounds(agent) and not self.agent_would_die(agent)


# %%


def make_test_maze():
    maze = Maze()
    e = maze.env
    e[3, 3] = 1
    e[0, 1: 3] = -1
    e[1, 2] = -1
    # e[2, 0] = -1
    e[3, 0: 2] = -1
    return maze

# %%


def main() -> None:
    m = make_test_maze()
    q = QMatrix(m.env.shape[0] * m.env.shape[1], 4, 0.1, 1.0)
    final_score: float = 0.0
    score: float = 0.0
    counter: int = 0
    while not m.has_won(m.agent):
        counter += 1
        moves = m.compute_possible_moves()
        random.shuffle(moves)  # shuffles inplace
        action, action_index = moves[0]
        previous_agent = m.state_for_agent(m.agent)
        score = m.do_a_move(action)  # state changes here
        new_state = m.state_for_agent(m.agent)
        final_score += score
        print('Iteration {}, score:{}, final score:{}'.format(
            counter, score, final_score))
        print("State:{}, action:{}".format(
            m.state_for_agent(action), action_index))
        m.visualize()
        print("-------------------")
    print('done, iterations:{} , score:{}'.format(counter, final_score))
    print(m.q)


# %%
if __name__ == '__main__':
    main()

# %%
