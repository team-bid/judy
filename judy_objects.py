class Node:
    node_count = 0
    bitmap = ''
    is_item = False

    def __init__(self, is_item, bitmap, parent, left_child, right_child):
        self.parent = parent
        self.bitmap = bitmap
        self.is_item = is_item
        self.left_child = left_child
        self.right_child = right_child
        TreeNode.node_count += 1

    def get_number_of_nodes(self):
        return TreeNode.node_count
