from typing import List

from src.types.type_dijkstra import EkimeiT, EkiT


def make_initial_eki_list(lst: List[EkimeiT], kiten: str) -> List[EkiT]:
    """駅名リストをもとに、始点を明示した経由駅リストを作る
    Args:
        lst (List[EkimeiT]): 駅名リスト
        kiten (str): 始点の駅名
    Returns:
        List[EkiT]: 経由駅リスト
    """

    def initialize_eki(ekimei: EkimeiT):
        if ekimei.kanji == kiten:
            return EkiT(ekimei.kanji, float(0), [ekimei.kanji])
        return EkiT(ekimei.kanji, float("inf"), [])

    return list(map(initialize_eki, lst))
