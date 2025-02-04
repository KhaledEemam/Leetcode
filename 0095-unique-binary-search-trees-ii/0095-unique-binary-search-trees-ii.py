# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def bfs(start,end) :
            if start == end :
                return [TreeNode(val=start)]
            
            if start > end :
                return [None]
            
            if (start,end) in memo :
                return memo[(start,end)]


            current_answer = []

            for i in range(start,end+1) :

                for left_node in bfs(start,i-1) :
                    for right_node in  bfs(i+1 , end) :
                        node = TreeNode(val=i , left=left_node , right = right_node)
                        current_answer.append(node)

            memo[(start,end)] = current_answer
            return current_answer



        return bfs(1,n)