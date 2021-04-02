# wczytanie potrzebnych bibliotek:
import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import math
import matplotlib.pyplot as plt
# ...

# definicje funkcji:

def zadanie_3():
    Tps = np.eye(4)
    Tbs = np.eye(4)
    Rps = np.array([[-1, 0, 0],
                    [0, 1, 0],
                    [0, 0, -1]])
    Rbs = np.array([[0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1]])
    tps = np.array([3, -6, 4])
    tbs = np.array([2, 5, 0])
    Tbs[0:3, 0:3] = Rbs
    Tbs[0:3, 3] = tbs.T
    Tbs = SE3(Tbs)
    Tps[0:3, 0:3] = Rps.T
    Tps[0:3, 3] = -(Rps.T)@tps
    Tps = SE3(Tps)
    dp = np.eye(4)
    db = np.eye(4)
    ds = np.eye(4)
    dp1 = np.array([1, -2, 2])
    dp[0:3, 3] = dp1.T
    dp = SE3(dp)
    ds = Tps@dp
    db = Tbs@ds
    db = SE3(db)
    print("Zadanie 3.1: ", db.t)
    #zadanie 3.2
    trplot(transl(0, 0, 0), frame='B', rviz=True, width=1)
    trplot(Tbs.A, color='red', frame='S')
    p = Tbs@Tps
    p = SE3(p)
    trplot(p.A, color='black', frame='P')
    plt.quiver(0, 0, 0, -2, 7, 2)
    plt.show()

# ...

# wykonywanie wybranej funkcji
if __name__ == '__main__':
    zadanie_3()

