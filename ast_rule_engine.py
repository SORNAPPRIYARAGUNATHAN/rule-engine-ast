class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # left child node
        self.right = right     # right child node
        self.value = value     # value for operand (e.g., age > 30)

    def evaluate(self, data):
        if self.type == 'operator':
            if self.value == 'AND':
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == 'OR':
                return self.left.evaluate(data) or self.right.evaluate(data)
        elif self.type == 'operand':
            # Evaluate comparison like 'age > 30'
            return eval(self.value, {}, data)
