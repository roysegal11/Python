def Age_group(a):
    if 0 <= a <= 18:
        answer = "chuld"
    if 18 < a <= 60:
        answer = "adult"
    if 60 < a <= 120:
        answer = "senior"
    return answer


for i in range(6):
    age = int(input("Age: "))
    print(Age_group(age))
