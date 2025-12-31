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
                






                
        