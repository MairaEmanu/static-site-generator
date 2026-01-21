import unittest
from block_markdown import markdown_to_blocks, BlockType, block_to_block_type


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    

    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    
    def test_markdown_with_extra_newlines(self):
        md = """
This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_paragraph_block(self):
        block = "This is just a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_valid_heading_block_level_1(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_valid_heading_block_level_6(self):
        block = "###### This is a level 6 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
      
    def test_invalid_heading_block_hashes(self):
        block = "####### This is not a valid heading"
        self.assertFalse(block_to_block_type(block) == BlockType.HEADING)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_heading_block_no_space(self):
        block = "##This is not a valid heading"
        self.assertFalse(block_to_block_type(block) == BlockType.HEADING)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_valid_code_block(self):
        block = "```\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block_single_line(self):
        block = "> This is a quote."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
 
    def test_quote_block_multiple_lines(self):
        block = "> This is a quote.\n> It has multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_no_space(self):    
        block = ">This is not a valid quote."
        self.assertFalse(block_to_block_type(block) == BlockType.QUOTE)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_single_item(self):  
        block = "- Single item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
    def test_unordered_list_multiple_items(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid_item(self):
        block = "- one\nnot a list item"
        self.assertFalse(block_to_block_type(block) == BlockType.UNORDERED_LIST)  
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_simple(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_start_number(self):
        block = "2. First item\n3. Second item"
        self.assertFalse(block_to_block_type(block) == BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_non_incrementing(self):
        block = "1. First item\n3. Second item"
        self.assertFalse(block_to_block_type(block) == BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        

    

if __name__ == "__main__":
    unittest.main()