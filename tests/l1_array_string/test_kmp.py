import unittest

from src.l1_array_string.kmp import kmp_search


class TestKMP(unittest.TestCase):

    def test_kmp_search(self):
        test_cases = [
            {
                "text": "abxabcabcaby",
                "pattern": "abcaby",
                "expected": "Found pattern at index 6",
            },
            {
                "text": "aaaaab",
                "pattern": "aaab",
                "expected": "Found pattern at index 2",
            },
            {
                "text": "abcdabcabcdabcdab",
                "pattern": "abcdab",
                "expected": "Found pattern at index 0",
            },
            {
                "text": "this is a test text",
                "pattern": "test",
                "expected": "Found pattern at index 10",
            },
            {"text": "abcdef", "pattern": "gh", "expected": None},
            {
                "text": "aaaaaa",
                "pattern": "aaa",
                "expected": "Found pattern at index 0",
            },
        ]

        for case in test_cases:
            text = case["text"]
            pattern = case["pattern"]
            expected = case["expected"]
            result = kmp_search(text, pattern)
            self.assertEqual(
                result, expected, f"Failed for text: '{text}' and pattern: '{pattern}'"
            )


if __name__ == "__main__":
    unittest.main()
