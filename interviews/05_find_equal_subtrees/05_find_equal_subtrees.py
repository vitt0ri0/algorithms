# Найти два одинаковых поддерева.
# Дано бинарное дерево с выделенным корнем, в каждой вершине которого записано по одной букве A-Z.
# Две вершины считаются эквивалентными, если поддеревья этих вершин содержат одинаковое множество
# (т.е. без учета частот) букв.


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left: Node = left
        self.right: Node = right


def count_subset(tree_root):
    pass


def count_node_set(node):
    r1 = set()
    r2 = set()
    if node.left:
        r1 = count_node_set(node.left)
    if node.right:
        r2 = count_node_set(node.right)
    node.res = set(node.value).union(r1, r2)
    return node.res


if __name__ == '__main__':
    n22 = Node('d', None, None)
    n3 = Node('a', None, None)
    n2 = Node('b', n22, None)
    n1 = Node('c', n3, n2)

    res = count_node_set(n1)

    print(res)


