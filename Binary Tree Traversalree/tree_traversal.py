"""Три різні обхіди дерев"""
def check_None(node):
    if node is None:
        return []
    else:
        pass

# class Node:
#     """Клас ноди"""
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

#     def get_r_and_l(self):
#         """Повертаємо ліст синів, якщо один з них None, опускаємо його в лісті"""
#         return [el for el in [self.left, self.right] if el is not None]

def pre_order(node):
    """Префіксна нотація"""
    if node:
        result = []
        def get_r_and_l(nodee):
            """Повертаємо ліст синів, якщо один з них None, опускаємо його в лісті"""
            if nodee:
                resultt = []
                if nodee.left:
                    result.append(nodee.left.data)
                    get_r_and_l(nodee.left)
                if nodee.right:
                    result.append(nodee.right.data)
                    get_r_and_l(nodee.right)
                return resultt
            else:
                return []
        result.append(node.data)
        result.extend(get_r_and_l(node))
        return result
    else:
        return []

# In-order traversal
def in_order(node):
    result = []
    def get_r_and_l(nodee):
        """Повертаємо ліст синів, якщо один з них None, опускаємо його в лісті"""
        if nodee:
            if nodee.left:
                get_r_and_l(nodee.left)
            result.append(nodee.data)
            if nodee.right:
                get_r_and_l(nodee.right)
    get_r_and_l(node)
    return result

# Post-order traversal
def post_order(node):
    """Постфіксна нотація"""
    if not node:
        return []
    else:
        result = []
        def get_r_and_l(nodee):
            """Повертаємо ліст синів, якщо один з них None, опускаємо його в лісті"""
            if nodee:
                resultt = []
                if nodee.left:
                    get_r_and_l(nodee.left)
                    result.append(nodee.left.data)
                if nodee.right:
                    get_r_and_l(nodee.right)
                    result.append(nodee.right.data)
                return resultt
            else:
                return []
        result.extend(get_r_and_l(node))
        result.append(node.data)
        return result
