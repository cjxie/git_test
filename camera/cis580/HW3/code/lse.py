import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  # qT E p = 0
  # input: 
  #       X1: calibrated points in frame1  Nx3
  #       X2: calibrated points in frame2  Nx3
  # Returns:
  #        E: estimated essential matrix   3x3

  # build the matrix
  N = X1.shape[0]
  # A = np.zeros((N,9))
  # for i in range(N):
  #   A[i] = np.array([X1[i,0]*X2[i], X1[i,1]*X2[i],X1[i,0]*X2[i]]).reshape(9,)
  A = np.hstack((X2*X1[:,0].reshape(-1,1), X2*X1[:,1].reshape(-1,1), X2*X1[:,2].reshape(-1,1)))

  u, s, vt = np.linalg.svd(A)
  e = vt.T[:,-1]
  E = np.reshape(e,(3,3)).T

  # force the essential matrix to a valid one
  u,s,vt = np.linalg.svd(E)
  E = u@np.diag([1,1,0])@vt
  """ END YOUR CODE
  """
  return E

if __name__ == '__main__':
  X1 = np.ones((3,3))
  X2 = np.arange(9).reshape(3,3)
  print(least_squares_estimation(X1,X2))


