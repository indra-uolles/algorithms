import pdb
import re

filepath = 'A-small-practice.in'
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

def get_transf_pos(S):
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

# flips_cnt
# def get_flips(S, K, count = None):
#     if count is None:
#         count = 0

#     if is_positive(S):
#         return count
#     elif is_negative(S) and K == 1:
#         return len(S) + count
#     elif is_negative(S) and len(S) <= K:
#         return 1 + count
#     elif is_negative(S) and len(S) > K and len(S) % K == 0:
#         return len(S)/K + count
#     elif is_negative(S) and len(S) > K and len(S) % K != 0
#         return -1
#     else:
#         lmc = lone_minus_cnt(S)
#         if lmc == 1:
#             #эне. надо сначала понять он покроется K или нет
#             return -1
#         else:
#             S = hide_minus(S, K)
#             get_flips(S, K, count + 1)

def flips(S, K):
    return S

with open(filepath) as fp:
    line = fp.readline()
    i = 1
    while line:
        if i > 1:
            S, K = line.split(' ', 2)
            ans.append(flips(S, K)+'\n')
            # pdb.set_trace()

        i += 1
        line = fp.readline()

output.writelines(ans)
output.close()
