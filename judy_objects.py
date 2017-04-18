class Node:
    node_count = 0
    bitmap = ''
    is_item = False

    def __init__(self, is_item, bitmap, parent=None, left_child=None, right_child=None):
        self.parent = parent
        self.bitmap = bitmap
        self.is_item = is_item
        self.left_child = left_child
        self.right_child = right_child
        Node.node_count += 1

    def get_number_of_nodes(self):
        return Node.node_count

    def __repr__(self):
        if self.is_item:
            return '[I: %s]' % self.bitmap
        return '[Q: %s]' % self.bitmap

class Item:
    probability = 0.0
    name = ''
    bitmap = ''

    def __init__(self, name, probability, bitmap):
        self.name = name
        self.probability = float(probability)
        self.bitmap = bitmap
        return

    def __repr__(self):
        return '<%s, %.2f: %s>' % (self.name, self.probability, self.bitmap)
