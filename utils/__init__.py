from .MsgTunnel import MsgTunnel
from copy import deepcopy


def __find_pos(cards):
    return cards


def is_all_sequence_or_triplet(cards):
    pass


def remove_pair(sorted_cards, v):
    result = deepcopy(sorted_cards)
    result.remove(v)
    result.remove(v)
    return result


def can_win(hands):
    sorted_cards = deepcopy(hands).sort()
    pos = __find_pos(sorted_cards)
    if len(pos) == 0:
        return False
    if len(pos) == 7:
        return True
    # 遍历所有对，因为胡必须有对
    last_pair_tile = None
    for v in pos:
        if v == last_pair_tile:
            continue
        else:
            last_pair_tile = v
        cards = remove_pair(sorted_cards, v)
        if is_all_sequence_or_triplet(cards):
            return True
    return False


def calculate_shanten(hands):
    pass
