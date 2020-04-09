from Stack import Stack


def balance_check(text):
    brackets_open = ['[', '(', '{']
    brackets_close = [']', ')', '}']

    result = 'сбалансировано'
    for letter in text:
        if letter in brackets_open:
            Stack.push(text_to_check, brackets_open.index(letter))
        elif letter in brackets_close:
            if not Stack.is_empty(text_to_check) and Stack.peek(text_to_check) == brackets_close.index(letter):
                Stack.pop(text_to_check)
            else:
                result = 'не сбалансировано'
    # if Stack.size(text_to_check) == 0:
    if Stack.is_empty(text_to_check):
        pass
    else:
        result = 'не сбалансировано'

    return result


if __name__ == '__main__':

    text_to_check = Stack('(нужно провер{ит[ь} баланс] скобок)')
    print(balance_check(text_to_check.string))













