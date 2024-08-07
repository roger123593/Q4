import re
import sys

def parse_file(filename):
    # 正則表達式模式
    pattern = re.compile(r'([A-Za-z]+) stays in [A-Za-z]+ at (\d{2}:\d{2} (?:AM|PM))$')

    try:
        with open(filename, 'r') as file:#讀檔
            lines = file.readlines()
            for line in lines:
                match = pattern.search(line.strip())
                if match:
                    name, time = match.groups()
                    print(f"{name}, {time}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
        filename = sys.argv[1]
        parse_file(filename)
