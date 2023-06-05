def check_input(num_input: int, new_dict_auto: dict) -> None:
    """
        функция для отсеивания не правильного ввода названия марки
    автомобиля, проверяет чтобы при вводе не вводилось чbсло 0 и не повторялась
    дважды название марки автомобиля. Если название марки подходит - добавляет ее в словарь
      {"название марки авто": 0 (кол-во голосов)}
    :param num_input: int - номер вводимой марки автомобиля
    :param new_dict_auto: dict - словарь с уже введенными марками автомобилей
    :return: None
    """
    while True:
        name_auto = input(f'Введите модель {num_input + 1}-го автомобиля: ')
        if name_auto == '0':
            print('0 это не марка автомобиля! Повторите ввод.')
            continue
        if name_auto in new_dict_auto.keys():
            print('Введенная марка автомобиля уже вводилась! Повторите ввод!')
            continue
        new_dict_auto[name_auto] = 0
        break


def input_auto(count_auto: int) -> dict:
    """
    Функция ввода названий марок автомобилей для голосования
    :param count_auto: int - необходимое количество вводов марок автомобилей
    :return: dict - словарь с введенными марками автомобилей для голосования.
        в качестве ключей в списке-название марки, в качестве значений-количество голосов
    """
    new_dict_auto = dict()
    for num_auto in range(count_auto):
        check_input(num_auto, new_dict_auto)
    print('\nГолосование создано!')
    return new_dict_auto


def input_choice_auto(dict_all_auto: dict) -> None:
    """
    Функция ввода и обработки выбора пользователя
    :param dict_all_auto: dict - словарь с уже введенными марками автомобилей для голосования.
        в качестве ключей в списке-название марки, в качестве значений-количество голосов
    :return: None
    """
    while True:
        print(f'\nВведите модель из списка: {"; ".join((dict_all_auto.keys()))}')
        print('Для подсчета голосов введите 0')
        choice = input(f'Ваш выбор?:\n')
        if choice in dict_all_auto.keys():
            print('Ваш голос принят!')
            dict_all_auto[choice] += 1
            continue
        elif choice == '0':
            print('Голосование завершено!')
            break
        print('!!введена модель не из списка, повторите выбор!!')


def begin(max_count: int = 20) -> int:
    """
    функция запуска голосования. Выдает заголовок приветствие и запрашивает необходимое
    количество марок автомобилей для голосования
    :param max_count: int - максимальное количество вводимых марок (ограничение)
    :return: int - введенное пользователем необходимое количество марок автомобилей для
        голосования
    """
    print('Голосование за автомобиль года \n')
    count_auto = 0
    while True:
        try:
            count_auto = int(input('Сколько моделей авто учавствуют в голосовании?: '))
        except ValueError:
            print('ввели не число! Повторите ввод')
            continue
        if count_auto > max_count or count_auto < 2:
            print(f'требуется ввести число от 2 до {max_count}! Повторите ввод')
            continue
        break
    return count_auto


def result(dict_auto_result: dict) -> None:
    """
    Функция подсчета и вывода результата голосования
    :param dict_auto_result: dict - словарь {'марка авто': кол-во голосов} для подсчета
    максимального кол-ва голосов
    :return: None
    """
    max_bals = max(dict_auto_result.values())
    tuple_best_auto = (auto for auto in dict_auto_result.keys() if dict_auto_result[auto] == max_bals)
    print('Лучший автомобиль года:')
    print(f'{", ".join(tuple_best_auto)}')
    print(f'Количество голосов: {max_bals}')


if __name__ == "__main__":
    dict_auto = input_auto(begin())
    input_choice_auto(dict_auto)
    result(dict_auto)
