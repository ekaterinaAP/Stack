from Stack import Stack


def balance_check(text):
    brackets_open = ['[', '(', '{']
    brackets_close = [']', ')', '}']

    result = 'сбалансировано'
    for letter in text:
        if letter in brackets_open:
            text_to_check.push(brackets_open.index(letter))
            # Stack.push(text_to_check, brackets_open.index(letter))
        elif letter in brackets_close:
            if not text_to_check.is_empty() and text_to_check.peek() == brackets_close.index(letter):
                text_to_check.pop()
            else:
                result = 'не сбалансировано'

    if not text_to_check.is_empty():
        result = 'не сбалансировано'

    return result


if __name__ == '__main__':

    text_to_check = Stack('(нужно провер{ит[ь} баланс] скобок)')
    print(balance_check(text_to_check.string))













