# The purpose of this file is for the purposes of easily keeping track of data
# used in this project and creating a simple command for extracting any of the relevant data
# sources in their most basic form

# The reason this is helpful is it puts the data generated through preprocessing
# and the raw data on an equal footing which is useful for understanding the project flow

def get_common_words():
    with open("count_1w.txt", "r", encoding="utf-8") as readfile:
        word_counts = readfile.read()
    return word_counts

def get_common_word_pairs():
    with open("count_2w.txt", "r", encoding="utf-8") as readfile:
        word_counts = readfile.read()
    return word_counts

def get_common_names():
    with open("all_names_count.txt", "r", encoding="utf-8") as readfile:
        name_counts = readfile.read()
    return name_counts

def get_dadoes_page_text():
    with open("dadoes.txt", "r", encoding="utf-8") as readfile:
        text = readfile.read()
    return text

def get_dadoes_text():
    with open("do_androids_dream_of_electric_sheep.txt", "r", encoding="utf-8") as readfile:
        text = readfile.read()
    return text

