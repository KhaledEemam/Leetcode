# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        stack = []
        
        
        cur = root
        while stack or cur :
            while cur :
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.res.append(cur.val)
            cur = cur.right
            
        self.nxt = -1
            

    def next(self) -> int:
        self.nxt += 1
        if self.nxt < len(self.res) :
            return self.res[self.nxt]

    def hasNext(self) -> bool:
        if self.nxt + 1 < len(self.res) :
            return True
        else :
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()