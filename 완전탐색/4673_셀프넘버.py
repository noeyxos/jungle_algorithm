# 셀프넘버 
# https://www.acmicpc.net/problem/4673

# 100보다 작은 셀프 넘버 
# 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97



def d(n):
    self_number = n
    while n > 0 : 
        self_number += n % 10
        n //= 10
    return self_number

# 1부터 10000까지의 숫자 집합
numbers = set(range(1, 10001))

# 생성된 숫자를 저장할 집합
generated_numbers = set()

# 1부터 10000까지의 숫자로 생성 가능한 숫자 구하기
for num in range(1, 10001):
    generated = d(num)
    if generated <= 10000:
        generated_numbers.add(generated)

# 셀프 넘버는 전체 숫자에서 생성된 숫자를 제외
self_numbers = numbers - generated_numbers

for self_num in sorted(self_numbers):
    print(self_num)
    