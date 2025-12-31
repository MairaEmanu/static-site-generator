import unittest
from textnode import TextNode, TextType, text_node_to_html_node


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

    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")


    def test_code(self):
        node = TextNode("print('Hello, World!')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, World!')")


    def test_link(self):
        node = TextNode("OpenAI", TextType.LINK, url="https://www.openai.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "OpenAI")
        self.assertEqual(html_node.props["href"], "https://www.openai.com")


    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, url="https://www.example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://www.example.com/image.png")
        self.assertEqual(html_node.props["alt"], "An image")

    def test_unknown_text_type(self):
        class FakeTextType:
            UNKNOWN = "unknown"

        node = TextNode("Unknown", FakeTextType.UNKNOWN)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertTrue("Unknown TextType" in str(context.exception))


if __name__ == "__main__":
    unittest.main()