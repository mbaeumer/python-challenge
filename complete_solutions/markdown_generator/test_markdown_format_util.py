#!/usr/bin/python
import unittest
from markdown_format_util import generate_heading
from markdown_format_util import generate_bullet_list
from markdown_format_util import generate_italic_text
from markdown_format_util import generate_bold_text
from markdown_format_util import generate_code_snippet
from markdown_format_util import generate_link
from markdown_format_util import generate_image

class TestMarkdownFormatUtil(unittest.TestCase):
  def test_generate_heading_level_one(self):
    self.assertTrue(generate_heading(1, "heading one") == "# heading one")

  def test_generate_heading_level_two(self):
    self.assertTrue(generate_heading(2, "heading two") == "## heading two")

  def test_generate_bullet(self):
    expected = self.create_expected_string()
    test_list = self.create_test_list()
    self.assertTrue(generate_bullet_list(test_list) == expected)  

  def test_generate_italic_text(self):
    expected = "__italics__"
    text = "italics"
    self.assertTrue(generate_italic_text(text) == expected)

  def test_generate_bold_text(self):
    expected = "**bold**"
    text = "bold"
    self.assertTrue(generate_bold_text(text) == expected)
  
  def test_generate_code_snippet(self):
    expected = "{% highlight python %}\n"
    expected = expected + "print('teststring')\n"
    expected = expected + "{% endhighlight %}\n"
    actual = generate_code_snippet("print('teststring')")
    self.assertTrue(actual == expected)

  def test_generate_link(self):
    expected = "[some title](http://url.com)"
    actual = generate_link("some title", "http://url.com") 
    self.assertTrue(actual == expected)

  def test_generate_image(self):
    expected = "![](path/to/file)"
    path = "path/to/file"
    actual = generate_image(path)
    self.assertTrue(actual == expected)
  
  def create_test_list(self):
    list = []
    list.append("bullet1")
    list.append("bullet2")
    list.append("bullet3")
    return list

  def create_expected_string(self):
    result = "\n\n"
    result = result + "* bullet1\n"
    result = result + "* bullet2\n"
    result = result + "* bullet3\n"
    result = result + "\n"
    return result

if __name__ == '__main__':
  unittest.main()
