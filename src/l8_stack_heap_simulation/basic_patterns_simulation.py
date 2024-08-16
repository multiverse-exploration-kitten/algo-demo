import heapq
from collections import Counter, deque


# 1. Grid/Matrix Simulation: Game of Life
def count_live_neighbors(r, c, rows, cols):
    live_neighbors = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if (i == r and j == c) or i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            if abs(board[i][j]) == 1:
                live_neighbors += 1
    return live_neighbors


def game_of_life(board):
    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(r, c, rows, cols)
            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[r][c] = -1  # -1 indicates the cell was live but now dead
            if board[r][c] == 0 and live_neighbors == 3:
                board[r][c] = 2  # 2 indicates the cell was dead but now live

    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0


# 2. String Simulation: Decode String
def decode_string(s):
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            prev_string, num = stack.pop()
            current_string = prev_string + num * current_string
        else:
            current_string += char

    return current_string


# 3. Event-Based Simulation: Task Scheduler
def least_interval(tasks, n):
    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = deque()  # to keep track of the cooling period

    while max_heap or queue:
        time += 1

        if max_heap:
            count = heapq.heappop(max_heap) + 1  # decrement the task count
            if count:
                queue.append(
                    (count, time + n)
                )  # add task back to queue with cooldown period

        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])

    return time


# 4. Sequential Simulation: Robot Return to Origin
# delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# delta_with_dir = [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]
def judge_circle(moves):
    x, y = 0, 0
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "L":
            x -= 1
        elif move == "R":
            x += 1
    return x == 0 and y == 0


# 5. Multi-Agent Simulation: Simulate Multi-Robot Grid Movement
def robot_collision(grid, robots):
    for robot in robots:
        x, y = robot["start"]
        for move in robot["moves"]:
            if move == "U":
                x -= 1
            elif move == "D":
                x += 1
            elif move == "L":
                y -= 1
            elif move == "R":
                y += 1
            if grid[x][y] == 1:  # Check for collision or obstacle
                return False
        robot["end"] = (x, y)
    return True


# 6. Simulating Data Structures: Design a Circular Queue
class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.capacity = k

    def en_queue(self, value):
        if self.is_full():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True

    def de_queue(self):
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def front(self):
        if self.is_empty():
            return -1
        return self.queue[self.head]

    def rear(self):
        if self.is_empty():
            return -1
        return self.queue[self.tail - 1]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity


# Example usage of the functions/classes
if __name__ == "__main__":
    # Example 1: Game of Life
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    game_of_life(board)
    print("Game of Life:", board)

    # Example 2: Decode String
    s = "3[a2[c]]"
    print("Decoded String:", decode_string(s))

    # Example 3: Task Scheduler
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print("Least Interval:", least_interval(tasks, n))

    # Example 4: Robot Return to Origin
    moves = "UD"
    print("Robot Return to Origin:", judge_circle(moves))

    # Example 5: Simulate Multi-Robot Grid Movement
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    robots = [{"start": (0, 0), "moves": "DRR"}, {"start": (2, 0), "moves": "URR"}]
    print("Robot Collision:", robot_collision(grid, robots))

    # Example 6: Circular Queue
    k = 3
    circular_queue = MyCircularQueue(k)
    print("Enqueue 1:", circular_queue.en_queue(1))
    print("Enqueue 2:", circular_queue.en_queue(2))
    print("Enqueue 3:", circular_queue.en_queue(3))
    print("Enqueue 4:", circular_queue.en_queue(4))
    print("Rear item:", circular_queue.rear())
    print("Is full:", circular_queue.is_full())
    print("Dequeue:", circular_queue.de_queue())
    print("Enqueue 4:", circular_queue.en_queue(4))
    print("Rear item:", circular_queue.rear())
