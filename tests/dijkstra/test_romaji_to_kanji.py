import unittest

from src.consts.metro import GLOBAL_EKIMEI_LIST
from src.dijkstra.romaji_to_kanji import romaji_to_kanji


class TestRomajiToCanji(unittest.TestCase):
    def setUp(self) -> None:
        self.eki_list = GLOBAL_EKIMEI_LIST.copy()
        return super().setUp()

    def test_empty_str_empty_list(self):
        """
        [異常系]空文字と空のリストを渡すと空文字が返る

        """
        self.assertEqual("", romaji_to_kanji("", []))

    def test_invalid_str_empty_list(self):
        """
        [異常系]対応が存在しない文字と空のリストを渡すと空文字が返る
        """
        self.assertEqual("", romaji_to_kanji("hoge", []))

    def test_empty_str_non_empty_list(self):
        """
        [異常系]空文字と任意の空でないリストを渡すと空文字が返る
        """
        self.assertEqual("", romaji_to_kanji("", self.eki_list))

    def test_invalid_str_empty_list(self):
        """
        [正常系]対応が存在しない文字と任意の空でないリストを渡すと空文字が返る
        """
        self.assertEqual("", romaji_to_kanji("hoge", self.eki_list))

    def test_valid_str_valid_list(self):
        """
        [正常系] 渡したリストの中にある対応する駅名が返る
        """
        self.assertEqual("白金台", romaji_to_kanji("shirokanedai", self.eki_list))


if __name__ == "__main__":
    unittest.main()
