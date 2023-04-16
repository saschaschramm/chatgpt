import os

def merge_files(input_dir: str, output_file: str, endswith: str) -> None:
    with open(output_file, mode='w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(f".{endswith}"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        for line in infile:
                            outfile.write(line)
                        outfile.write('\n--------')

def main():
    home: str = os.path.expanduser("~")
    languages: list[tuple[str, str]] = [("Python", "py"), ("C", "c"), ("C-Plus-Plus", "cpp"), ("JavaScript", "js"), ("Go", "go"), ("Java", "java")]
    for language in languages:
        input_dir: str = os.path.join(home, "Downloads", language[0])
        output_file: str = os.path.join("playground", "data", f"{language[1]}.txt")
        merge_files(input_dir, output_file, endswith=language[1])
        with open(output_file, mode='r', encoding='utf-8') as infile:
            text = infile.read() 
        print(f"{language[0]} {len(text)}")

if __name__ == '__main__':
    main()