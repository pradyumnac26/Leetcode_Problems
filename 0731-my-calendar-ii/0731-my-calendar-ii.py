class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.nonoverlapping = [] 
        

    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlapping : 
            if end > s and e > start:
                return False
        
        for s,e in self.nonoverlapping :
            if end > s and e > start : 
                self.overlapping.append((max(s,start), min(e,end)))
        self.nonoverlapping.append((start,end))
        return True
                    

                
                
                
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)