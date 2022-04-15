import string
import typing

from pydantic.dataclasses import dataclass


@dataclass
class EkimeiT:
    """
    駅名の情報を格納する型
    """

    kanji: str  # 駅名
    kana: str  # 読み
    romaji: str  # ローマ字
    shozoku: str  # 所属線名


@dataclass
class EkikanT:
    """
    駅間の情報を格納する型
    """

    kiten: str  # 起点
    shuten: str  # 終点
    keiyu: str  # 経由線名
    kyori: float  # 距離
    jikan: float  # 時間


@dataclass
class EkiT:
    """
    グラフの頂点の情報を格納する型
    """

    namae: str  # 駅名（漢字）
    saitan_kyori: float  # 最短距離
    temae_list: typing.List[str]  # 経由した駅のリスト
