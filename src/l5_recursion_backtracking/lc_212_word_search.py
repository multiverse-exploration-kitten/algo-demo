import collections
from typing import List


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False
        self.usage = 0


class Trie:
    def __init__(self):
        self.root = Node()
        self.num_of_words = 0

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            node.usage += 1

        node.is_word = True
        self.num_of_words += 1

    def remove(self, word):
        node = self.root

        for w in word:
            prev_node = node
            node = node.children[w]
            node.usage -= 1
            if node.usage == 0:
                del prev_node.children[w]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # O(m*n * 4 ^ (K - 1)) ->  m* n * 2 ^ K
        res = []

        trie = Trie()
        node = trie.root

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_node = node.children.get(board[i][j])
                if not curr_node:
                    continue

                self.dfs(i, j, board, curr_node, trie, board[i][j], res)

        return res

    def dfs(self, x, y, board, node, trie, path, res):

        if not node or trie.num_of_words == 0:
            return

        if node.is_word:
            res.append(path)
            node.is_word = False
            trie.num_of_words -= 1
            trie.remove(path)

        if not self.in_bound(x, y, board):
            return

        char = board[x][y]
        board[x][y] = "#"

        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in deltas:
            nx = x + dx
            ny = y + dy
            if not self.in_bound(nx, ny, board):
                continue

            c = board[nx][ny]
            nxt_node = node.children.get(c)
            if not nxt_node:
                continue

            self.dfs(nx, ny, board, nxt_node, trie, path + c, res)

        board[x][y] = char

    def in_bound(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
