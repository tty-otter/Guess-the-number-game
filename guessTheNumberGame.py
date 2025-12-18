import random

# 最小値、最大値の入力
n = int(input("Min: "))
m = int(input("Max: "))

# 整合性の確認と範囲内のランダムな数値を生成
def guessTheNumber(n, m):
    if n > m:
        return None
    return random.randint(n, m)

# 生成数値と答え合わせ
def answerTheNumber(correct, guess):
    if guess < correct:
        return "Small"
    elif guess > correct:
        return "Large"
    else:
        return "Correct"

correct = guessTheNumber(n, m)

# 入力数値が要件と異なる場合
if correct is None:
    print("Error")
else:
    # answerTheNumber関数を繰り返して生成数値を当てられるまで繰り返し
    while True:
        guess = int(input("Your guess: "))
        result = answerTheNumber(correct, guess)
        if result == "Small":
            print("Too small")
        elif result == "Large":
            print("Too large")
        else:
            print("Correct")
            break

    
