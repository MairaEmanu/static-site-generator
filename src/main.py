from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)

    htmlnode = HTMLNode("p", "this is a paragraph",)
    print(htmlnode)






main()
