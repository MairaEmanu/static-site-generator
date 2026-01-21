from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE= "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    cleaned_markdown = []
    pieces = markdown.split("\n\n")


    for piece in pieces:
        
        if len(piece) > 0:
            cleaned_piece = piece.strip()
            cleaned_markdown.append(cleaned_piece)
        else:
            continue


    return cleaned_markdown


def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")

    if len(lines) == 0:
        return None
    
    if lines[0].startswith("#"):
        line = lines[0]
        count = 0
        while count < len(line) and line[count] == "#":
            count += 1

        if 1 <= count <= 6 and line[count] == " " and count < len(line):
            return BlockType.HEADING
        
    
    
    
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE
    

    if lines[0].startswith("> "):
        is_qoute = True
        for line in lines:
            if not line.startswith("> "):
                is_qoute = False
                break
        if is_qoute:
            return BlockType.QUOTE
        

    if lines[0].startswith("- "):
        is_unordered_list = True
        for line in lines:
            if not (line.startswith("- ")):
                is_unordered_list = False
                break
        if is_unordered_list:
            return BlockType.UNORDERED_LIST


    
    if lines[0].startswith(f"1. "):
        is_ordered_list = True
        counter = 1
        for line in lines:
            if not line.startswith(f"{counter}. "):
                is_ordered_list = False
                break
            counter += 1
        if is_ordered_list:
            return BlockType.ORDERED_LIST
     

    return BlockType.PARAGRAPH

        
        