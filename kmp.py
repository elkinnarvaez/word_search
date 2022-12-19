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


def main():
    t = "ABABDABACDABABCABAB"
    p = "DABA"
    ans = kmpSearch(t, p)
    if (len(ans) == 0):
        print("The pattern p doesn't exist in t")
    else:
        for i in ans:
            print(i, end=" ")
        print()


main()
