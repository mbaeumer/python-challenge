#!/usr/bin/python
import unittest
from cli_handler import CliHandler
from cli_validation_result import ValidationResult

class TestCliHandler(unittest.TestCase):
  def test_isValidArgs_return_OK_empty_title(self):
    argv = []
    argv.append("filename.py")
    argv.append("targetfile.markdown")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.OK)
    self.assertTrue(cli.title == "")
    self.assertTrue(str(cli.targetFilename) == "targetfile.markdown")

  def test_isValidArgs_return_OK_sometitle(self):
    argv = []
    argv.append("filename")
    argv.append("somefile.markdown")
    argv.append("sometitle")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.OK)
    self.assertTrue(str(cli.title) == 'sometitle')

  def test_isValidArgs_return_OK_multiple_words(self):
    argv = []
    argv.append("filename")
    argv.append("somefile.markdown")
    argv.append("my title")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.OK)
    self.assertTrue(cli.title == "my title")

  def test_isValidArgs_return_HELP(self):
    argv = []
    argv.append("filename")
    argv.append("-help")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.HELP)
  
  def test_isValidArgs_return_NOT_ENOUGH_ARGS(self):
    argv = []
    argv.append("filename")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.NOT_ENOUGH_ARGS)
  
  def test_isValidArgs_return_NOT_MARKDOWN(self):
    argv = []
    argv.append("filename")
    argv.append("filename.txt")
    cli = CliHandler(argv)
    self.assertTrue(cli.isValidArgs() == ValidationResult.NOT_MARKDOWN)

if __name__ == '__main__':
  unittest.main()
