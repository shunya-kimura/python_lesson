# calculator.py

# 加算関数
def add(x, y):
    return x + y

# 減算関数
def subtract(x, y):
    return x - y

# 乗算関数
def multiply(x, y):
    return x * y

#除算関数(ゼロ除算のエラーチェックを含む)
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# メイン関数
def main():
    # 操作の選択肢を表示
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # ユーザーから操作の選択を入力
    choice = input("Enter choice(1/2/3/4): ")

    # ユーザーから数値を入力
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 選択された操作に基づいて計算を実行
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

# このファイルが直接実行された場合、main関数を呼び出す
if __name__ == "__main__":
    main()