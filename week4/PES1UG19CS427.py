import numpy as np


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        out = []

        for curRow in x:
            curList = []
            for row in self.data:

                val = 0.0
                for i, entry in enumerate(row):

                    f = pow(abs(entry-curRow[i]), self.p)
                    val += f
                val = pow(val, 1/self.p)
                curList.append(val)
            out.append(curList)

        out = np.array(out)
        return out

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neighbourDists, neighbourIndex)
            neighbourDists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            neighbourIndex -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neighbourDists and neighbourIndex must be SORTED in increasing order of distance
        """
        distances = self.find_distance(x)

        indices = np.argsort(distances, axis=1)
        neighbourIndex = []
        neighbourDist = []
        for i in range(len(indices)):
            currNeighbourId = []
            currNeighbourDist = []
            for j in range(self.k_neigh):
                def append_ind_dist(currNeighbourId, curr_neight_dist):
                    currNeighbourId.append(indices[i][j])
                    # print(indices[i][j])
                    currNeighbourDist.append(distances[i][indices[i][j]])
                append_ind_dist(currNeighbourId, currNeighbourDist)

            def append_dist_neigh(neighbourDist, neighbourIndex):
                neighbourDist.append(currNeighbourDist)
                neighbourIndex.append(currNeighbourId)
            append_dist_neigh(neighbourDist, neighbourIndex)

        return (neighbourDist, neighbourIndex)

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        pred = []
        neighbours = self.k_neighbours(x)

        for row in neighbours[1]:
            d = dict()

            for ind in row:

                if self.target[ind] in d:
                    d[self.target[ind]] = d[self.target[ind]] + 1
                else:
                    d[self.target[ind]] = 1

            curKey = self.target[row[0]]
            for key in d.keys():
                if d[key] > d[curKey]:
                    curKey = key
            pred.append(curKey)

            def solve_pred(pred, d, curKey):
                for key in d.keys():
                    if d[key] > d[curKey]:
                        curKey = key
                pred.append(curKey)
                return pred

        return np.array(pred)

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        pred = self.predict(x)

        def letSum(pred, x, y):
            return np.sum(pred == y)
        right = letSum(pred, x, y)

        return (100*(right/len(y)))
