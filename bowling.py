def score(game):
    result = 0
    frame = 1
    half = 1
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
            result += get_value(game[i+1])
        else:
            result += get_value(game[i])
        if frame < 10  and (game[i] == 'X' or game[i] == 'x'):
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        if (game[i] == 'X' or game[i] == 'x') or half % 2 ==0:
            frame += 1
        half += 1
    return result

def get_value(char):
    for i in range(1,10):
        if char == str(i):
            return int(char)
    if char in ("xX/"):
        return 10
    else:
        return 0