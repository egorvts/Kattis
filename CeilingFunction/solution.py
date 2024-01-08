n, k = map(int, input().split())


class BST:
    def __init__(self, num=None):
        self.num = num
        self.left = None
        self.right = None

    def insert(self, num):
        if not self.num:
            self.num = num
        elif num < self.num:
            if self.left:
                self.left.insert(num)
            else:
                self.left = BST(num)
        else:
            if self.right:
                self.right.insert(num)
            else:
                self.right = BST(num)

    def depth(self):
        if not ((not (self.left)) and (not (self.right)) and self.num):
            if self.left and self.right:
                return 1 + max(self.left.depth(), self.right.depth())
            if self.left:
                return 1 + self.left.depth()
            if self.right:
                return 1 + self.right.depth()
        return 0


def are_equal_shape_BSTs(tree1, tree2):
    if tree1 == tree2 == None:
        return True
    elif type(tree1) != type(tree2):
        return False
    elif tree1 != None and tree2 != None:
        tree1_depth = tree1.depth()
        tree2_depth = tree2.depth()
        if tree1_depth != tree2_depth:
            return False
        return are_equal_shape_BSTs(tree1.left, tree2.left) and are_equal_shape_BSTs(tree1.right, tree2.right)


prototypes = []
for i in range(n):
    inp = list(map(int, input().split()))
    tree = BST()
    for i in range(len(inp)):
        tree.insert(inp[i])
    prototypes.append(tree)

res = 0
for i in range(len(prototypes)):
    for j in range(i + 1, len(prototypes)):
        if are_equal_shape_BSTs(prototypes[i], prototypes[j]):
            res += 1

print(len(prototypes) - res)
