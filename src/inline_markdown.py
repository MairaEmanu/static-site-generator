import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    splitted_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splitted_nodes.append(old_node)
    
        else:
            parts = old_node.text.split(delimiter)
            num_delimiters = len(parts) - 1

            if num_delimiters % 2 != 0:
                raise Exception("Unmatched delimiter found in text.")
                

        
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        splitted_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    splitted_nodes.append(TextNode(part, text_type))

    return splitted_nodes
                

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    

def split_nodes_image(old_nodes):
    splitted_nodes = []
    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            splitted_nodes.append(old_node)
            continue

        
        text = old_node.text

        images = extract_markdown_images(text)
        while images:
            alt, url =  images[0]
            full_image = f"![{alt}]({url})"
            before, after = text.split(full_image, 1)

    
            if before:
                splitted_nodes.append(TextNode(before, TextType.TEXT))

            splitted_nodes.append(TextNode(alt, TextType.IMAGE, url=url))
            text = after
            images = extract_markdown_images(text)
            
        if text:
            splitted_nodes.append(TextNode(text, TextType.TEXT)) 
    return splitted_nodes


def split_nodes_link(old_nodes):
    splitted_nodes = []
    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            splitted_nodes.append(old_node)
            continue

        
        text = old_node.text

        links = extract_markdown_links(text)
        while links:
            alt, url =  links[0]
            full_link = f"[{alt}]({url})"
            before, after = text.split(full_link, 1)

            if before:
                splitted_nodes.append(TextNode(before, TextType.TEXT))

            splitted_nodes.append(TextNode(alt, TextType.LINK, url=url))

            text = after
            links = extract_markdown_links(text)

        if text:
            splitted_nodes.append(TextNode(text, TextType.TEXT)) 
    return splitted_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes





                
        