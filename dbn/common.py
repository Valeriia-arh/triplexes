import collections

open_brackets = "([{<"
close_brackets = ")]}>"


def get_element(data, nucleotide_pos):
    for type in data.keys():
        for element in data[type]:
            for part in element:
                if (nucleotide_pos >= part[0]) and (nucleotide_pos < part[1]):
                    return part


def search_element(data, triplex):
    n0 = triplex[0]
    element_n0 = None
    key_n0 = None

    n1 = triplex[1]
    element_n1 = None
    key_n1 = None

    n2 = triplex[2]
    element_n2 = None
    key_n2 = None

    for type in data.keys():
        for element in data[type]:
            for part in element:
                if (n0 >= part[0]) and (n0 < part[1]):
                    element_n0 = element
                    key_n0 = type
                if (n1 >= part[0]) and (n1 < part[1]):
                    element_n1 = element
                    key_n1 = type
                if (n2 >= part[0]) and (n2 < part[1]):
                    element_n2 = element
                    key_n2 = type

    same12 = 1 if element_n0 == element_n1 else 0
    same23 = 1 if element_n1 == element_n2 else 0
    same13 = 1 if element_n0 == element_n2 else 0

    #print(same12, same23, same13)

    if key_n0 == 'stems' and key_n1 != 'stems':
        local12 = search_local(element_n0, element_n1)
    else:
        local12 = 0

    if key_n1 == 'stems' and key_n2 != 'stems':
        local23 = search_local(element_n1, element_n2)
    else:
        local23 = 0

    if key_n0 == 'stems' and key_n2 != 'stems':
        local13 = search_local(element_n0, element_n2)
    else:
        local13 = 0

    #print(local12, local23, local13)

    longrange12 = 0
    longrange23 = 0
    longrange13 = 0
    if same12 == 0 and local12 == 0:
        longrange12 = 1
    if same23 == 0 and local23 == 0:
        longrange23 = 1
    if same13 == 0 and local13 == 0:
        longrange13 = 1

    #print(longrange12, longrange23, longrange13)

    return same12, same23, same13, local12, local23, local13, longrange12, longrange23, longrange13


def search_local(element_n0, element_n1):
    i, j = 0, 0

    while i != len(element_n0) or j != len(element_n1):
        if (element_n0[i][1] == element_n1[j][0]) or (element_n0[i][0] == element_n1[j][1]):
            return 1
        else:
            if element_n0[i][0] > element_n1[j][1]:
                j += 1
            else:
                i += 1
    return 0


#'stems': [[(41, 44), (57, 60)], [(26, 28), (64, 66)], [(14, 17), (37, 40)], [(46, 49), (53, 56)], [(20, 23), (28, 31)], [(68, 73), (77, 82)], [(0, 8), (85, 93)]]
# 'internal_loop': [[(17, 20), (31, 37)], [(44, 46), (56, 57)], [(40, 41), (60, 64)]],
# 'mult': [[(8, 14), (66, 68), (82, 85)]],
# 'hairpin': [[(23, 26)], [(49, 53)], [(73, 77)]],
# 'bulging': [[(93, 94)]]}



def binary_search(data, item):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if item < data[middle][0][0]:
            high = middle - 1
        elif item > data[middle][0][1]:
            low = middle + 1
        else:
            return middle

    return -1


def to_stack(stack, i):
    j = 0
    while len(stack[j]) > 0 and stack[j][len(stack[j]) - 1] < i:
        j += 1
    stack[j].append(i)
    return j


def from_stack(stack, i):
    j = 0
    while len(stack[j]) == 0 or stack[j][len(stack[j]) - 1] != i:
        j += 1
    stack[j].pop()
    return j


def inverse_brackets(bracket):
    res = collections.defaultdict(int)
    for i, a in enumerate(bracket):
        res[a] = i
    return res


def dotbracket_to_pairtable(struct):
    pt = [0] * (len(struct) + 1)
    pt[0] = len(struct)
    stack = collections.defaultdict(list)
    inverse_bracket_left = inverse_brackets(open_brackets)
    inverse_bracket_right = inverse_brackets(close_brackets)

    i = 0
    for elem in struct:
        i += 1
        if elem == "." or elem == '-':
            pt[i] = 0
        else:
            if elem in inverse_bracket_left:
                stack[inverse_bracket_left[elem]].append(i)
            else:
                if len(stack[inverse_bracket_right[elem]]) == 0:
                    raise ValueError('ERROR. A lot of closing brackets')
                j = stack[inverse_bracket_right[elem]].pop()
                pt[i] = j
                pt[j] = i
    if len(stack[inverse_bracket_left[elem]]) != 0:
        raise ValueError('ERROR. A lot of opening brackets')
    return pt
