from visualiser.visualiser import Visualiser as vs
from pprint import pprint

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("There's no such thing as negative money.")

    @vs()
    def change(i, coin_sum):
        #pprint(f'i: {i}, coin_sum: {coin_sum}')
        #pprint(memo)

        if coin_sum == 0:
            return []
        elif coin_sum in memo:
            return memo[coin_sum]
        else:
            fewest = None

            for j in range(i, len(coins)):
                cur_coin = coins[j]
                sub_sum = coin_sum - cur_coin

                if cur_coin <= coin_sum:
                    sub_combo = change(i=j, coin_sum=sub_sum)

                    if sub_combo is not None:
                        combo = [cur_coin]+sub_combo

                        if fewest is None or len(combo) < len(fewest):
                            fewest = combo

            if (fewest is not None and
                (coin_sum not in memo or len(memo[coin_sum]) < len(fewest))):
                memo[coin_sum] = fewest
            return fewest

    memo = {}
    fewest_coins = change(0, target)
    pprint(memo)
    if fewest_coins is None:
        raise ValueError('No change was found')
    return fewest_coins


if __name__ == '__main__':
    print(find_fewest_coins([1, 2, 5], 47))
    #vs.make_animation("make_change.gif", delay=2)
