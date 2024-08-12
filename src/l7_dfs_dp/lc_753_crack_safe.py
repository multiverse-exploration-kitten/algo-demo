from itertools import product


class Solution:
    def crack_safe(self, n: int, k: int) -> str:
        # Generate all possible n-length combinations of digits from 0 to k-1
        # Create a range of numbers as strings
        number_strings = map(str, range(k))

        # Generate all possible products with repetition
        all_combinations = product(number_strings, repeat=n)

        # Join each tuple of characters into a single string
        joined_combinations = map("".join, all_combinations)

        # Convert the result to a set
        perms = set(joined_combinations)

        # This will store the result in reverse order as we perform DFS
        res = []

        # Start with the initial combination of all zeros
        start = "0" * n

        # Remove the start combination from the set of permutations since we're starting from it
        perms.remove(start)

        # Start the DFS traversal from the initial combination
        self.dfs(start, k, perms, res)

        # Join the result list and add the starting combination to complete the Eulerian circuit
        return "".join(res) + start

    def dfs(self, n: str, k: int, perms: set, res: list):
        """
        This method performs Depth-First Search (DFS) to explore all possible combinations,
        and ensures that each combination is visited exactly once to form an Eulerian circuit.

        :param n: The current combination being explored
        :param k: Number of possible digits (0 to k-1)
        :param perms: Set of all unvisited combinations
        :param res: List to store the result in reverse order
        """

        # If all permutations have been visited, stop the DFS
        if not perms:
            return

        # Explore all possible digits (0 to k-1)
        for d in map(str, range(k)):
            # Create the next combination by appending the digit `d` and removing the first character
            next_ = (n + d)[1:]

            # If the next combination has not been visited yet, continue the DFS from this combination
            if next_ in perms:
                # Mark this combination as visited by removing it from the set
                perms.remove(next_)

                # Recursively perform DFS on the next combination
                self.dfs(next_, k, perms, res)

                # After all edges from this node are visited, add the digit to the result
                res.append(d)
