'''
Implementation of a Binary Tree and the three traversal algorithms:
    1 - Preorder
    2 - Inorder 
    3 - Postorder
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
    
class Binary_tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traversal):
        #Root -> Left -> Right
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        
        return traversal
    
    def inorder(self, start, traversal):
        #Left -> Root -> Right
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right, traversal)
        
        return traversal

    def postorder(self, start, traversal):
        #Right -> Left -> Root
        if start:
            traversal = self.postorder(start.right, traversal)
            traversal = self.postorder(start.left, traversal)
            traversal += (str(start.value) + '-')
        
        return traversal
    
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(self.root, '')
        
        elif traversal_type == 'inorder':
            return self.inorder(self.root, '')
        
        elif traversal_type == 'postorder':
            return self.postorder(self.root, '')

        else:
            return False

tr1 = Binary_tree(3)
tr1.root.left = Node(4)
tr1.root.right = Node(5)
tr1.root.left.left = Node(6)
tr1.root.left.right = Node(10)
tr1.root.left.left.left = Node(11)
tr1.root.left.left.left.left = Node(13)
tr1.root.left.right.right = Node(20)





# print(tr1.root.value)
# print(tr1.root.left.value)
# print(tr1.root.right.value)

pr = tr1.print_tree('preorder')
pr2 = tr1.print_tree('inorder')
pr3 = tr1.print_tree('postorder')


print(pr)
print(pr2)
print(pr3)