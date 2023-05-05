def read_single_line_to_str(path):
    with open(path, "r") as file:
        content = file.readline()
    return content

if __name__ == "__main__":
    out = read_single_line_to_str("../2015/input_2015_1.txt")
