from est_homography import est_homography
import numpy as np

def PnP(Pc, Pw, K=np.eye(3)):
    """
    Solve Perspective-N-Point problem with collineation assumption, given correspondence and intrinsic

    Input:
        Pc: 4x2 numpy array of pixel coordinate of the April tag corners in (x,y) format
        Pw: 4x3 numpy array of world coordinate of the April tag corners in (x,y,z) format
    Returns:
        R: 3x3 numpy array describing camera orientation in the world (R_wc)
        t: (3, ) numpy array describing camera translation in the world (t_wc)

    """

    ##### STUDENT CODE START #####

    # Homography Approach
    # Following slides: Pose from Projective Transformation
    
    # find the approximated H
    H = est_homography(Pw[:,:2], Pc)
    H_prime = np.linalg.inv(K) @ H
    
    # Procrustes
    h3 = H_prime[:,2].copy()
    H_prime[:,2] = np.cross(H_prime[:,0], H_prime[:,1]).reshape(3,1)
    u, s, vt = np.linalg.svd(H_prime)
    R = u @ np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, np.linalg.det(u@vt)]]) @ vt
    
    
    t = h3 / np.linalg.norm(H_prime[:,0])

    R = R.T
    t = -R.T @ t

    ##### STUDENT CODE END #####

    return R, t
