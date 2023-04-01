from FlowNetwork import FlowNetwork


# acceptable_chars == 
#   set(string.printable)
#     .difference({'\r', '\v', '\f'})
#     .add({'ñ', 'Ñ'})

acceptable_chars = {
    #numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    #letters
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    #symbols
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\',']', '^', '_', '`', '{', '|',
    '}', '~', 
    #invisible
    ' ', '\t', '\n',
}

def load_network(path):
    nw = FlowNetwork()

    with open(path, 'r') as file:
        for line in file:

            sanitized = ''.join(filter(lambda c: c in acceptable_chars, line))
            words = sanitized.split()
            if(len(words) == 0): continue

            assert(words[0] in 'cpna')
            w0, w1, w2 = words[0], words[1], words[2]

            if  (w0 == 'c' or w0 == 'p'): continue
            elif(w0 == 'n'): nw.set_st(w1, w2)
            elif(w0 == 'a'): nw.add_arc(w1, w2, int(words[3]))

    return nw
