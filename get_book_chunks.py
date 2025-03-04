# choice one: most unique sets of words to the book
# choice two: up to 5 words in a row only
# choice three: interested in only up to 20 concepts
# choice four: need a way of determining the unique concepts
import re
import useful_functions

def is_proper(word):
    # Checks if the word has the format of a proper noun
    if word.isalpha() and word[0].isupper() and word[1::].islower():
        return True
    else:
        return False

def get_word_chunks(chunk_size, words):
    return [[words[i+j] for j in range(chunk_size)] for i in range(len(words)-chunk_size+1)]

def is_proper_chunk(word_chunks):
    return [all([is_proper(word) for word in word_chunk]) for word_chunk in word_chunks]

def get_proper_word_chunks(chunk_size, words):
    word_chunks = get_word_chunks(chunk_size, words)
    proper_word_chunks = []
    for word_chunk in word_chunks:
        if sum([is_proper(word) for word in word_chunk]) == chunk_size:
            proper_word_chunks.append(word_chunk)
    return proper_word_chunks

def get_top_chunk_size(text):
    words = text.split(" ")
    number_proper_chunks = 1
    chunk_size = 1
    chunks_sizes_valid = []
    while number_proper_chunks != 0:
        temp_number_proper_chunks = sum(is_proper_chunk(get_word_chunks(chunk_size, words)))
        if temp_number_proper_chunks != 0:
            chunks_sizes_valid.append(chunk_size)
        chunk_size += 1
        number_proper_chunks = temp_number_proper_chunks
    return chunks_sizes_valid[-1]

def get_chunks(text, top_chunk_size):
    return get_proper_word_chunks(top_chunk_size, text.split(" "))

def get_chunks_up_to_size(text, size):
    words = text.split(" ")
    chunks = []
    for chunk_size in range(1, size + 1):
        unstring_pwc = get_proper_word_chunks(chunk_size, words)
        string_pwc = [" ".join(s) for s in unstring_pwc]
        chunks.append(string_pwc)
    chunks.reverse()
    return chunks

def chunks_filler_word_cleaner(chunks):
    # Words commonly used to start a sentence which don't have any part in the "concept"
    filler_words = ["To", "And", "Or", "As", "But", "Again", "For", "At", "Any", "So",
                    "No", "Yes", "Over", "Under",
                    "An", "At", "Be", "By", "All", "If", "This", "Why",
                    "Her", "His", "He", "She", "They", "It", "On", "In", "We", "You",
                    "Maybe", "Not", "What"]
    cleaned_chunks = []
    for chunk in chunks:
        cleaned_chunk = []
        for chunk_bit in chunk:
            if chunk_bit.split()[0] not in filler_words:
                cleaned_chunk.append(chunk_bit)
        cleaned_chunks.append(cleaned_chunk)
    return cleaned_chunks

def chunks_remove_redundant_threes(chunks):
    # The reason for adding this is that if there is a long
    # four chunk that includes a sub-chunk of three titles then
    # the three chunk is often redundant
    # See: San Francisco Police Department with sub-chunk San Francisco Police
    # Then the sub-chunk is considered redundant
    new_chunks = chunks
    if len(chunks) >= 4:
        fours = chunks[-4]
        threes = chunks[-3]
        removed_threes = []
        for four in fours:
            for three in threes:
                if re.search(three, four):
                    # print("Four: ", four, "Three: ", three)
                    removed_threes.append(three)
        new_chunks[-3] = [three for three in threes if three not in removed_threes]
    return new_chunks

