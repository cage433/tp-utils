from typing import TypeVar, Callable, Tuple


class ListUtils:
    S = TypeVar("S")
    T = TypeVar("T")
    @staticmethod
    def partition(values: list[S], pred: Callable[[S], bool]) -> Tuple[list[S], list[S]]:
        true_values = []
        false_values = []
        for v in values:
            if pred(v):
                true_values.append(v)
            else:
                false_values.append(v)
        return true_values, false_values


    @staticmethod
    def group_into(values: list[S], func: Callable[[S], T]) -> dict[T, list[S]]:
        result = dict()
        for v in values:
            key = func(v)
            result[key] = result.get(key, []) + [v]
        return result