"""
3170.删除星号以后字典序最小的字符串

给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。
当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：
·删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
请你返回删除所有 '*' 字符以后，剩余字符连接而成的 字典序最小 的字符串。
"""

# 字典序：按位比较
def clearStars(self, s: str) -> str:
    res = list(s)
    # 栈，维护已经读取到的序列（桶），存储位序
    stack = [[] for _ in range(26)]

    for idx, cr in enumerate(res):
        if cr != "*":
            stack[ord(cr) - ord('a')].append(idx)
        else:
            for j in range(26):
                # 桶，直接找出字典序最小的
                if stack[j]:
                    del_idx = stack[j].pop()
                    res[del_idx] = '*'
                    break

    return ''.join(cr for cr in res if cr != '*')
