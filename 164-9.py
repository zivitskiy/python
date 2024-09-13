from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue: deque = deque()

    def fifoenqueue(self, item) -> None:
        self.queue.append(item)

    def fifodequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Черга порожня!"

    def lifoenqueue(self, item) -> None:
        self.queue.append(item)

    def lifodequeue(self):
        if self.queue:
            return self.queue.pop()
        return "Черга порожня!"

    def display(self) -> None:
        print(list(self.queue))

def main() -> None:
    queue: Queue = Queue()

    queue.fifoenqueue(1)
    queue.fifoenqueue(2)
    queue.fifoenqueue(3)

    print("Черга після додавання (FIFO):")
    queue.display()

    print("\nFIFO: Перший прийшов, перший пішов:")
    print(queue.fifodequeue())
    queue.display()

    print("\nLIFO: Перший прийшов, останній пішов:")
    print(queue.lifodequeue())
    queue.display()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
