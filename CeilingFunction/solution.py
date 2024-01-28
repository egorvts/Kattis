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


def BST_to_str(tree, lvl):
    if not tree:
        return ""
    else:
        return BST_to_str(tree.left, lvl+1) + str(lvl) + BST_to_str(tree.right, lvl+1)


prototypes = {}
for i in range(n):
    inp = list(map(int, input().split()))
    tree = BST()
    for i in range(k):
        tree.insert(inp[i])
    s = BST_to_str(tree, 0)
    if s in prototypes:
        prototypes[s] += 1
    else:
        prototypes[s] = 1

print(len(prototypes))
