from lse import least_squares_estimation
import numpy as np

def calculate_distance2epipolar(x1,x2,E):
    # input parameters:
    # x1: N x 3, x2: N x 3
    #
    e3 = np.array([[0,-1,0],
                   [1,0,0],
                   [0,0,0]])
    d = np.square(np.diagonal(x2@E@x1.T).reshape(-1,))/ np.square(np.linalg.norm(e3@E@x1.T,axis=0).reshape(-1,))
    return d

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        E = least_squares_estimation(X1[sample_indices], X2[sample_indices])

        # compute the distance of a matching point to the epipolar
        dist = calculate_distance2epipolar(X1[test_indices],X2[test_indices],E) + calculate_distance2epipolar(X2[test_indices],X1[test_indices],E.T)
        inliers = np.concatenate((sample_indices,test_indices[dist<eps]))

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers


    return best_E, best_inliers