# 1. Implement Queue using Stacks

## Idea

A Queue follows **FIFO** (First In First Out).
Stacks follow **LIFO** (Last In First Out).

Use **two stacks**:
* `inputStack` → for enqueue
* `outputStack` → for dequeue

Whenever dequeue/front is requested:

* If `outputStack` is empty:
  * Move all elements from `inputStack` to `outputStack`
* Then perform operation on `outputStack`

---

## Pseudocode
```
Push(x)
    Push x into inputStack
Pop()
    If outputStack is empty
        Move all elements from inputStack to outputStack
    Pop outputStack
Peek()
    If outputStack is empty
        Move all elements from inputStack to outputStack
    Return top(outputStack)
Empty()
    Return inputStack empty AND outputStack empty
```

---

# 2. Design Circular Queue
## Idea
Use an array of fixed size `k`.

Maintain:
* front
* rear
* size

When rear reaches end:

* Wrap around using modulo.

```text
rear = (rear + 1) % capacity
front = (front + 1) % capacity
```

---



## Pseudocode

```text
CLASS MyCircularQueue
    queue[k]
    front = 0
    rear = -1
    size = 0
    FUNCTION enQueue(value)
        IF size == k
            RETURN False
        rear = (rear + 1) mod k
        queue[rear] = value
        size++
        RETURN True
    FUNCTION deQueue()
        IF size == 0
            RETURN False
        front = (front + 1) mod k
        size--
        RETURN True
    FUNCTION Front()
        IF size == 0
            RETURN -1
        RETURN queue[front]
    FUNCTION Rear()
        IF size == 0
            RETURN -1
        RETURN queue[rear]
```
