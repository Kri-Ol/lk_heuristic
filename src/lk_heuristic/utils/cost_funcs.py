import lk_heuristic.utils.globals

def euc_2d(n1, n2) -> float:
    """
    The euclidean distance for 2D cartesian nodes

    :param n1: first node
    :type n1: Node
    :param n2: second node
    :type n2: Node
    :return: the euclidean distance between first node and second node in 2D space
    :rtype: float
    """
    return ((n1.x - n2.x)**2 + (n1.y - n2.y)**2)**0.5


def euc_3d(n1, n2) -> float:
    """
    The euclidean distance for 3D cartesian nodes

    :param n1: first node
    :type n1: Node3D
    :param n2: second node
    :type n2: Node3D
    :return: the euclidean distance between first node and second node in 3D space
    :rtype: float
    """
    return ((n1.x - n2.x)**2 + (n1.y - n2.y)**2 + (n1.z - n2.z)**2)**0.5

def full_matrix(n1, n2) -> float:
    """
    The external distance via explicit full matrix

    :param n1: first node, used as matrix index
    :type n1: Node2D
    :param n2: second node, used as matrix index
    :type n2: Node2D
    :return: the distance between first node and second node in 3D space, from full matrix
    :rtype: float
    """
    return lk_heuristic.utils.globals.distmatrix[n1.x][n2.x]

# a dictionary mapping tsp lib edge weight type with respective cost function
cost_funcs = {"EUC_2D": euc_2d,
              "EUC_3D": euc_3d,
              "EXPLICIT": full_matrix}
