import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.LINK)
        node2 = TextNode("this is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node3 = TextNode("this is a text node", TextType.TEXT)
        node4 = TextNode("this is also a text node", TextType.TEXT)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("this is a text node", TextType.TEXT, url="google.com")
        node6 = TextNode("this is a text node", TextType.TEXT)
        self.assertNotEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()