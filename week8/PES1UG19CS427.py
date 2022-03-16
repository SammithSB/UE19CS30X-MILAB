import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of all possible states
        emissions: list of all possible observations
        B: Emmision probabilities
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
            nu: Probability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        T = len(seq)
        nu = np.zeros((self.N, T))
        back_pointers = np.full((self.N, T), -1)
        for t, obs in enumerate(seq):
            for i in range(self.N):
                if t == 0:
                    nu[i, t] = self.pi[i] * self.B[i, self.emissions_dict[obs]]
                else:
                    prev_state_probs = [nu[j, t-1]*self.A[j, i]*self.B[i, self.emissions_dict[obs]]
                                        for j in range(self.N)]
                    back_pointers[i, t] = np.argmax(prev_state_probs)
                    nu[i, t] = np.max(prev_state_probs)
        # Last element of the sequence
        index = np.argmax(nu[:, -1])
        hidden_states_sequence = [self.states[index]]
        for t in range(T-1, 0, -1):
            col = back_pointers[:, t]
            back_index = col[index]
            state = self.states[back_index]
            hidden_states_sequence.insert(0, state)
            index = col[back_index]
        return hidden_states_sequence
