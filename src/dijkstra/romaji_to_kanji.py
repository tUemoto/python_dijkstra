from typing import List

from src.types.type_dijkstra import EkimeiT


def romaji_to_kanji(eki: str, lst: List[EkimeiT]) -> str:
    """ローマ字の駅名をもとに漢字駅名を取得する

    Args:
        eki (str): ローマ字の駅名
        lst (List[EkimeiT]): 駅情報のリスト
    Returns:
        str: 対応する駅の漢字表記
    """
    if len(lst) == 0:
        return ""
    first: EkimeiT = lst.pop(0)
    if first.romaji == eki:
        return first.kanji
    return romaji_to_kanji(eki, lst)
