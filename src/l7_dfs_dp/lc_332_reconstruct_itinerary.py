import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        destinations = collections.defaultdict(list)

        for origin, dest in tickets:
            destinations[origin].append(dest)

        for k, v in destinations.items():
            v.sort(reverse=True)

        res = []
        self.dfs(destinations, res, "JFK")

        return res[::-1]

    def dfs(self, destinations, res, origin):
        dest_list = destinations[origin]

        while dest_list:
            next_dest = dest_list.pop()
            self.dfs(destinations, res, next_dest)

        res.append(origin)

        return
