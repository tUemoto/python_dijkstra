from typing import List

from src.types.type_dijkstra import EkimeiT


def romaji_to_kanji(eki: str, lst: List[EkimeiT]) -> str:
    if len(lst) == 0:
        return ""
    first: EkimeiT = lst.pop(0)
    if first.get("romaji") == eki:
        return first.get("kanji")
    return romaji_to_kanji(eki, lst)
