"""
name_count_dict = {name: {"count": 0} for name in total_names}

for year in range(1880, 2023+1):
    with open(f"./names/yob{year}.txt", "r") as readfile:
        lines = readfile.read().split("\n")

    for line in lines:
        try:
            split_line = line.split(",")
            name = split_line[0]
            count = split_line[2]
            name_count_dict[name]["count"] += int(count)
        except IndexError:
            pass

out_names = list(name_count_dict.keys())
out_counts = list(temp_dict["count"] for temp_dict in name_count_dict.values())

print(out_names[0:10], out_counts[0:10])
print(out_names[-10::], out_counts[-10::])

count_sorted_out_counts, count_sorted_out_names = zip(*sorted(zip(out_counts, out_names)))
count_sorted_out_counts = list(count_sorted_out_counts)
count_sorted_out_names = list(count_sorted_out_names)
count_sorted_out_counts.reverse()
count_sorted_out_names.reverse()
"""

if __name__ == "__main__":
    animal_list = ["dog", "cat", "cat", "cat", "dog", "duck", "kitten", "cat"]
    count_dict = {animal: {"count": 0} for animal in animal_list}
    for animal in animal_list:
        count_dict[animal]["count"] += 1
    out_animals = list(count_dict.keys())
    out_counts = list(temp_dict["count"] for temp_dict in count_dict.values())

    count_sorted_out_counts, count_sorted_out_animals = zip(*sorted(zip(out_counts, out_animals)))
    count_sorted_out_counts = list(count_sorted_out_counts)
    count_sorted_out_animals = list(count_sorted_out_animals)
    count_sorted_out_counts.reverse()
    count_sorted_out_animals.reverse()

    print(count_sorted_out_animals, count_sorted_out_counts)


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