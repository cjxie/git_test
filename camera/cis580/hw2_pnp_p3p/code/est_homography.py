import numpy as np

def est_homography(X, Y):
    """
    Calculates the homography H of two planes such that Y ~ H*X
    If you want to use this function for hw5, you need to figure out
    what X and Y should be.
    Input:
        X: 4x2 matrix of (x,y) coordinates
        Y: 4x2 matrix of (x,y) coordinates
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. Y ~ H*X

    """

    ##### STUDENT CODE START #####
    A = np.zeros((8,8))
    B = np.zeros((8,1))
    # for i in range(4):
    #     x, y = X[i,0] , X[i,1]
    #     Y, y_prime = Y[i,0] , Y[i,1]
    #     B[2*i] = Y
    #     B[2*i+1] = y_prime
    #     A[2*i,:] = np.array([x, y, 1, 0, 0, 0, -x*Y, -y*Y])
    #     A[2*i+1,:] = np.array([0, 0, 0, x, y, 1, -x*y_prime, -y*y_prime])

    # h = np.linalg.lstsq(A,B, rcond= None)[0]

    
    # # Modify the corresponding point pairs
    X = np.vstack((X.T, np.ones((1,4))))
    Y = np.vstack((Y.T, np.ones((1,4))))

    # # Set up the linear equations
    A = np.zeros((8,9))
    # B = np.zeros((8,1))

    for i in range(np.shape(X)[1]):
        A[2*i,:3] = -X[:,i]
        A[2*i+1,3:6] = -X[:,i]
        A[2*i,6] = X[0,i] * Y[0,i]
        A[2*i,7] = X[1,i] * Y[0,i]
        A[2*i,8] = Y[0,i]
        A[2*i+1,6] = X[0,i] * Y[1,i]
        A[2*i+1,7] = X[1,i] * Y[1,i]
        A[2*i+1,8] = Y[1,i]

        # B[2*i:2*(i+1)] = Y[:2,i].reshape(2,1)

    # print("A:", A)
    # print("b:", B)

    # h = np.linalg.lstsq(-A,B, rcond= None)[0]
    # h = np.vstack((h,np.array([1]).reshape(1,)))

    # H = h.reshape((3,3))

    u,s,vt = np.linalg.svd(A)
    H = vt.T[:,-1].reshape((3,3))
 
    ##### STUDENT CODE END #####

    ##### STUDENT CODE END #####

    return H
