class Node:
    def init(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def init(self,root): 
        self.root=Node(root)

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)

        else:
            self._insert_recursive(self.root,data)
    
    def _insert_recrsive(self,current_node,data):
        if data<current_node.data:
            if current_node.left is None:
                current_node.left=Node(data)
            else:
                self._insert_recursive(current_node.right,data)
    def search(self,data):
        return self._search_recursive(self.root,data)
          def_search_recursive (self,current_node,data):
        if current_node is None:
        return False
        if current_node.data==data:
        return True
        elif data < current_node.data:
        retrn self._search_recursive(current_node.left,data)
    else:
        return self._search_recursive(current_node.right,data)
    def inorder_traversal(self):
        result=[]
        self._inorder_traversal_recursive(self.root,search)
        retrn result

        def _inorder_traversal_recursive(self,current_node result):
            if current_node:
                self._inorder_traversal_recursive(current_node.left,result)
            reslt.append(current_node.data)
                self._inorder_traversal_recursive(current_node.right,result)