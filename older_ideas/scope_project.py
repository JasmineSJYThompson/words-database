# choice one: unique words (sets of 2 are acceptable)
# choice two: proper nouns only
# choice three: only interested in a top 10
# choice four: must be flexible to shorten this list based on strength of association

with open("dadoes.txt", "r", encoding="utf-8") as readfile:
    text = readfile.read()

words = text.split(" ")

def is_proper(word):
    if word.isalpha() and word[0].isupper() and word[1::].islower():
        return True
    else:
        return False

def is_proper_pair(word_pair):
    if is_proper(word_pair[0]) and is_proper(word_pair[1]):
        return True
    else:
        return False

def is_proper_triplet(word_triplet):
    if is_proper(word_triplet[0]) and is_proper(word_triplet[1]) and is_proper(word_triplet[2]):
        return True
    else:
        return False

def is_proper_set(word_set, word_set_length):
    check_set = [is_proper(word) for word in word_set]
    if check_set.contains(False):
        return False
    return True

proper_words = [word for word in words if is_proper(word)]

print(proper_words)

word_pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
proper_word_pairs = [pair for pair in word_pairs if is_proper_pair(pair)]

print(proper_word_pairs)

word_triplets = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]
proper_word_triplets = [triplet for triplet in word_triplets if is_proper_triplet(triplet)]

print(proper_word_triplets)

gen_number = 3
word_triplets = [[words[i+j] for j in range(gen_number)] for i in range(len(words)-gen_number+1)]

def get_word_chunks(chunk_size, words):
    return [[words[i+j] for j in range(chunk_size)] for i in range(len(words)-chunk_size+1)]

def is_proper_chunk(word_chunks):
    return [all([is_proper(word) for word in word_chunk]) for word_chunk in word_chunks]

print(is_proper_chunk(get_word_chunks(1, words)))

print(len(words))
print(len(is_proper_chunk(get_word_chunks(5, words))))

import time

start = time.time()
number_proper_chunks = 1
chunk_size = 1
chunks_sizes_valid = []
while number_proper_chunks != 0:
    temp_number_proper_chunks = sum(is_proper_chunk(get_word_chunks(chunk_size, words)))
    if temp_number_proper_chunks != 0:
        chunks_sizes_valid.append(chunk_size)
    chunk_size+=1
    number_proper_chunks = temp_number_proper_chunks
print("chunk sizes valid", chunks_sizes_valid)
end = time.time()
print(end - start)

start = time.time()
number_proper_chunks = []
for word_chunk_size in range(10):
    number_proper_chunks.append(sum(is_proper_chunk(get_word_chunks(word_chunk_size, words))))
print(number_proper_chunks)
end = time.time()
print(end - start)

def is_proper(word):
    if word.isalpha() and word[0].isupper() and word[1::].islower():
        return True
    else:
        return False

def get_word_chunks(chunk_size, words):
    return [[words[i+j] for j in range(chunk_size)] for i in range(len(words)-chunk_size+1)]

def is_proper_chunk(word_chunks):
    return [all([is_proper(word) for word in word_chunk]) for word_chunk in word_chunks]

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

print("cutoff")
print("top chunk size", get_top_chunk_size(text))