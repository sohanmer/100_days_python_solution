# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

height = float(height)
weight = float(weight)

bmi = weight/(height ** 2)

print(int(bmi))
