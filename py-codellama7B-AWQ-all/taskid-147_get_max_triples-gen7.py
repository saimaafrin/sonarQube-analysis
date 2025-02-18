def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
    >>> get_max_triples(5)
    1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    # Runtime: 36 ms, faster than 86.60% of Python3 online submissions for Maximum Number of Non-Overlapping Subarrays With Sum Equals Target.
    # Memory Usage: 13.9 MB, less than 60.00% of Python3 online submissions for Maximum Number of Non-Overlapping Subarrays With Sum Equals Target.
    from collections import Counter
    def get_max_triples(n):
        """
        :type n: int
        :rtype: int
        """
        def is_multiple(x, y):
            return x % y == 0
        
        def get_max_triples(n, result):
            """
            :type n: int
            :type result: List[int]
            """
            if n == 1:
                result.append(n)
                return
            for i in range(1, n):
                get_max_triples(i, result)
            result.append(n)
        result = []
        get_max_triples(n, result)
        result = Counter(result)
        # print(result)
        return result.most_common(n=1)[0][1]
    
    # result = []
    # for i in range(1, n+1):
    #     get_max_triples(i, result)
    # print(result)
    # result = Counter(result)
    # print(result)
    # return result.most_common(n=1)[0][1]
