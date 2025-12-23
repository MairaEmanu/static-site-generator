import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph")
        node2 = HTMLNode("p", "this is a paragraph")
        self.assertEqual(node, node2)

        node3 = HTMLNode("p", "this is a paragraph", props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        node4 = HTMLNode("p", "this is a paragraph", props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node3, node4)


    def test_not_eq(self):
        node = HTMLNode("h", "this is a heading")
        node2 = HTMLNode("p", "this is a paragraph")
        self.assertNotEqual(node, node2)

        node3 = HTMLNode("p", "this is a paragraph", props={
    "href": "https://www.boot.dev",
    "target": "_blank",
})
        node4= HTMLNode("p", "this is a paragraph", props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertNotEqual(node3, node4)



if __name__ == "__main__":
    unittest.main()

