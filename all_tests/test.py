a = "aabcccd"

char_freq_map = {}

for ch in a:
    if ch not in char_freq_map:
        char_freq_map[ch] = 1
    else:
        char_freq_map[ch] += 1

print("frequencies of all character", char_freq_map)

for key,value in char_freq_map.items():
    if value<=2:
        print(key, sep=",")
