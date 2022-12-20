from sys import stdin


def compute_lps(p):
    """
    This method computes the longest proper prefix of a pattern that also happens to be a suffix of the same pattern.

    Input: A string value p, representing the pattern that is being found
    Output: An array with the longest proper prefixes that are also profer suffixes of p
    """
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


def kmp_search(t, p):
    """
    This method computes all the occurrences of a pattern in a given text.

    Input: Two string values t and p, where p represents the pattern that needs to be found in the text t
    Output: An array with the starting positions where p occurs in t as a substring
    """
    ans = []
    n, m, i, j = len(t), len(p), 0, 0
    lps = compute_lps(p)
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
        This method gets the longest possible word strips in the board in all directions (vertical, horizontal, digonal).

        Input: A n x m word search board
        Output: A map cotaining the longest possible word strips in all directions with its respective starting positions (vertical, horizontal and diagonal)
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
    """
    This method prints the positions of the words that were found in the board

    Input: A n x m word search board and a list of words to find in the board
    Output: None
    """
    for i in range(len(board)):
        board[i] = board[i].split()
    strips = get_strips(board, n, m)
    for word in words:
        print("Searching '{0}'".format(''.join(word)))
        word_board_positions = []
        for direction in strips:
            for (strip, strip_pos) in strips[direction]:
                word_strip_positions = kmp_search(strip, word)
                for word_strip_pos in word_strip_positions:
                    word_board_pos = []
                    if (direction == 'h'):
                        j = word_strip_pos
                        for _ in range(len(word)):
                            word_board_pos.append((strip_pos[0], j))
                            j += 1
                    elif (direction == 'v'):
                        i = word_strip_pos
                        for _ in range(len(word)):
                            word_board_pos.append((i, strip_pos[1]))
                            i += 1
                    else:
                        i = strip_pos[0] + word_strip_pos
                        j = strip_pos[1] + word_strip_pos
                        for _ in range(len(word)):
                            word_board_pos.append((i, j))
                            i = i + 1
                            j = j + 1
                    word_board_positions.append(word_board_pos)
        if len(word_board_positions) > 0:
            sep = False
            for word_board_pos in word_board_positions:
                if not sep:
                    sep = True
                else:
                    print("-------------")
                for i in range(len(word)):
                    print("{0} - {1}".format(word[i], word_board_pos[i]))
        else:
            print("'{0}' not found".format(word))


def main():
    """
    This method is in charge of the standard input and output

    Input: None
    Output: None
    """
    # Read all lines of input file. Doing this here improves the execution time as it only needs to be done once.
    lines = stdin.readlines()
    current_line = 0
    case_num = 1
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
            print("Case #{0}".format(case_num))
            word_search(board, words, n, m)
            case_num += 1


if __name__ == '__main__':
    main()
