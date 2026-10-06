class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

        # HEAD = most recently used
        # TAIL = least recently used
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.dict:
            return -1

        x = self.dict[key]

        # Remove x from its current position
        x.prev.next = x.next
        x.next.prev = x.prev

        # Put x at HEAD
        x.prev = self.head
        x.next = self.head.next

        self.head.next.prev = x
        self.head.next = x

        return x.value

    def put(self, key: int, value: int) -> None:

        # If key already exists
        if key in self.dict:
            x = self.dict[key]

            # Update value
            x.value = value

            # Remove x from current position
            x.prev.next = x.next
            x.next.prev = x.prev

        else:
            # Create new node
            x = Node(key, value)
            self.dict[key] = x

            # If cache is full
            if len(self.dict) > self.capacity:

                # Least recently used node
                old = self.tail.prev

                # Remove it from linked list
                old.prev.next = self.tail
                self.tail.prev = old.prev

                # Remove it from dictionary
                del self.dict[old.key]

        # Put x at HEAD = most recently used
        x.prev = self.head
        x.next = self.head.next

        self.head.next.prev = x
        self.head.next = x