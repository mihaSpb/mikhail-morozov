def sum_list_elements(list_1, list_2):
    result_list = []

    # Нахожу самый длинный список из двух
    max_length = max(len(list_1), len(list_2))

    for i in range(max_length):
        # Если индекс выходит за пределы списка, то использую 0 вместо отсутствующего элемента списка
        element_1 = list_1[i] if i < len(list_1) else 0
        element_2 = list_2[i] if i < len(list_2) else 0
        result_list.append(element_1 + element_2)
    return result_list


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 100, 543]

    # Получаем новый список, где каждый элемент - сумма соответствующих элементов list1 и list2
    summed_list = sum_list_elements(list1, list2)
    print("Результирующий список:", summed_list)


main()
