from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    max_value
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    counts = [0] * (max_value + 1)  # инициализируем массив для подсчета
    for num in container:  # считаем количество каждого элемента в массиве
        counts[num] += 1
    sorted_container = []
    for i in range(len(counts)):  # восстанавливаем отсортированный массив
        sorted_container += [i] * counts[i]
    return sorted_container
# пустая строка
