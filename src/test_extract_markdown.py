import unittest
from inline import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):

    def test_extract_images(self):
        text = "![image1](https://example.com/img1.jpg) and ![image2](https://example.com/img2.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            [
                ("image1", "https://example.com/img1.jpg"),
                ("image2", "https://example.com/img2.jpg"),
            ],
            result,
        )

    def test_no_image(self):
        text = "No images here, just plain text."
        result = extract_markdown_images(text)
        self.assertEqual([], result)

    def test_broken_image(self):
        text = "![broken link(https://example.com/img1.jpg)[alt](missing)"
        result = extract_markdown_images(text)
        self.assertEqual([], result)

    def test_extract_links(self):
        text = "[Boot.dev](https://www.boot.dev) and [Python](https://www.python.org)"
        result = extract_markdown_links(text)
        self.assertEqual(
            [
                ("Boot.dev", "https://www.boot.dev"),
                ("Python", "https://www.python.org"),
            ],
            result,
        )

    def test_no_links(self):
        text = "No links, only plain text."
        result = extract_markdown_links(text)
        self.assertEqual([], result)


if __name__ == "__main__":
    unittest.main()
