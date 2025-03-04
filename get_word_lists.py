import get_data

def convert_to_lines(word_counts):
    lines = word_counts.split("\n")
    # Removes last empty line from the file
    lines = lines[0:-1]
    #print("Total number of words", len(lines))
    #print(lines[0])
    #print(lines[-1])
    return lines

def get_word_list():
    word_counts = get_data.get_common_words()
    word_count_lines = convert_to_lines(word_counts)
    word_list = [line.split()[0] for line in word_count_lines]
    return word_list

def get_word_pair_list():
    word_pair_counts = get_data.get_common_word_pairs()
    word_pair_count_lines = convert_to_lines(word_pair_counts)
    word_pair_list = []
    for line in word_pair_count_lines:
        split_line = line.split()
        word_pair_list.append(f"{split_line[0]} {split_line[1]}")
    return word_pair_list

def get_name_list():
    name_counts = get_data.get_common_names()
    name_count_lines = convert_to_lines(name_counts)
    name_list = []
    for line in name_count_lines:
        name_list.append(line.split(",")[0])
    return name_list

if __name__ == "__main__":
    print(get_word_list()[0:10])
    print(get_word_pair_list()[0:5])
    print(get_name_list()[0:10])