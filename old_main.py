import re
import get_book_chunks
import get_book_names
import get_word_lists
import useful_functions

def separate_first_last_names():
    full_names = get_book_names.get_dadoes_full_names()
    chunks = get_book_chunks.get_dadoes_chunks()

    print(full_names)
    print(chunks)

    last_names = list(set(full_name.split()[1] for full_name in full_names))
    print(last_names)

    last_names_name_dict = {last_name: [] for last_name in last_names}
    for full_name in full_names:
        for last_name in last_names:
            if full_name.split()[1] == last_name:
                last_names_name_dict[last_name].append(full_name)

    print(last_names_name_dict)

    first_names = list(set(full_name.split()[0] for full_name in full_names))
    print(first_names)

    first_names_name_dict = {first_name: [] for first_name in first_names}
    for full_name in full_names:
        for first_name in first_names:
            if full_name.split()[0] == first_name:
                first_names_name_dict[first_name].append(full_name)

    print(first_names_name_dict)

    # Gets names labelled as first and last names
    both = list(set.intersection(set(first_names), set(last_names)))

    common_names = get_word_lists.get_name_list()[0:5000]
    common_both = [namelike for namelike in both if namelike in common_names]
    print("Both: ", both)
    print("Common both: ", common_both)

    for name in common_both:
        print(name)
        last_names.remove(name)

    print("Adjusted last names:", last_names)

    print(sorted(first_names))
    print(sorted(last_names))
    print(sorted(full_names))

    return first_names, last_names

def get_first_last_names_dicts(full_names):
    last_names = list(set(full_name.split()[1] for full_name in full_names))

    last_names_name_dict = {last_name: [] for last_name in last_names}
    for full_name in full_names:
        for last_name in last_names:
            if full_name.split()[1] == last_name:
                last_names_name_dict[last_name].append(full_name)

    first_names = list(set(full_name.split()[0] for full_name in full_names))

    first_names_name_dict = {first_name: [] for first_name in first_names}
    for full_name in full_names:
        for first_name in first_names:
            if full_name.split()[0] == first_name:
                first_names_name_dict[first_name].append(full_name)

    return first_names_name_dict, last_names_name_dict

def get_main_character_first_name():
    chunks = get_book_chunks.get_dadoes_chunks()
    single_chunks = chunks[3]
    first_names, last_names = separate_first_last_names()

    first_names = sorted(list(set(first_names)))
    last_names = sorted(list(set(last_names)))

    first_name_counts = [chunks[3].count(first_name) for first_name in first_names]
    main_character = first_names[first_name_counts.index(max(first_name_counts))]
    print("Main character:", main_character)
    return main_character

if __name__ == "__main__":
    # commented out main character first name to find a more simple way of doing
    # things
    #main_character_first_name = get_main_character_first_name()

    # commented out the line in case the names functionality is redundant
    # we are going to attempt to get it from chunks on their own
    # full_names = get_book_names.get_dadoes_full_names()
    chunks, smallest_chunks_ordered_cut_off, from_combos = get_book_chunks.get_dadoes_chunks()
    first_names_dict, last_names_dict = get_first_last_names_dicts(chunks[-2])
    main_character_first_name = smallest_chunks_ordered_cut_off[0]
    print("Main character first name:", main_character_first_name)
    try:
        main_character_full_name = first_names_dict[main_character_first_name]
        print("Main character full name:", set(main_character_full_name))
    except:
        print("Standard full name for main character could not be retrieved")

    actual_names = []
    for potential_first_or_last_name in smallest_chunks_ordered_cut_off:
        try:
            potential_actual_names = first_names_dict[potential_first_or_last_name]
            # Sorts the options by popularity and extracts the most popular
            best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
            actual_names.append(best_pick_actual_name)
        except KeyError:
            try:
                potential_actual_names = last_names_dict[potential_first_or_last_name]
                # Sorts the options by popularity and extracts the most popular
                best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
                actual_names.append(best_pick_actual_name)
            except KeyError:
                actual_names.append(None)
                print(f"Full name couldn't be retrieved for {potential_first_or_last_name}")
    print("Actual names:", actual_names)
    removable_actual_names = []
    for actual_name in actual_names:
        for three in chunks[-3]:
            if re.search(actual_name, three):
                removable_actual_names.append(actual_name)
    print("Removable actual names:", removable_actual_names)

    actual_names = [actual_name for actual_name in actual_names if actual_name not in removable_actual_names]
    print("Actual names again:", actual_names)

    chunks, smallest_chunks_ordered_cut_off, from_combos = get_book_chunks.get_bnw_chunks()
    first_names_dict, last_names_dict = get_first_last_names_dicts(chunks[-2])
    main_character_first_name = smallest_chunks_ordered_cut_off[0]
    print("Main character first name:", main_character_first_name)
    """
    # The main character full name simple retrieval from the first names dict isn't effective
    try:
        main_character_full_name = first_names_dict[main_character_first_name]
        print("Main character full name:", set(main_character_full_name))
    except:
        print("Standard full name for main character could not be retrieved")
    """

    actual_names = []
    for potential_first_or_last_name in smallest_chunks_ordered_cut_off:
        try:
            potential_actual_names = first_names_dict[potential_first_or_last_name]
            # Sorts the options by popularity and extracts the most popular
            best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
            actual_names.append(best_pick_actual_name)
        except KeyError:
            try:
                potential_actual_names = last_names_dict[potential_first_or_last_name]
                # Sorts the options by popularity and extracts the most popular
                best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
                actual_names.append(best_pick_actual_name)
            except KeyError:
                actual_names.append(None)
                print(f"Full name couldn't be retrieved for {potential_first_or_last_name}")
    print("Actual names:", actual_names)

    removable_actual_names = []
    for actual_name in actual_names:
        for three in chunks[-3]:
            if re.search(actual_name, three):
                removable_actual_names.append(actual_name)
    print("Removable actual names:", removable_actual_names)

    actual_names = [actual_name for actual_name in actual_names if actual_name not in removable_actual_names]
    print("Actual names again:", actual_names)

    chunks, smallest_chunks_ordered_cut_off, from_combos = get_book_chunks.get_aiw_chunks()
    first_names_dict, last_names_dict = get_first_last_names_dicts(chunks[-2])
    main_character_first_name = smallest_chunks_ordered_cut_off[0]
    print("Main character first name:", main_character_first_name)
    try:
        main_character_full_name = first_names_dict[main_character_first_name]
        print("Main character full name:", set(main_character_full_name))
    except:
        print("Standard full name for main character could not be retrieved")

    actual_names = []
    for potential_first_or_last_name in smallest_chunks_ordered_cut_off:
        try:
            potential_actual_names = first_names_dict[potential_first_or_last_name]
            # Sorts the options by popularity and extracts the most popular
            best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
            actual_names.append(best_pick_actual_name)
        except KeyError:
            try:
                potential_actual_names = last_names_dict[potential_first_or_last_name]
                # Sorts the options by popularity and extracts the most popular
                best_pick_actual_name = useful_functions.list_counter_rearrange(potential_actual_names)[0][0]
                actual_names.append(best_pick_actual_name)
            except KeyError:
                actual_names.append(None)
                print(f"Full name couldn't be retrieved for {potential_first_or_last_name}")
    print("Actual names:", actual_names)

    removable_actual_names = []
    for actual_name in actual_names:
        for three in chunks[-3]:
            print()
            if re.search(actual_name, three):
                removable_actual_names.append(actual_name)
    print("Removable actual names:", removable_actual_names)

    actual_names = [actual_name for actual_name in actual_names if actual_name not in removable_actual_names]
    print("Actual names again:", actual_names)