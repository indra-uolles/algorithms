https://code.google.com/codejam/contest/3264486/dashboard

| S \ K | 1 | 2 | 3 | 4 |
| ----  | - | - | - | - |
| +     | 0 | 0 | 0 | 0 |
| -     | 1 | 1 | 1 | 1 |
| ++    | 0 | 0 | 0 | 0 |
| --    | 2 | 1 | 1 | 1 |
| +-    | 1 | x | x | x |
| -+    | 1 | x | x | x |
| +++   | 0 | 0 | 0 | 0 |
| ---   | 3 | x | 1 | 1 |
| -++   | 1 | x | x | x |
| +-+   | 1 | x | x | x |
| ++-   | 1 | x | x | x |
| +--   | 2 | 1 | x | x |
| -+-   | 2 | x | x | x |
| --+   | 2 | 1 | x | x |

Закономерности
1) если строка состоит из всех + то тут и делать ничего не надо -> 0
2) если строка состоит из всех - то
    для K=1 перевороты == длина строки
    len(S), K
    len(S) <= K тогда 1
    len(S) > K
    тогда если len(S) % K = 0 то len(S)/K раз
    если  len(S) % K != 0 то X
3) если в строке -+ (рядом плюс и минус)
если в строке один -, то сколько бы + не добавляли, где бы он не находился
K = 1 тогда 1
K != 1 тогда x
4) если в строке > 1 минус и среди них нет соседних минусов то
K = 1 тогда к-во минусов
K != 1 тогда x
5) если в строке > 1 минус который соседствует с другим минусом
пусть m кол-во минусов
если K > m тогда x
если K = m тогда 1
если K < m то
если m % K == 0 тогда m/K
если m % K != 0 тогда x

к-во преобразований - t_count
1) строка состоит из всех - ?
2) строка состоит из всех + ?
3) K = 1 ?
4) в строке есть минусы с соседями? если только ОДИН и не покрывается K то X
5) выбираем минус который наиболее близок к краю строки и стараемся от него избавиться
если это минус в левой части строки то идем слева направо
если это минус в правой части строки то идем справа налево

---+-++-
1) нет 2) нет 3) нет
4) ++++-++-
   ++++---+
   ++++++++

+-+-+- K=3
+-++-+
++---+
++++++

-+-+-+ K=3
+-++-+
++---+
++++++

-+-+-+- K=3
+-++-+-
++---+-
++--+-+
++-+-++
+++-+++