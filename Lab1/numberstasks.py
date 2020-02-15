def is_Palindrom(number):
    '''
    int -> bool
    Functions returns True if number is palindrom and False otherwise.
    >>> is_Palindrom(77)
    True
    >>> is_Palindrom(90)
    False
    '''
    number = str(number)
    answer = True
    lengt = len(number)
    if lengt % 2 == 0:
        for var in range(0, int(lengt / 2)):
            if number[var] != number[lengt - var - 1]:
                answer = False
    else:
        for var in range(0, int(lengt//2)):
            if number[var] != number[lengt - var - 1]:
                answer = False
    if answer:
        return True
    return False


def kaprekar_numbers(digits_number):
    '''
    int -> list
    Function finds all Kaprekar numbers that have given number of digits.
    >>> kaprekar_numbers(1)
    [1, 9]
    '''
    answer = []
    for var in range(10**(digits_number-1), 10**(digits_number)):
        square = str(var**2)
        lst_numbers = [el for el in square]
        if (int('0' + ''.join(lst_numbers[0:len(square)//2])) +
            int('0' + ''.join(lst_numbers[len(square)//2:])) == var or
            int('0' + ''.join(lst_numbers[0:len(square)//2 + 1])) +
            int('0' + ''.join(lst_numbers[len(square)//2 + 1:])) == var or
            int('0' + ''.join(lst_numbers[0:len(square)//2 - 1])) +
            int('0' + ''.join(lst_numbers[len(square)//2 - 1:])) == var) and\
        int(''.join(lst_numbers[len(square)//2:])) != 0:
                    answer.append(var)
    return answer


def multiply_numbers_not_pal(lst_numbers):
    '''
    list -> list
    Function returns list of numbers that aren't palindroms and are
    result of muliplying two different numbers from the list.
    '''
    answer = []
    for var_1 in lst_numbers:
        for var_2 in lst_numbers:
            if var_1 != var_2 and not is_Palindrom(var_1*var_2):
                answer.append(var_1*var_2)
    return list(set(answer))


def find_two_digits_square(number):
    '''
    int -> list
    Function returns list of tuples of all y and z that
    given number = y**2 + z**2.
    >>> find_two_digits_square(2)
    [(1, 1)]
    '''
    answer = []
    for y in range(0, number+1):
        for z in range(0, number+1):
            if y**2 + z**2 == number:
                answer.append((y, z))
    return answer


def main_1():
    result = min(multiply_numbers_not_pal(kaprekar_numbers(4)))
    return result, find_two_digits_square(result)


def leiland_numbers(digits_number):
    '''
    int -> list
    Function finds all Leiland numbers that have given number of digits.
    >>> leiland_numbers(1)
    [8]
    '''
    answer = []
    for x in range(2, 10**(digits_number)):
        for y in range(2, 10**(digits_number)):
            var = x**y + y**x
            if len(str(var)) == digits_number:
                answer.append(var)
    return sorted(list(set(answer)))


def find_two_digits_multiply(number):
    '''
    int -> list
    Function returns list of tuples of all y and z that given number = y*z.

    '''
    answer = []
    for y in range(1, number+1):
        for z in range(1, number+1):
            if y*z == number:
                answer.append((y, z))
    return list(set(answer))


def main_2():
    result = max(multiply_numbers_not_pal(leiland_numbers(5)))
    return result, find_two_digits_multiply(result)


def multiply_numbers_ascend(lst_numbers):
    '''
    list -> list
    Function returns list of nummbers which digits are in ascending
    order and are result of muliplying two different numbers from the list.
    '''
    answer = []
    for var_1 in lst_numbers:
        for var_2 in lst_numbers:
            if var_1 != var_2 and ascending_digits(var_1*var_2):
                answer.append(var_1*var_2)
    return list(set(answer))


def ascending_digits(number):
    '''
    int -> bool
    Function checks if all digits in the number are in ascending order.
    >>> ascending_digits(123)
    True
    >>> ascending_digits(1452)
    False
    '''
    number = str(number)
    final = True
    for var in range(0, len(number)-1):
        if not number[var] <= number[var+1]:
            final = False
    return final


def threemorph_numbers(digits_number):
    '''
    int -> list
    Function finds all threemorph numbers that have given number of digits.
    >>> threemorph_numbers(1)
    [1, 4, 5, 6, 9]
    '''
    answer = []
    for var in range(1, 10**(digits_number)):
        if int(str(var**3)[-len(str(var)):]) == var and\
        len(str(var)) == digits_number:
            answer.append(var)
    return answer


def main_3():
    result = max(multiply_numbers_ascend(threemorph_numbers(5)))
    return result, find_two_digits_square(result)


def multiply_numbers_not_lish(lst_numbers):
    '''
    list -> list
    Function returns list of nummbers that aren't Lishrel and are result
    of muliplying two different numbers from the list.
    '''
    answer = []
    for var_1 in lst_numbers:
        for var_2 in lst_numbers:
            if var_1 != var_2 and not is_lishrel(var_1*var_2):
                answer.append(var_1*var_2)
    return list(set(answer))


def avtomorph_numbers(digits_number):
    '''
    int -> list
    Function finds all avtomorph numbers that have given number of digits.
    >>> avtomorph_numbers(1)
    [0, 1, 5, 6]
    '''
    answer = []
    for var in range(0, 10**(digits_number)):
        if int(str(var**2)[-len(str(var)):]) == var and len(str(var)) == \
        digits_number:
            answer.append(var)
    return answer


def is_lishrel(number):
    '''
    int -> bool
    Functions returns True if number is lishrel and False otherwise.
    >>> is_lishrel(123)
    False
    '''
    if not is_Palindrom(int(''.join([el for el in reversed(str(number))])) +
    number):
        return True
    return False


def main_4():
    result = min(multiply_numbers_not_lish(avtomorph_numbers(6)))
    return result, find_two_digits_multiply(result)


def numberstasks(task=1):
    '''
    Pre: task = 1 or 2 or 3 or 4
    int -> tuple
    The main function that performs the chosen variant of the exam
    and returns result.
    >>> numberstasks(5)
    'Wrong number'
    '''
    if task == 1:
        main_1()
    if task == 2:
        main_2()
    if task == 3:
        main_3()
    if task == 4:
        main_4()
    else:
        return 'Wrong number'
