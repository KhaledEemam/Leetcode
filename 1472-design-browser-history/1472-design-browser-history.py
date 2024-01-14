class ListNode :
    def __init__(self,val,next_node=None, prev_node = None) :
        self.val = val
        self.prev = prev_node
        self.next = next_node

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        new_page = ListNode(url)
        self.cur.next = new_page
        new_page.prev = self.cur
        self.cur = new_page

    def back(self, steps: int) -> str:
        
        
        while self.cur.prev and steps > 0   :
            steps -= 1
            self.cur = self.cur.prev
            
        
        return self.cur.val
        

    def forward(self, steps: int) -> str:

        while self.cur.next and steps > 0   :
            steps -= 1
            self.cur = self.cur.next
            
                
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)