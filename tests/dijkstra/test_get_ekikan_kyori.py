import unittest

from src.consts.metro import GLOBAL_EKIKAN_LIST
from src.dijkstra.get_ekikan_kyori import get_ekikan_kyori


class TestGetEkikanKyori(unittest.TestCase):
    def setUp(self) -> None:
        self.eki_list = GLOBAL_EKIKAN_LIST.copy()
        return super().setUp()

    def test_all_empty(self):
        """
        引数に何も渡さない場合Infinityが返る
        """
        self.assertEqual(float("inf"), get_ekikan_kyori("", "", []))

    def test_only_list(self):
        """
        駅間リストのみ指定した場合Infinityが返る
        """
        self.assertEqual(float("inf"), get_ekikan_kyori("", "", self.eki_list))

    def test_valid_pattern_1(self):
        """
        駅間リストに存在する駅を指定した場合正しく距離が取得できる
        """
        self.assertEqual(1.5, get_ekikan_kyori("小竹向原", "氷川台", self.eki_list))

    def test_valid_pattern_2(self):
        """
        駅間リストに存在する駅を逆順で指定した場合正しく距離が取得できる
        """
        self.assertEqual(1.5, get_ekikan_kyori("氷川台", "小竹向原", self.eki_list))


if __name__ == "__main__":
    unittest.main()
