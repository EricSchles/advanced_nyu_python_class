from binary_tree import BinarySearchTree
import random

def pretty_print(node, level):
    # step 1 (base case)
    if node.val is None:
        return
    # step 2
    if node.left is not None:
        to_print = "\t"*level + str(node.val)
        print(to_print)
        pretty_print(node.left, level+1)
    elif node.right is not None:
        to_print = "\t"*level + str(node.val)
        print(to_print)
        pretty_print(node.right, level+1)

tree = BinarySearchTree()

listing = []
for _ in range(10):
    elem = random.randint(0,10)
    listing.append(elem)
    tree.insert(elem)

print(listing)
pretty_print(tree.root, 0)

