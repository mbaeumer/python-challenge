#!/usr/bin/python
import unittest
from markdown_format_util import generate_heading
from markdown_format_util import generate_bullet_list


class TestMarkdownFormatUtil(unittest.TestCase):
  def test_generate_heading_level_one(self):
    self.assertTrue(generate_heading(1, "heading one") == "# heading one")

  def test_generate_heading_level_two(self):
    self.assertTrue(generate_heading(2, "heading two") == "## heading two")

  def test_generate_bullet(self):
    expected = self.create_expected_string()
    test_list = self.create_test_list()
    self.assertTrue(generate_bullet_list(test_list) == expected)  

  def create_test_list(self):
    list = []
    list.append("bullet1")
    list.append("bullet2")
    list.append("bullet3")
    return list

  def create_expected_string(self):
    result = "\n"
    result = result + "* bullet1\n"
    result = result + "* bullet2\n"
    result = result + "* bullet3\n"
    result = result + "\n"
    return result

if __name__ == '__main__':
  unittest.main()
