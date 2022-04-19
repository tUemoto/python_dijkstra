import functools
from dataclasses import dataclass
from typing import List, Mapping, Tuple

from src.types.type_dijkstra import EkiT


def saitan_wo_bunri(lst: List[EkiT]) -> Tuple[EkiT, List[EkiT]]:
    """駅情報のリストを受け取り、その中で、最短距離最小の駅と
    それ以外の駅のリストに分割して返却する
    Args:
        lst: (List[EkiT]): 駅情報のリスト
    Returns:
        Tuple[EkiT, List[EkiT]]: 最短距離最小の駅とそれ以外の駅のリスト
    """
    if len(lst) == 0:
        raise ValueError("lstの長さが0です。")

    if len(lst) == 1:
        return (lst[0], [])

    # 与えられたiteratorに対して、要素の逆順にfuncを実行する（初期値: acc）メソッド
    fold_right = lambda func, acc, xs: functools.reduce(
        lambda x, y: func(y, x), xs[::-1], acc
    )

    def _compare_eki(current: EkiT, accumulator: Tuple[EkiT, List[EkiT]]):
        """2駅を比較してsaitan_kyoriの短い方を指定のフォーマットにして返す
        Args:
            current (EkiT): 比較対象1
            accumulator (Tuple[EkiT, List[EkiT]]): 0番目の要素を比較対象1と比較
        Returns:
            Tuple[EkiT, List[EkiT]]
        """
        if current.saitan_kyori < accumulator[0].saitan_kyori:
            accumulator[1].insert(0, accumulator[0])
            return (current, accumulator[1])
        accumulator[1].insert(0, current)
        return accumulator

    return fold_right(_compare_eki, (lst.pop(), []), lst)
