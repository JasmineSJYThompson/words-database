total_names = []

for year in range(1880, 2023+1):
    with open(f"./names/yob{year}.txt", "r") as readfile:
        lines = readfile.read().split("\n")

    for line in lines:
        name = line.split(",")[0]
        total_names.append(name)

print(len(total_names))

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

"""
print(name_count_dict["Mercedes"])
print(name_count_dict["Jesus"])
print(name_count_dict["Clara"])
print(name_count_dict["Jasmine"])
print(name_count_dict["Samuel"])
print(name_count_dict["Melissa"])
print(name_count_dict["John"])
"""

out_names = list(name_count_dict.keys())
out_counts = list(temp_dict["count"] for temp_dict in name_count_dict.values())

print(out_names[0:10], out_counts[0:10])
print(out_names[-10::], out_counts[-10::])

count_sorted_out_counts, count_sorted_out_names = zip(*sorted(zip(out_counts, out_names)))
count_sorted_out_counts = list(count_sorted_out_counts)
count_sorted_out_names = list(count_sorted_out_names)
count_sorted_out_counts.reverse()
count_sorted_out_names.reverse()

print(count_sorted_out_names[0:10], count_sorted_out_counts[0:10])
print(count_sorted_out_names[-10::], count_sorted_out_counts[-10::])

# Please note that we exclude any empty string names when writing to the file
out_lines = [f"{count_sorted_out_names[i]},{count_sorted_out_counts[i]}"
             for i in range(len(count_sorted_out_names))
             if count_sorted_out_names[i] != ""]

out_text = "\n".join(out_lines)

with open(f"../all_names_count.txt", "w") as writefile:
    writefile.write(out_text)