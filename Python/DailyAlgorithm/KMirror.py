# 2081. k 镜像数字的和
def kMirror(k,n):
    # 判断字符串是否回文
    def isPalindrome(word):
        return word == word[::-1]

    # 十进制转k进制
    def toBaseK(num, k):
        res = ""
        while num:
            res += str(num % k)
            num //= k
        res = res[::-1]
        return res

    # 基本思路：枚举一半的回文，拼接，分为奇数拼接偶数拼接
    # 12 => 121 / 1221
    # 偶数拼接必然比奇数拼接多一位，也就必然比奇数拼接大
    # 为了找出最小的，需要保证递增，则以原数字的位数枚举
    # 假设现在在枚举N位，则下一个N+1位的回文也必然大于N位
    # 2*N < 2*(N+1)-1 = 2*N+1
    # 则对所有N位的先枚举所有奇数回文再偶数回文
    # 和、个数、位数
    total, count, length  = 0, 0, 1
    while count < n:
        # 构造奇数长度回文
        for half in range(10**(length - 1), 10**(length)):
            tempStr = str(half)
            # 不重复最后一位
            palin = int(tempStr + tempStr[-2::-1])
            if isPalindrome(toBaseK(palin, k)):
                total += palin
                count += 1
                if count == n:
                    return total
        for half in range(10**(length - 1), 10**(length)):
            tempStr = str(half)
            # 不重复最后一位
            palin = int(tempStr + tempStr[::-1])
            if isPalindrome(toBaseK(palin, k)):
                total += palin
                count += 1
                if count == n:
                    return total
        length += 1
    return 0


kMirror(2,5)
