# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# сортировка выбором
def sort_list_imperative(numbers):
    for i in range(0, len(numbers) - 1):
        smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[smallest]:
                smallest = j
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    return numbers


if __name__ == '__main__':
    nums = [8, 4, 9, 5, 10, 1, 2]
    print(sort_list_imperative(nums))