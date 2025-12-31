import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_one_node(self):
        node= TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)


    def test_split_nodes_delimiter_multiple_nodes(self):
        nodes = [
            TextNode("Start **bold** middle ", TextType.TEXT),
            TextNode("**another bold** end", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Start ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" middle ", TextType.TEXT),
            TextNode("another bold", TextType.BOLD),
            TextNode(" end", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)


    def test_split_nodes_delimiter_no_delimiters(self):
        node = TextNode("This is plain text without delimiters.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [TextNode("This is plain text without delimiters.", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)


    def test_split_nodes_delimiter_unmatched_delimiter(self):
        node = TextNode("This text has an unmatched ** delimiter.", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "Unmatched delimiter found in text.")

    def test_split_nodes_delimiter_non_text_node(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, url="http://example.com"),
            TextNode(" and more **bold** text.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, url="http://example.com"),
            TextNode(" and more ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)


    def test_split_nodes_delimiter_adjacent_delimiters(self):
        node = TextNode("This is **bold****and more bold** text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("and more bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)


    


if __name__ == "__main__":
    unittest.main()

