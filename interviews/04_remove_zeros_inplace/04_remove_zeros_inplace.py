def task_2_remove_zeros(arr):
    # Мы должны удалять элементы без дополнительной памяти.
    # Разобъем задачу на две. 1. Перемещение всех нулей в конец массива, 2. Удаление нулей с конца.

    j = 1  # Будет указывать на первый возможный элемент, с которым мы будем меняться местами.
    num_elems = 0  # Число ненулевых элементов, чтобы сделать slice

    # Пройдем по всем элементам.
    for i in range(len(arr)):  # Уже получаем O(n)
        if arr[i] == 0:  # Если нуль, меняем его местами с первым ненулевым.
            jj = -1  # Индекс-кандидат на обмен местами
            if j <= i:  # Если первые элементы ненули, мы должны начать с элемента, правее текущего.
                j = i + 1
            while j < len(arr):  # Смотрим вперед массива
                # j = i+1 происходит только разово, когда первые элементы ненули, поэтому это еще один проход O(n)
                # Индекса j, а не двойной цикл.
                if arr[j] != 0:  # Если нашли нуль
                    jj = j  # будем с ним меняться
                    break
                j += 1
            if jj == -1:  # Если индекс-кандидат не нашелся, значит что все следующие элементы - нули, либо массив кончился
                break  # Тогда просто выходим из обработки массива.

            # Меняемся элементами. Текущим нулем и ближайшим справа не_нулем.
            arr[jj], arr[i] = arr[i], arr[jj]
        # После каждоый итерации считаем кол-во элементов, которые обработали.
        num_elems += 1

    return arr[0:num_elems]  # Сложность slice - O(k) - где k == num_elems.
    # Итого, общая сложность остается линейная, O(n)

