class Tree:
    def __init__(self):
        self.__root = None

    def search(self, key):
        if self.__root is None:
            return None
        node = self.__search_rek(key, self.__root)
        return node.value

    def __search_rek(self, key, node):
        if node is None:
            return None
        
        if key == node.key:
            return node
        elif key > node.key:
            return self.__search_rek(key, node.right)
        else:
            return self.__search_rek(key, node.left)

    def insert(self, key, value, node=None, first=True):
        if first:
            if self.__root is not None:
                node = self.__root
                return self.insert(key, value, node, False)
            else:
                self.__root = Node(key, value)
                return self.__root

        if node is None:
            return Node(key, value)
        
        if key < node.key:
            node.left = self.insert(key, value, node.left, False)
            return node
        elif key > node.key:
            node.right = self.insert(key, value, node.right, False)
            return node
        else:
            node.value = value
            return node

    def delete(self, key):
        if self.__root is None:
            return None
        
        (parent, right) = None, None
        root = Node(0, "phantom", None, self.__root) if self.__root.key == key else self.__root
        (parent, right) = self.__delete_rek(key, root)

        if parent is None:
            return None
        
        deleting_node = parent.right if right else parent.left
        left_child = deleting_node.left is not None
        right_child = deleting_node.right is not None

        if left_child and right_child:
            least_key, least_value, least_right, prev = self.__minimal_from_branch(deleting_node.right, deleting_node)
            
            if prev is not deleting_node:
                prev.left = None
            
            if right:
                parent.right.key = least_key
                parent.right.value = least_value
            else:
                parent.left.key = least_key
                parent.left.value = least_value

            if prev.right.key == least_key:
                prev.right = least_right
            else:
                prev.left = least_right

        elif left_child:
            if right:
                parent.right = deleting_node.left
            else:
                parent.left = deleting_node.left

        elif right_child:
            if right:
                parent.right = deleting_node.right
            else:
                parent.left = deleting_node.right

        else:
            if right:
                parent.right = None
            else:
                parent.left = None
    
    def __delete_rek(self, key, node):
        if node is None:
            return None, None
        
        if node.left is not None and node.left.key == key:
            return node, False
        elif node.right is not None and node.right.key == key:
            return node, True
        
        if key > node.key:
            return self.__delete_rek(key, node.right)
        else:
            return self.__delete_rek(key, node.left)    

    def __minimal_from_branch(self, node, prev):
        while node.left is not None:
            prev = node
            node = node.left
        return node.key, node.value, node.right, prev

    def __str__(self):
        if self.__root is None:
            return "puste drzewo"
        else:
            return self.__print_rek(self.__root)
        
    def __print_rek(self, node):
        if node is None:
            return ""
        node_str = ""
        node_str += self.__print_rek(node.left)
        node_str += str(node.key) + " " + str(node.value) + ","
        node_str += self.__print_rek(node.right)
        return node_str

    def height(self):
        return self.__height_rek(self.__root)

    def __height_rek(self, node):
        if node is None:
            return 0
        left = self.__height_rek(node.left)
        right = self.__height_rek(node.right)
        return left+1 if left >= right else right+1

    def print_tree(self):
        print("==============")
        self.__print_tree(self.__root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

class Node:
    def __init__(self, key, value, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.key = key
        self.value = value

def main():
    tree = Tree()

    chars = [*"ABCDEFGHIJKL"]
    nums = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]

    for num, char in zip(nums, chars):
        tree.insert(num, char)

    tree.print_tree()
    print(tree)
    print(tree.search(24))
    tree.insert(20, "AA")
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    print(tree)
    tree.print_tree()

if __name__ == "__main__":
    main()
