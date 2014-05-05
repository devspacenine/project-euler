class Node(object):
    data = None
    children = []

    def __init__(self, data):
        self.data = data

    def addChild(self, node):
        self.children.append(node)
