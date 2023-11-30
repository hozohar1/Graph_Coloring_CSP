


# hodaya zohar



# Graph Coloring
import math

# The graph is represented by a list with an item for every node.
# Item i represents node i+1 (the nodes are positive integers.)
# Each node is represented by a list of 3 items:
#   The color of the node (1...N). 0 for no color (yet)
#   A list of the node's neighbors (positive integers)
#   The domain -  a list of integers (1...N)

N = 0  # The colours are numbered 1...N


def create(fpath="graph.txt"):
    # fpath first line contains the num. of colours to be used.
    # The second line contains the list of neighbours of node 1.
    # The third line contains the list of neighbours of node 2.
    # ...
    global N
    p = []
    f = open(fpath, "r")
    N = int(f.readline())
    s = f.readline()
    while s != "":
        p += [[0, [int(i) for i in s.split()], list(range(1, N + 1))]]
        s = f.readline()
    f.close()
    present(p)
    return p


def domain(problem, v):
    # Returns the domain of v
    return problem[v - 1][2][:]


def domain_size(problem, v):
    # Returns the domain size of v
    return len(problem[v - 1][2])


def assign_val(problem, v, x):
    # Assigns x in var. v
    problem[v - 1][0] = x


def get_val(problem, v):
    # Returns the val. of v
    return problem[v - 1][0]


def erase_from_domain(problem, v, x):
    # Erases x from the domain of v
    problem[v - 1][2].remove(x)


def get_list_of_free_vars(problem):
    """
    Returns a list of variables that were not assigned a value in the problem.

    Args:
        problem (list): The problem representation where each item represents a variable.
                        Each item is a list containing:
                            - The color of the node (0 for unassigned).
                            - A list of the node's neighbors.
                            - The domain, a list of possible values.

    Returns:
        list: A list of variable numbers that were not assigned a value.

    """
    return [(v + 1) for v, item in enumerate(problem) if item[0] == 0]



def is_solved(problem):
    # Returns True iff the problem is solved
    for i in problem:
        if i[0] == 0:
            return False
    return True


def is_consistent(problem, v1, v2, x1, x2):
    """
    Checks the consistency of assigning values to two variables in the problem.

    Args:
        problem (list): The problem representation where each item represents a variable.
                        Each item is a list containing:
                            - The color of the node.
                            - A list of the node's neighbors.
                            - The domain, a list of possible values.
        v1 (int): The number of Variable 1.
        v2 (int): The number of Variable 2.
        x1: The value assigned to Variable 1.
        x2: The value assigned to Variable 2.

    Returns:
        bool: True if the assignment is consistent, False otherwise.

    """
    l1 = problem[v1 - 1][1]  # Neighbors of Variable 1
    l2 = problem[v2 - 1][1]  # Neighbors of Variable 2

    # Check if any neighbor of Variable 1 has the same assigned value
    for i in l1:
        if problem[i - 1][0] == x1:
            return False

    # Check if any neighbor of Variable 2 has the same assigned value
    for i in l2:
        if problem[i - 1][0] == x2:
            return False

    return True


#The function first initializes an empty list l to store the influenced variables.
# It then iterates over the neighbors of v (retrieved from problem[v - 1][1]). For each neighbor,
# it checks if the assigned value (problem[i - 1][0]) is 0,
# indicating that it has not been assigned a value yet. If so, it adds the variable to the list l.
#Finally, the function returns the list l containing the variables influenced by v that have not been assigned a value.
def list_of_influenced_vars(problem, v):
    """
    Args:
        problem (list): The problem representation where each item represents a variable.
                        Each item is a list containing:
                            - The color of the node.
                            - A list of the node's neighbors.
                            - The domain, a list of possible values.
        v (int): Variable number.

    Returns:
        list: List of variables influenced by v that have not been assigned a value.

    """
    l = []
    for i in problem[v - 1][1]:
        if problem[i - 1][0] == 0:
            l.append(i)
    return l




def present(problem):
    for p in problem:
        print(p)
    print("************")
