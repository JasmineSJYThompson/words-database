def list_counter_rearrange(long_list):
    count_dict = {item: {"count": 0} for item in long_list}
    for item in long_list:
        count_dict[item]["count"] += 1
    out_longs = list(count_dict.keys())
    out_counts = list(temp_dict["count"] for temp_dict in count_dict.values())

    count_sorted_out_counts, count_sorted_out_longs = zip(*sorted(zip(out_counts, out_longs)))
    count_sorted_out_counts = list(count_sorted_out_counts)
    count_sorted_out_longs = list(count_sorted_out_longs)
    count_sorted_out_counts.reverse()
    count_sorted_out_longs.reverse()

    return count_sorted_out_longs, count_sorted_out_counts

def cut_off_list_before_cut_off(long_list, long_list_counter_descending, cut_off):
    if cut_off >= max(long_list_counter_descending):
        return []
    actual_cut_off = min([number for number in long_list_counter_descending if number >= cut_off])
    return long_list[:long_list_counter_descending.index(actual_cut_off)]

if __name__ == "__main__":
    long_list = ["cat", "dog", "chicken", "horse", "pig", "canary", "swan", "horse", "kitten"]
    counter_list = [12, 10, 3, 3, 3, 3, 2, 2, 1]
    print(counter_list[:counter_list.index(2)])

    print(cut_off_list_before_cut_off(long_list, counter_list, 2))

    print([f"{animal1} {animal2}" for animal1 in long_list for animal2 in long_list])