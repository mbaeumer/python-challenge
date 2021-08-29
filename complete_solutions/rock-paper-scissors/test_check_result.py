import unittest
from rock_paper_scissors import check_result
from game_result import GameResult

class SumTestCase(unittest.TestCase):
  def test_rock_paper(self):
    self.assertTrue(check_result("R", "P") == GameResult.COMPUTER_LOOSE)

  def test_rock_scissors(self):
    self.assertTrue(check_result("R", "S") == GameResult.COMPUTER_WIN)

  def test_paper_rock(self):
    self.assertTrue(check_result("P", "R") == GameResult.COMPUTER_WIN)

  def test_paper_scissors(self):
    self.assertTrue(check_result("P", "S") == GameResult.COMPUTER_LOOSE)

  def test_rock_rock(self):
    self.assertTrue(check_result("R", "R") == GameResult.DRAW)


if __name__ == '__main__':
  unittest.main()