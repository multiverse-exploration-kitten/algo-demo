def compute_lps_array(pattern):
    """Compute the longest prefix-suffix (LPS) array."""
    length = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps_array(pattern)
    i = j = 0  # index for text[] and pattern[]

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return "Found pattern at index " + str(i - j)

        # mismatch after j matches
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == "__main__":
    # Example usage
    text_example = "ABABDABACDABABCABAB"
    pattern_example = "ABABCABAB"
    kmp_search(text_example, pattern_example)
