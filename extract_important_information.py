import re

def extract_important_information(book_file):
    with open(book_file, "r", encoding="utf-8") as readfile:
        text = readfile.read()

    text = text.replace("“", "\"").replace("”", "\"")
    text = text.replace("‘", "\'").replace("’", "\'")
    text = text.replace("\xad-", "-")

    print("Count analysis")

    text_no_newlines = text.replace("\n", " ")

    print("Number of characters: ", len(text_no_newlines))
    print("Number of lines: ", len(text.split("\n")))

    text_no_punctuation = text
    for punctuation in ",.?:;":
        text_no_punctuation = text_no_punctuation.replace(punctuation, "")

    text_words_only = text_no_punctuation
    for mark in "-()\n\xad-":
        text_words_only = text_words_only.replace(mark, " ")
    words = text_words_only.split()
    text_words_only = " ".join(words)

    print("Number of words: ", len(words))

    words_all_lower = text_words_only.lower().split()

    print("Number unique words: ", len(set(words_all_lower)))

    split_by_speech_marks = re.split(r"[\"]", text)
    # This line is going to have lots of issues if there is any mismatch
    speech_sections = split_by_speech_marks[1::2]
    print("Number of speech sections: ", len(speech_sections))
    text_only_speech_sections = " ".join(speech_sections).split(" ")
    print("Number of speech words: ", len(text_only_speech_sections))

    print("Other")
    print(f"Starting speech section: {speech_sections[0]}")
    print(f"Ending speech section: {speech_sections[-1]}")

if __name__ == "__main__":
    extract_important_information("dadoes.txt")

    print("-"*100)

    extract_important_information("do_androids_dream_of_electric_sheep.txt")

    print("-" * 100)

    extract_important_information("brave_new_world.txt")
