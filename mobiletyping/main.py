# Translate a text message to a sequence of keystrokes
# Sequences that represents different letters with the same
# key should be separated by '_'
# http://dojopuzzles.com/problemas/exibe/escrevendo-no-celular/

keyboard = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' ',
}


def get_keystrokes(char):
    for key, letters in keyboard.items():
        if char in letters:
            return key * (letters.index(char) + 1)


def type_on_phone(msg):
    typing = ''
    for char in msg:
        press = get_keystrokes(char)
        if typing.endswith(press[0]):
            typing += '_'
        typing += press
    return typing


def test_equals(got, expected):
    if not expected == got:
        print('Expected: {}, got: {}'.format(expected, got))


if __name__ == '__main__':
    test_equals(type_on_phone('g'), '4')
    test_equals(type_on_phone('h'), '44')
    test_equals(type_on_phone('i'), '444')

    test_equals(type_on_phone('d'), '3')
    test_equals(type_on_phone('e'), '33')
    test_equals(type_on_phone('f'), '333')

    test_equals(type_on_phone('w'), '9')
    test_equals(type_on_phone('x'), '99')
    test_equals(type_on_phone('y'), '999')
    test_equals(type_on_phone('z'), '9999')

    test_equals(type_on_phone('hey'), '4433999')
    test_equals(type_on_phone('nice'), '6644422233')
    test_equals(type_on_phone('hey you'), '4433999099966688')

    test_equals(type_on_phone('python'), '7999844666_66')
