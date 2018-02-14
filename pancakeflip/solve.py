# import pdb

filepath = 'A-small-practice.in'
output = open('output.txt', 'w')
ans = []

def flips(S, K):
    return S

with open(filepath) as fp:
    line = fp.readline()
    i = 1
    while line:
        # print("Line {}: {}".format(i, line.strip()))
        if i > 1:
            S, K = line.split(' ', 2)
            ans.append(flips(S, K)+'\n')
            # pdb.set_trace()

        i += 1
        line = fp.readline()

output.writelines(ans)
output.close()
