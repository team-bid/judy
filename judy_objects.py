class Node(object):
    left = None
    right = None
    item = None
    probability = 0.0
    bitmap = ''
    is_item = False

    def __init__(self, i, p, bitmap='', is_item=False):
        self.item = i
        self.probability = float(p)
        self.bitmap = str(bitmap)
        self.is_item = is_item

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __repr__(self):
        if self.is_item:
            return '\nI: %s p=%s map=%s' % (self.item, self.probability, self.bitmap)
        else:
            return '\nQ: %s p=%s map=%s l=%s r=%s' % (self.item, self.probability, self.bitmap, self.left, self.right)

    def __cmp__(self, a):
        return cmp(self.probability, a.probability)

    def __lt__(self, a):
        return self.probability < a.probability
