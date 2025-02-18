from typing import List

def eat(number: int, need: int, remaining: int) -> List[int]:
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    >>> eat(5, 6, 10)
    [11, 4]
    >>> eat(4, 8, 9)
    [12, 1]
    >>> eat(1, 10, 10)
    [11, 0]
    >>> eat(2, 11, 5)
    [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

    # code here

    # 생각을 많이 하지 말고 문제를 엄격하게 읽자
    # 문제에서 원하는 것은 몇 개의 칸칸이 먹혔는지와 남은 칸칸 수 이다
    # 첫 번째 값은 총 몇 개 먹었는지를 담는다
    # 두 번째 값은 남은 칸칸 수 를 담는다

    result = [number, 0]

    if number + need <= remaining:
        result[0] = number + need
        result[1] = remaining - number - need

    else:
        result[0] = remaining
        result[1] = 0

    return result
