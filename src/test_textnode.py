import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_all_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_all_not_eq(self):
        node = TextNode("This is a text node1", "italic")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is a text node", "bold", "http://google.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is a text node", "bold", "http://yahoo.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
