import unittest

from src.sample import samplemethod


class TestSampleMethod(unittest.TestCase):
    """test class of samplemethod"""

    def test_sample(self):
        """test method for samplemethod"""
        self.assertEqual("hoge", samplemethod("hoge"))


if __name__ == "__main__":
    unittest.main()
