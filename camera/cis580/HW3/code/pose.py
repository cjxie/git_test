import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  u,s,vt = np.linalg.svd(E)
  R = np.array([[0,1,0],
                [-1,0,0],
                [0,0,1]])
  R_ = np.array([[0,-1,0],
                [1,0,0],
                [0,0,1]])
  transform_candidates+=[{"T":u[:,-1], "R": u@R.T@vt},
                               {"T":u[:,-1], "R": u@R_.T@vt},
                               {"T":-u[:,-1], "R": u@R.T@vt},
                               {"T":-u[:,-1], "R": u@R_.T@vt}]

  """ END YOUR CODE
  """
  return transform_candidates