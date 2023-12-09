def check_horizontal(direction: int, match: int, line: str):
    value = 0
    expanding = ''
    newline = list(line)
    while match > 0 and match < len(line) - 1\
            and line[match + direction].isdigit():
        expanding += line[match + direction]
        newline[match + direction] = '.'
        match += direction
    if expanding != '':
        value = int(expanding[::direction])
    return value, "".join(newline)


def check_vertical(match: int, line: str):
    value = 0
    expanding = ''
    newline = list(line)
    if line[match].isdigit():
        while match >= 1 and line[match - 1].isdigit():
            match -= 1
        while match < len(line) and line[match].isdigit():
            expanding += line[match]
            newline[match] = '.'
            match += 1
        if expanding != '':
            value = int(expanding)
    return value, "".join(newline)


def check_left(match: int, line: str):
    return check_horizontal(-1, match, line)


def check_right(match: int, line: str):
    return check_horizontal(1, match, line)


def check_around(match: int, lines: list[str]):
    values, lines = get_adyacent_values(match, lines)
    return sum(values), lines


def get_adyacent_values(match: int, lines: list[str]):
    line_above, line_actual, line_below = lines
    left, line_actual = check_left(match, line_actual)
    right, line_actual = check_right(match, line_actual)
    above, line_above = check_vertical(match, line_above)
    la_diag = ra_diag = 0
    if not above:
        la_diag, line_above = check_left(match, line_above)
        ra_diag, line_above = check_right(match, line_above)
    below, line_below = check_vertical(match, line_below)
    lb_diag = rb_diag = 0
    if not below:
        lb_diag, line_below = check_left(match, line_below)
        rb_diag, line_below = check_right(match, line_below)
    value = [left, right, above, la_diag,
             ra_diag, below, lb_diag, rb_diag]
    return value, [line_above, line_actual, line_below]
