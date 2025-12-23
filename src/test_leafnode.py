import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag(self):
        node = LeafNode(None,"Hello")
        self.assertEqual(node.to_html(), "Hello")

    def test_leaf_no_value(self):
        node = LeafNode("p",None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_link_with_href(self):
        node = LeafNode("a", "Click me", {"href": "https://www.google.com"})
        self.assertIn('href="https://www.google.com"', node.to_html())
        self.assertIn("<a", node.to_html())
        self.assertIn(">Click me</a>", node.to_html())

    def test_leaf_with_multiple_props(self):
        node = LeafNode("span", "hi", {"class": "greeting", "id": "msg"})
        html = node.to_html()
        self.assertIn("<span", html)
        self.assertIn('class="greeting"', html)
        self.assertIn('id="msg"', html)
        self.assertIn(">hi</span>", html)

if __name__ == "__main__":
    unittest.main()

