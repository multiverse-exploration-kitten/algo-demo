from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 1:
            return True

        num_of_rooms = len(rooms)

        visited = [False for _ in range(num_of_rooms)]

        self.visit(rooms, visited, 0)
        return all(visited)

    def visit(self, rooms, visited, curr):

        if visited[curr]:
            return

        visited[curr] = True
        for key in rooms[curr]:
            self.visit(rooms, visited, key)
