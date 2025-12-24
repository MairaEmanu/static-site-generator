import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    
    def test_to_html_without_tag_raises_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "A tag is required.")


    def test_to_html_without_children_raises_error(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "At least one child node is required.")


    def test_to_html_with_properties(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )

    def test_to_html_nested_structure(self):
        grandchild_node1 = LeafNode("i", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><i>grandchild1</i><b>grandchild2</b></span></div>",
        )


    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={})
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

if __name__ == "__main__":
    unittest.main()

