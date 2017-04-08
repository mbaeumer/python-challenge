#!/usr/bin/python
import unittest
from cli_handler import CliHandler

class TestliHandler(unittest.TestCase):
  def test_create_object(self):
    argv = []
    argv.append("test0")
    argv.append("test1")
    cli = CliHandler(argv)
    self.assertTrue(cli.title == "")

  def test_isVaidArgs_return_true_if_valid(self):
    argv = []
    argv.append("filename")
    argv.append("somefile.txt")
    argv.append("sometitle")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs())
    self.assertTrue(str(cli.title) == 'sometitle')

  def test_isValidArgs_return_true_multiple_words(self):
    argv = []
    argv.append("filename")
    argv.append("somefile.txt")
    argv.append("my title")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs())
    self.assertTrue(cli.title == "my title")

if __name__ == '__main__':
  unittest.main()
