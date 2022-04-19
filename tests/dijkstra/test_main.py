import unittest
from turtle import update
from typing import Tuple

from src.consts.metro import GLOBAL_EKIKAN_LIST
from src.dijkstra.main import koushin, saitan_wo_bunri
from src.types.type_dijkstra import EkiT


class TestSaitanWoBunri(unittest.TestCase):
    def setUp(self) -> None:
        self.ekiA: EkiT = EkiT("eki_a", 0.1, [])
        self.ekiB: EkiT = EkiT("eki_b", 0.2, [])
        self.ekiC: EkiT = EkiT("eki_c", 0.3, [])
        return super().setUp()

    def test_empty(self):
        """
        空のリストを渡すと例外をthrowする
        """
        with self.assertRaises(ValueError) as cm:
            saitan_wo_bunri([])
        self.assertEqual(cm.exception.args[0], "lstの長さが0です。")

    def test_length_1(self):
        """
        長さ1のリストを渡す
        """
        self.assertEqual((self.ekiA, []), saitan_wo_bunri([self.ekiA]))

    def test_length_2(self):
        """
        長さ2のリストを渡す
        """
        self.assertEqual(
            (self.ekiA, [self.ekiB]), saitan_wo_bunri([self.ekiA, self.ekiB])
        )

    def test_length_2_reverse(self):
        """
        長さ2のリストを渡す(逆順)
        """
        self.assertEqual(
            (self.ekiA, [self.ekiB]), saitan_wo_bunri([self.ekiB, self.ekiA])
        )

    def test_length_3(self):
        """
        長さ3のリストを渡す
        """
        self.assertEqual(
            (self.ekiA, [self.ekiB, self.ekiC]),
            saitan_wo_bunri([self.ekiB, self.ekiA, self.ekiC]),
        )


class TestKoushin(unittest.TestCase):
    def setUp(self) -> None:
        self.eki_list = GLOBAL_EKIKAN_LIST.copy()
        self.ekiA: EkiT = EkiT("池袋", float("inf"), [])
        self.ekiB: EkiT = EkiT("新大塚", 1.2, ["新大塚", "茗荷谷"])
        self.ekiC: EkiT = EkiT("茗荷谷", float(0), ["茗荷谷"])
        self.ekiD: EkiT = EkiT("後楽園", float("inf"), [])
        return super().setUp()

    def test_no_undef_eki(self):
        """未確定の駅がない"""
        self.assertEqual([], koushin(self.ekiB, [], self.eki_list))

    def test_undef_eki(self):
        """未確定の駅がある"""
        updated = EkiT("池袋", 3.0, ["池袋", "新大塚", "茗荷谷"])
        self.assertEqual(
            [updated, self.ekiB, self.ekiC, self.ekiD],
            koushin(
                self.ekiB, [self.ekiA, self.ekiB, self.ekiC, self.ekiD], self.eki_list
            ),
        )


if __name__ == "__main__":
    unittest.main()
