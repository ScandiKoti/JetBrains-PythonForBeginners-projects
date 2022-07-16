msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (int(v1) == 1 or int(v2) == 1) and v3 == '*':
        msg += msg_7
    if (int(v1) == 0 or int(v2) == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if - 10 < v < 10 and v == int(v):
        return True
    else:
        return False


mod = ["+", "-", "*", "/"]
memory = 0
while True:
    result = 0
    print(msg_0)
    x, oper, y = input().split()
    if x == 'M':
        x = memory
        if y == 'M':
            y = memory
    elif y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in mod:
        print(msg_2)
        continue
    check(x, y, oper)
    if oper == '+':
        result = x + y
        print(result)
    elif oper == '-':
        result = x - y
        print(result)
    elif oper == '*':
        result = x * y
        print(result)
    elif oper == '/':
        if y != 0:
            result = x / y
            print(result)
        else:
            print(msg_3)
            continue
    print(msg_4)
    answer_store = input()
    if answer_store == 'n':
        memory = 0
    elif answer_store == 'y':
        if is_one_digit(result) is False:
            memory = result
        else:
            msg_index = 10
            print(msg_[msg_index])
            answer_digit = input()
            if answer_digit == 'y':
                msg_index = 10
                while msg_index < 12:
                    msg_index += 1
                    print(msg_[msg_index])
                    answer_digit = input()
                    if answer_digit == 'n':
                        break
                    memory = result
    print(msg_5)
    answer_continue = input()
    if answer_continue == 'y':
        continue
    else:
        break
