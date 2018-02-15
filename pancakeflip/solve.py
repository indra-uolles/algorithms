import pdb
import re

filepath = 'A-large-practice.in'
output = open('output.txt', 'w')
ans = []
regex = re.compile(r'(-)+')

def is_negative(S):
    return (S.count('-') == len(S))

def is_positive(S):
    return (S.count('+') == len(S))

def lone_minus_cnt(S):
    match = regex.findall(S)
    return len(match)

def transf_pos(S):
    matches = re.finditer(r'(-)+', S)
    pos = [(name.start(0), name.end(0) - 1) for name in matches]

    first_pos = pos[0][0]
    last_pos = pos[len(pos) - 1][1]
    d_first_pos = first_pos
    d_last_pos = len(S) - 1 - last_pos

    if d_first_pos <= d_last_pos:
        return (pos[0][0], 1)
    else:
        return (pos[len(pos) - 1][1], -1)

def transfIter(a, i):
    b = list(a)
    if b[i] == '+':
        b[i] = '-'
    elif b[i] == '-':
        b[i] = '+'
    return "".join(b)

def transf(S, pos, K):
    k = 0
    start, direction = pos
    if direction == 1:
        while start + k < len(S) and k < K:
            S = transfIter(S, start + k)
            k += 1
    else:
        while start - k >= 0 and k < K:
            S = transfIter(S, start - k)
            k += 1
    return S

# предполагается что у S только один минус с соседями
def is_block_minus(S, K):
    matches = re.finditer(r'(-)+', S)
    pos = [(name.start(0), name.end(0) - 1) for name in matches]
    minus_len = pos[0][1] - pos[0][0] + 1
    if K <= minus_len and minus_len % K == 0:
        return False
    else:
        return True

def check(S, K, m):
    finished = False
    count = m

    if is_positive(S):
        finished = True
    elif is_negative(S) and K == 1:
        count += len(S)
        finished = True
    elif is_negative(S) and len(S) <= K:
        count += 1
        finished = True
    elif is_negative(S) and len(S) > K and len(S) % K == 0:
        count = len(S)/K + count
        finished = True
    elif is_negative(S) and len(S) > K and len(S) % K != 0:
        count = -1
        finished = True
    elif lone_minus_cnt(S) == 1 and is_block_minus(S, K):
        count = -1
        finished = True

    return (finished, count)

def flips_cnt(S, K):
    finished = False
    count = 0

    while finished == False:
        finished, count = check(S, K, count)
        if finished == False:
            S = transf(S, transf_pos(S), K)
            count += 1

    return count

def formatted_flips_cnt(i, n):
    res = int(n)
    if n == -1:
        res = 'IMPOSSIBLE'
    return 'Case #{0}: {1}'.format(i, res)

with open(filepath) as fp:
    line = fp.readline()
    i = 1
    while line:
        if i > 1:
            S, K = line.split(' ', 2)
            n = flips_cnt(S, int(K))
            ans.append(formatted_flips_cnt(i - 1, n) + '\n')

        i += 1
        line = fp.readline()

output.writelines(ans)
output.close()
