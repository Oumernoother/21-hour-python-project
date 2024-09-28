import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLES = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left)+ " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

worng = 0
input("Press enter to start!")
print("-----------------------------------")
start_time = time.time()
for i in range(TOTAL_PROBLES):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i + 1)+ ": "+ expr + " " +str(answer) + " = ")
        if guess == str(answer):
            break
        worng += 1
end_time = time.time()
total_time = int(end_time - start_time)
print("-----------------------------------")
print("nice work!,you finished in",total_time,"sec")

