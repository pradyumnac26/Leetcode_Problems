class AllOne:

    class Node:
        def __init__(self, count: int):
            self.count = count
            self.keys = set()
            self.prev = None
            self.next = None

    def __init__(self):
        self.myds = {}  # Maps key to the node containing its count
        self.head = self.Node(float('-inf'))  # Dummy head node
        self.tail = self.Node(float('inf'))   # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        """Add new_node after prev_node in the doubly linked list."""
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.myds:
            node = self.myds[key]
            node.keys.remove(key)
            if node.next.count != node.count + 1:
                new_node = self.Node(node.count + 1)
                self._add_node_after(new_node, node)
            else:
                new_node = node.next
            new_node.keys.add(key)
            self.myds[key] = new_node
            if not node.keys:
                self._remove_node(node)
        else:
            if self.head.next.count != 1:
                new_node = self.Node(1)
                self._add_node_after(new_node, self.head)
            else:
                new_node = self.head.next
            new_node.keys.add(key)
            self.myds[key] = new_node

    def dec(self, key: str) -> None:
        if key in self.myds:
            node = self.myds[key]
            node.keys.remove(key)
            if node.count == 1:
                del self.myds[key]
            else:
                if node.prev.count != node.count - 1:
                    new_node = self.Node(node.count - 1)
                    self._add_node_after(new_node, node.prev)
                else:
                    new_node = node.prev
                new_node.keys.add(key)
                self.myds[key] = new_node
            if not node.keys:
                self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()