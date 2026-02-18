import re

# Compile a regex pattern for valid mobile numbers
pattern = re.compile(r'^[789]\d{9}$')

# Number of inputs
n = int(input())

for _ in range(n):
    number = input().strip()
    if pattern.match(number):
        print("YES")
    else:
        print("NO")
