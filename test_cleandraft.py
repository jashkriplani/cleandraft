import unittest
from cleandraft import clean_markdown

class CleanMarkdownTests(unittest.TestCase):
    def test_trailing_spaces_removed(self):
        self.assertEqual(clean_markdown("hello   \n"), "hello\n")

    def test_multiple_blank_lines_collapsed(self):
        self.assertEqual(clean_markdown("a\n\n\n\nb"), "a\n\nb\n")

    def test_heading_spacing_normalized(self):
        self.assertEqual(clean_markdown("##Heading##"), "## Heading\n")

    def test_final_newline_added(self):
        self.assertEqual(clean_markdown("hello"), "hello\n")

if __name__ == "__main__":
    unittest.main()
