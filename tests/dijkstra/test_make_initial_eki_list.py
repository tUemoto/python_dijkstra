import unittest

from src.consts.metro import GLOBAL_EKIMEI_LIST
from src.dijkstra.make_ekimei_list import make_initial_eki_list
from src.types.type_dijkstra import EkiT


class TestRomajiToCanji(unittest.TestCase):
    def setUp(self) -> None:
        self.eki_list = GLOBAL_EKIMEI_LIST[0:3]
        return super().setUp()

    def test_empty_list_empty_str(self):
        """
        [異常系]空のリストと空文字を渡すと空のリストが返る

        """
        self.assertEqual([], make_initial_eki_list([], ""))

    def test_empty_list_invalid_str(self):
        """
        [異常系]空のリストと任意の文字列を渡すと空のリストが返る

        """
        self.assertEqual([], make_initial_eki_list([], "hoge"))

    def test_valid_list_empty_str(self):
        """
        [異常系]正常なリストと空文字を渡すとそのままリストが返される

        """
        self.assertEqual(
            [
                EkiT("代々木上原", float("inf"), []),
                EkiT("代々木公園", float("inf"), []),
                EkiT("明治神宮前", float("inf"), []),
            ],
            make_initial_eki_list(self.eki_list, ""),
        )

    def test_valid_list_invalid_str(self):
        """
        [異常系]正常なリストとリストに存在しない駅名を渡すとそのままリストが返される

        """
        self.assertEqual(
            [
                EkiT("代々木上原", float("inf"), []),
                EkiT("代々木公園", float("inf"), []),
                EkiT("明治神宮前", float("inf"), []),
            ],
            make_initial_eki_list(self.eki_list, "hoge"),
        )

    def test_valid_list_valid_str(self):
        """
        [正常系]正常なリストとリストに存在する駅名を渡すと起点が定義されたリストが返される

        """
        self.assertEqual(
            [
                EkiT("代々木上原", float("inf"), []),
                EkiT("代々木公園", float(0), ["代々木公園"]),
                EkiT("明治神宮前", float("inf"), []),
            ],
            make_initial_eki_list(self.eki_list, "代々木公園"),
        )


if __name__ == "__main__":
    unittest.main()
