import string
from typing import List


class Solution:
    def ladder_length(
        self, begin_word: str, end_word: str, word_list: List[str]
    ) -> int:
        if end_word not in word_list:
            return 0

        forward = {begin_word}
        backward = {end_word}
        word_list = set(word_list)

        step = 1

        while forward and backward:
            if forward & backward:
                return step

            if len(forward) > len(backward):
                forward, backward = backward, forward

            next_batch = set()

            for word in forward:
                for i in range(len(begin_word)):
                    for char in string.ascii_lowercase:
                        new_word = word[:i] + char + word[i + 1 :]
                        if new_word not in word_list:
                            continue
                        next_batch.add(new_word)

            word_list -= forward
            forward = next_batch
            step += 1

        return 0
