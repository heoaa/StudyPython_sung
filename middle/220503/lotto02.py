# 번호 가중치를 준 로또프로그램

import random as rnd

numbers = weights = list(range(1,46))     # [i for i in range(1,46)]
lotto = []
rnd.shuffle(weights)

lotto = rnd.choices(numbers, weights=weights, k=6)   # choices 한번에 6개 찾음

lotto.sort()
print(lotto)