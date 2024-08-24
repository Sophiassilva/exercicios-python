from random import randint

nums = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'''Os números gerados pelo PC foram: {nums}
O maior valor é {max(nums)} e o menor é {min(nums)}.''')