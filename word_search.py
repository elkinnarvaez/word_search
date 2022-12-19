from sys import stdin


def computeLPS(p):
    m = len(p)
    lps = [0]*m
    i, j = 0, 1
    lps[i] = 0  # lps[0] is always 0
    while (j < m):
        if (p[i] == p[j]):
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            if (i != 0):
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1
    return lps


def kmpSearch(t, p):
    ans = []
    n, m, i, j = len(t), len(p), 0, 0
    lps = computeLPS(p)
    while (i < n):
        if (t[i] == p[j]):
            i += 1
            j += 1
        if (j == m):
            ans.append(i - m)
            j = lps[j - 1]
        elif (t[i] != p[j] and i < n):
            if (j != 0):
                j = lps[j - 1]
            else:
                i += 1
    return ans


def get_strips(board, n, m):
    """
        Input: A word search board and its dimesions
        Output: A map cotaining the longest possible word strips in all directions (vertical, horizontal and diagonal)
    """
    strips = {'h': [], 'v': [], 'd': []}
    # Horizonal strips
    for i in range(n):
        strips['h'].append((''.join(board[i]), (i, 0)))
    # Vertical strips
    for j in range(m):
        strips['v'].append((''.join([row[j] for row in board]), (0, j)))
    # Diagonal strips
    for i in range(n):
        strip = ""
        i_prime, j_prime = i, 0
        for _ in range(min(n - i, m)):
            strip += board[i_prime][j_prime]
            i_prime += 1
            j_prime += 1
        strips['d'].append((strip, (i, 0)))
    for j in range(1, m):
        strip = ""
        i_prime, j_prime = 0, j
        for _ in range(min(m - j, n)):
            strip += board[i_prime][j_prime]
            i_prime += 1
            j_prime += 1
        strips['d'].append((strip, (0, j)))
    return strips


def word_search(board, words, n, m):
    for i in range(len(board)):
        board[i] = board[i].split()
    strips = get_strips(board, n, m)
    for word in words:
        print("Searching '{0}'".format(''.join(word)))
        locations = []
        for direction in strips:
            for index in range(len(strips[direction])):
                strip = strips[direction][index][0]
                initial_positions = kmpSearch(strip, word)
                for initial_position in initial_positions:
                    positions = []
                    if (direction == 'h'):
                        j = initial_position
                        for _ in range(len(word)):
                            positions.append((index, j))
                            j += 1
                    elif (direction == 'v'):
                        i = initial_position
                        for _ in range(len(word)):
                            positions.append((i, index))
                            i += 1
                    else:
                        pass
                    locations.append(positions)
        if len(locations) > 0:
            pass
        else:
            print("'{0}' not found".format(word))


def main():
    # Read all lines of input file. Doing this here improves the execution time as it only needs to be done once.
    lines = stdin.readlines()
    current_line = 0
    while (current_line < len(lines)):
        n, m = map(int, lines[current_line].split())
        current_line += 1
        board = []
        if (n != 0 and m != 0):
            for _ in range(n):
                board.append(lines[current_line])
                current_line += 1
            words = lines[current_line].split()
            current_line += 1
            word_search(board, words, n, m)


if __name__ == '__main__':
    main()
