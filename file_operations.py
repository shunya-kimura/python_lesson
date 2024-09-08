# file_operations.py

# ファイルにコンテンツを書き込む関数
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# ファイルからコンテンツを読み取る関数
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
# メイン関数
def main():
    filename = "sampele.text" # 使用するファイルの名前
    content = "This is a sample test file." # ファイルに書き込むコンテント

    # ファイルにコンテンツを書き込む
    write_to_file(filename, content)
    print(f"Content written to {filename}")

    #　ファイルからコンテンツを読み取る
    read_content = read_from_file(filename)
    print(f"Content read from {filename}: {read_content}")

# このファイルが直接実行された場合、main関数を呼び出す
if __name__ == "__main__":
    main()