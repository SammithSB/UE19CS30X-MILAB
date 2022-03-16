import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        # TODO
        init_seq = [self.emissions_dict[s] for s in seq]
        T = len(init_seq)
        delta = np.zeros((self.N, T))
        psi = np.zeros((self.N, T))
        delta[:, 0] = self.pi * self.B[:, init_seq[0]]
        for t in range(1, T):
            for j in range(self.N):
                delta[j, t] = np.max(
                    delta[:, t-1] * self.A[:, j]) * self.B[j, init_seq[t]]
                psi[j, t] = np.argmax(delta[:, t-1] * self.A[:, j])
        nu = np.max(delta[:, T-1])
        hidden_states_sequence = []
        for t in range(T):
            hidden_states_sequence.append(
                self.states[np.argmax(delta[:, T-1-t])])
        return hidden_states_sequence