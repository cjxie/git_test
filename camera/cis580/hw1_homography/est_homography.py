import numpy as np


def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####
    A = np.zeros((8,8))
    B = np.zeros((8,1))
    # for i in range(4):
    #     x, y = X[i,0] , X[i,1]
    #     x_prime, y_prime = X_prime[i,0] , X_prime[i,1]
    #     B[2*i] = x_prime
    #     B[2*i+1] = y_prime
    #     A[2*i,:] = np.array([x, y, 1, 0, 0, 0, -x*x_prime, -y*x_prime])
    #     A[2*i+1,:] = np.array([0, 0, 0, x, y, 1, -x*y_prime, -y*y_prime])

    # h = np.linalg.lstsq(A,B, rcond= None)[0]

    
    # # Modify the corresponding point pairs
    X = np.vstack((X.T, np.ones((1,4))))
    X_prime = np.vstack((X_prime.T, np.ones((1,4))))

    # # Set up the linear equations
    A = np.zeros((8,9))
    # B = np.zeros((8,1))

    for i in range(np.shape(X)[1]):
        A[2*i,:3] = -X[:,i]
        A[2*i+1,3:6] = -X[:,i]
        A[2*i,6] = X[0,i] * X_prime[0,i]
        A[2*i,7] = X[1,i] * X_prime[0,i]
        A[2*i,8] = X_prime[0,i]
        A[2*i+1,6] = X[0,i] * X_prime[1,i]
        A[2*i+1,7] = X[1,i] * X_prime[1,i]
        A[2*i+1,8] = X_prime[1,i]

        # B[2*i:2*(i+1)] = X_prime[:2,i].reshape(2,1)

    # print("A:", A)
    # print("b:", B)

    # h = np.linalg.lstsq(-A,B, rcond= None)[0]
    # h = np.vstack((h,np.array([1]).reshape(1,)))

    # H = h.reshape((3,3))

    u,s,vt = np.linalg.svd(A)
    H = vt.T[:,-1].reshape((3,3))
 
    ##### STUDENT CODE END #####

    return H
