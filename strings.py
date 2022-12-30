from typing import Optional, List

def FindLast(s: str, sub: str) -> Optional[int]:
    def buildTable(sub: str, table: List[int], i: int, j: int) -> List[int]:
        if i >= len(sub):
            return table
        if sub[i] == sub[j]:
            table[i] = j+1
            return buildTable(sub, table, i + 1, j + 1)
        else:
            if j == 0:
                table[i] = 0
                return buildTable(sub, table, i + 1, j)
            else:
                return buildTable(sub, table, i, table[j-1])
    def impl(s: str, sub: str, table: List[int], i: int, j: int) -> Optional[int]:
        if i == -1:
            return None
        if s[i] == sub[j]:
            if j + 1 == len(sub):
                return i
            else:
                return impl(s, sub, table, i - 1, j + 1)
        else:
            if j == 0:
                return impl(s, sub, table, i - 1, j)
            else:
                return impl(s, sub, table, i, table[j - 1])

    sub = "".join(reversed(sub))
    table = buildTable(sub, [0]*len(sub), 1, 0)
    return impl(s, sub, table, len(s) - 1, 0)

print(FindLast("coololoo", "ol"))
