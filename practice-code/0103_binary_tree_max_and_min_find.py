class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None
 
# function to insert a new node in BST
def insert(root, data):
    # if the tree is empty, return a new (single node)
    if not root: return Node(data)
 
    # otherwise, recur down the tree
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
        
    # return the (unchanged) node pointer
    return root
 
# function to find the node with maximum value 
def maxValue(root):
    current = root

    while(current.right):
        current = current.right
    return current.data


# function to find the node with minimum value 
def minValue(root):
    current = root

    while(current.left):
        current = current.left
    return current.data


# driver code
if __name__=='__main__':
    root = None
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)

    print("Maximum value in BST is {}".format(maxValue(root)))
    print("Minimum value in BST is {}".format(minValue(root)))
    

'''output:

Maximum value in BST is 6
Minimum value in BST is 1
'''