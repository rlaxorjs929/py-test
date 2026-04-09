print("** 로또 추첨을 시작합니다. **")
import random
a,b,c,d,e,f = random.sample(range(1,46),6)
nums = sorted([a, b, c, d, e, f])
print()
print("추첨된 로또 번호 ==>",*nums)