import unittest
from typing import Tuple

from src.dijkstra.main import saitan_wo_bunri
from src.types.type_dijkstra import EkiT

ekiA: EkiT = EkiT("eki_a", 0.1, [])
ekiB: EkiT = EkiT("eki_b", 0.2, [])
ekiC: EkiT = EkiT("eki_c", 0.3, [])


class TestSaitanWoBunri(unittest.TestCase):
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
        self.assertEqual((ekiA, []), saitan_wo_bunri([ekiA]))

    def test_length_2(self):
        """
        長さ2のリストを渡す
        """
        self.assertEqual((ekiA, [ekiB]), saitan_wo_bunri([ekiA, ekiB]))

    def test_length_2_reverse(self):
        """
        長さ2のリストを渡す(逆順)
        """
        self.assertEqual((ekiA, [ekiB]), saitan_wo_bunri([ekiB, ekiA]))

    def test_length_3(self):
        """
        長さ3のリストを渡す
        """
        self.assertEqual((ekiA, [ekiB, ekiC]), saitan_wo_bunri([ekiB, ekiA, ekiC]))


if __name__ == "__main__":
    unittest.main()
