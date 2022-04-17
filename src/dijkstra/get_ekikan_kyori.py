from typing import List

from src.types.type_dijkstra import EkikanT


def get_ekikan_kyori(ekimei1: str, ekimei2: str, lst: List[EkikanT]) -> float:
    """漢字の駅名２つと駅間リストを受け取り、
    駅間リストに照らし合わせて2駅間の距離を返す
    Args:
        ekimei1 (str): 漢字の駅名（起点）
        ekimei2 (str): 漢字の駅名 (終点)
        lst (List[EkikanT]): 駅間リスト
    Returns:
        (float): 2駅間の距離
    """
    if len(lst) == 0:
        return float("inf")
    first: EkikanT = lst.pop(0)
    if first.kiten == ekimei1 and first.shuten == ekimei2:
        return first.kyori
    elif first.kiten == ekimei2 and first.shuten == ekimei1:
        return first.kyori
    else:
        return get_ekikan_kyori(ekimei1, ekimei2, lst)
