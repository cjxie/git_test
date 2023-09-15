import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  """ YOUR CODE HERE
  """

  """
  INPUTS: uncalibrated_1 : array of 3 * N
          uncalibrated_2 : array of 3 * N
          R, T : 1 in 2
  OUTPUTS: P2proj:
           P1proj: reprojected P1  array of
  """
  # P2proj= (K@(R.T@(P2-T).T)).T    # p2 proj to  frame 1
  # P1proj= (K@(R@ P1.T + T.reshape(3,-1))).T
  
  P2proj = ((R.T @ P2.T).T - R.T@T) @K.T  # P2 Project to P1
  P1proj = ((R @ P1.T).T + T) @K.T    # P1 Project to P2
  """ END YOUR CODE
  """

  if (plot):
    plt.figure(figsize=(6.4*3, 4.8*3))
    ax = plt.subplot(1, 2, 1)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image1[:, :, ::-1])
    plt.plot(P2proj[:, 0] / P2proj[:, 2],
           P2proj[:, 1] / P2proj[:, 2], 'bs')
    plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

    ax = plt.subplot(1, 2, 2)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image2[:, :, ::-1])
    plt.plot(P1proj[:, 0] / P1proj[:, 2],
           P1proj[:, 1] / P1proj[:, 2], 'bs')
    plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')
    
  else:
    return P1proj, P2proj