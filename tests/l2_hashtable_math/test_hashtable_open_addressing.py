import unittest

from src.l2_hashtable_math.hashtable_open_addressing import HashMapOpenAddressing


class TestHashMapOpenAddressing(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMapOpenAddressing()

    def test_insert_and_search(self):
        self.hash_map.insert("key1", "value1")
        self.hash_map.insert("key2", "value2")
        self.assertEqual(self.hash_map.search("key1"), "value1")
        self.assertEqual(self.hash_map.search("key2"), "value2")
        self.assertIsNone(self.hash_map.search("key3"))

    def test_insert_update(self):
        self.hash_map.insert("key1", "value1")
        self.hash_map.insert("key1", "value2")
        self.assertEqual(self.hash_map.search("key1"), "value2")

    def test_delete(self):
        self.hash_map.insert("key1", "value1")
        self.hash_map.delete("key1")
        self.assertIsNone(self.hash_map.search("key1"))

    def test_collision(self):
        self.hash_map.insert(1, "value1")
        self.hash_map.insert(
            11, "value2"
        )  # assuming default size of 10, 1 and 11 will collide
        self.assertEqual(self.hash_map.search(1), "value1")
        self.assertEqual(self.hash_map.search(11), "value2")

    def test_rehashing(self):
        for i in range(8):
            self.hash_map.insert(f"key{i}", f"value{i}")
        self.assertEqual(self.hash_map.size, 10)
        self.hash_map.insert("key8", "value8")
        self.assertEqual(self.hash_map.size, 20)
        self.assertEqual(self.hash_map.search("key8"), "value8")
        self.assertEqual(self.hash_map.search("key0"), "value0")


if __name__ == "__main__":
    unittest.main()
