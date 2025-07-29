string = "aabcddd"
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print each character with its count
for char, count in char_count.items():
    print(f"'{char}' occurs {count} time(s)")
    