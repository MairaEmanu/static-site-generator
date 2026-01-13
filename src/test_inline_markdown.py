import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
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


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    
    def test_no_matches(self):
        no_image_matches = extract_markdown_images("This text has no images.")
        no_link_matches = extract_markdown_links("This text has no links.")
        self.assertListEqual([], no_image_matches)
        self.assertListEqual([], no_link_matches)


    def test_multiple_matches(self):
        image_text = "![img1](http://img1.png) and ![img2](http://img2.png)"
        link_text = "[link1](http://link1.com) and [link2](http://link2.com)"
        
        image_matches = extract_markdown_images(image_text)
        link_matches = extract_markdown_links(link_text)
        
        self.assertListEqual(
            [("img1", "http://img1.png"), ("img2", "http://img2.png")],
            image_matches
        )
        self.assertListEqual(
            [("link1", "http://link1.com"), ("link2", "http://link2.com")],
            link_matches
        )


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )


    def test_split_images_no_images(self):
        node = TextNode("This text has no images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)


    def test_split_links_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)


    def test_split_images_non_text_node(self):
        nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and more text.", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(nodes, new_nodes)

    def test_split_links_non_text_node(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("[link](https://example.com)", TextType.LINK, "https://example.com"),
            TextNode(" and more text.", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(nodes, new_nodes)
    

    def test_text_to_textnodes_plain_text(self):
        text = "This is a sample text."
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("This is a sample text.", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)


    def test_text_to_textnodes_with_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_italic(self):
        text = "This is _italic_ text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_code(self):
        text = "This is `code` text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_multiple_formats(self):
        text = "This is **bold**, _italic_, and `code`."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),             
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)
    

    def test_text_to_textnodes_link(self):
        text = "This is a [link](https://example.com)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    
    def test_text_to_textnodes_image(self):
        text = "This is an ![image](https://i.imgur.com/zjjcJKZ.png)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)




    


if __name__ == "__main__":
    unittest.main()

