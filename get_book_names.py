import get_word_lists
import get_book_chunks

def get_full_names(chunks, pair_list, shorter_word_list, name_list):
    # Please note that we should probably change this to index pairs in a more
    # intuitive way
    pair_chunks = chunks[-2]
    common_pair_chunks = []
    uncommon_pair_chunks = []
    for pair_chunk in pair_chunks:
        if pair_chunk.lower() in pair_list:
            common_pair_chunks.append(pair_chunk)
        else:
            uncommon_pair_chunks.append(pair_chunk)
    #print(set(common_pair_chunks))
    #print(set(uncommon_pair_chunks))

    names = []
    not_names = []
    for uncommon_pair_chunk in uncommon_pair_chunks:
        pair = uncommon_pair_chunk.split()
        if pair[0].lower() not in shorter_word_list and pair[1].lower() not in shorter_word_list:
            names.append(uncommon_pair_chunk)
        else:
            not_names.append(uncommon_pair_chunk)
    print("Temp not names:", not_names)
    print(set(not_names))
    print("Only one missed name: John Isidore")
    # Fixed by developing a whole extra chunk of work converting common names

    first_common_last_uncommon_names = []
    for not_name in not_names:
        if not_name.split()[0] in name_list:
            first_common_last_uncommon_names.append(not_name)
    #print("IMPORTANT")
    #print(first_common_last_uncommon_names)
    return list(set(list(names) + first_common_last_uncommon_names))

def get_dadoes_full_names():
    dadoes_chunks = get_book_chunks.get_chunks("do_androids_dream_of_electric_sheep.txt")
    word_pairs = get_word_lists.get_word_pair_list()
    word_list = get_word_lists.get_word_list()
    name_list = get_word_lists.get_name_list()
    shorter_word_list = word_list[0:2000]
    shorter_name_list = name_list[0:100]

    return get_full_names(dadoes_chunks, word_pairs, shorter_word_list, shorter_name_list)

def get_bnw_full_names():
    bnw_chunks = get_book_chunks.get_chunks("brave_new_world.txt")
    word_pairs = get_word_lists.get_word_pair_list()
    word_list = get_word_lists.get_word_list()
    name_list = get_word_lists.get_name_list()
    shorter_word_list = word_list[0:2000]
    shorter_name_list = name_list[0:100]

    return get_full_names(bnw_chunks, word_pairs, shorter_word_list, shorter_name_list)

def get_aiw_full_names():
    aiw_chunks = get_book_chunks.get_chunks("carroll-alice.txt")
    word_pairs = get_word_lists.get_word_pair_list()
    word_list = get_word_lists.get_word_list()
    name_list = get_word_lists.get_name_list()
    shorter_word_list = word_list[0:2000]
    shorter_name_list = name_list[0:100]

    try:
        full_names = get_full_names(aiw_chunks, word_pairs, shorter_word_list, shorter_name_list)
    except IndexError:
        print("Some issue with pairs")
        full_names = aiw_chunks

    return full_names


if __name__ == "__main__":
    print(get_dadoes_full_names())
    print(get_bnw_full_names())
    # commented out line as not working well for alice in wonderland in this case
    #print(get_aiw_full_names())