def get_chunks(book_file):
    with open(book_file, "r") as readfile:
        text = readfile.read()

    top_chunk_size = get_top_chunk_size(text)
    # Keeping this print statement in at the moment as it's very special
    print("largest unique to book chunk size:", top_chunk_size)

    chunks = get_chunks_up_to_size(text, top_chunk_size)
    chunks = chunks_filler_word_cleaner(chunks)
    chunks = chunks_remove_redundant_threes(chunks)

    biggest_chunks_ordered, biggest_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[0])
    print("Biggest chunks:", biggest_chunks_ordered)

    triple_chunks_ordered, triple_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[-3])
    print("Triple chunks:", triple_chunks_ordered)

    smallest_chunks_ordered, smallest_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[-1])
    cut_off = 30
    smallest_chunks_ordered_cut_off = useful_functions.cut_off_list_before_cut_off(
        smallest_chunks_ordered, smallest_chunks_ordered_count, cut_off)
    # print(smallest_chunks_ordered, smallest_chunks_ordered_count)
    print(f"Smallest chunks ordered cut off {cut_off}:",
          smallest_chunks_ordered_cut_off,
          smallest_chunks_ordered_count[:len(smallest_chunks_ordered_cut_off)])

    top_ten = smallest_chunks_ordered_cut_off
    combos = [f"{namelike1} {namelike2}" for namelike1 in top_ten for namelike2 in top_ten]
    from_combos = sorted([fullnamelike for fullnamelike in chunks[-2] if fullnamelike in combos])
    # print("From combos: ", from_combos)

    return chunks, smallest_chunks_ordered_cut_off, from_combos

def get_chunks_fileless(text):
    top_chunk_size = get_top_chunk_size(text)
    # Keeping this print statement in at the moment as it's very special
    print("largest unique to book chunk size:", top_chunk_size)

    chunks = get_chunks_up_to_size(text, top_chunk_size)
    chunks = chunks_filler_word_cleaner(chunks)
    chunks = chunks_remove_redundant_threes(chunks)

    biggest_chunks_ordered, biggest_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[0])
    print("Biggest chunks:", biggest_chunks_ordered)

    triple_chunks_ordered, triple_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[-3])
    print("Triple chunks:", triple_chunks_ordered)

    smallest_chunks_ordered, smallest_chunks_ordered_count = useful_functions.list_counter_rearrange(chunks[-1])
    cut_off = 30
    smallest_chunks_ordered_cut_off = useful_functions.cut_off_list_before_cut_off(
        smallest_chunks_ordered, smallest_chunks_ordered_count, cut_off)
    # print(smallest_chunks_ordered, smallest_chunks_ordered_count)
    print(f"Smallest chunks ordered cut off {cut_off}:",
          smallest_chunks_ordered_cut_off,
          smallest_chunks_ordered_count[:len(smallest_chunks_ordered_cut_off)])

    top_ten = smallest_chunks_ordered_cut_off
    combos = [f"{namelike1} {namelike2}" for namelike1 in top_ten for namelike2 in top_ten]
    from_combos = sorted([fullnamelike for fullnamelike in chunks[-2] if fullnamelike in combos])
    # print("From combos: ", from_combos)

    return chunks, smallest_chunks_ordered_cut_off, from_combos

def get_dadoes_chunks():
    return get_chunks("do_androids_dream_of_electric_sheep.txt")

def get_bnw_chunks():
    return get_chunks("brave_new_world.txt")

def get_aiw_chunks():
    #book = nltk.corpus.gutenberg.raw('carroll-alice.txt')
    book = ""
    return get_chunks_fileless(book)

if __name__ == "__main__":
    book_holder = [get_dadoes_chunks(), get_bnw_chunks()]
    print("\n")
    #print("I am extremely proud of myself for this amazing work")
    print("I managed to write a short program using a reasonably small amount of data")
    print("Without any AI which is able to determine the main character in a novel")
    #print("I want to try this on more books but for now I want to congratulate myself")

    """
    import nltk
    nltk.download('averaged_perceptron_tagger_eng')

    for chunks in book_holder:
        for chunk in chunks:
            viewable_chunk = sorted(set(chunk))
            print(len(viewable_chunk), viewable_chunk[0:20])
            print([nltk.pos_tag(chunk.split()) for chunk in viewable_chunk[0:20]])

    print(nltk.pos_tag("Happy Dog Pet Shop".split()))
    """

