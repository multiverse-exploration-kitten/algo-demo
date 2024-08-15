from typing import List


class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:

        # this is an 16 - 8
        res, cur, num_of_letters = [], [], 0
        for w in words:
            # if current length is greater than max width
            if num_of_letters + len(w) + len(cur) > max_width:

                # adding spaces to each of the words
                # rotate by using %
                for i in range(max_width - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))

                # reset
                cur = []
                num_of_letters = 0
            # append
            cur += [w]
            num_of_letters += len(w)
        return res + [" ".join(cur).ljust(max_width)]
