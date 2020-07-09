# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

from collections import defaultdict

# Setting default_factory to int creates a count of each letter
cache = defaultdict(int)

# Use Open() to read ciphertext.txt file
f = open("ciphertext.txt", "r")
txt = f.read()

# # create a decoded table using v:k from encode_table
# decode_table = { v:k for k,v in encode_table.items()}

# def decode(s):
#   decoded = ""
  
#   # TODO - use frequency analysis to find key then decode key

#   for c in s:
#     if c in decode_table.keys():
#       decoded += decode_table[c]
#     else: 
#       decoded += c

#   print(decoded)

for c in txt:
    if c.isupper():
        cache[c] += 1

freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

freq = [item[0] for item in sorted(cache.items(), key=lambda x: x[1], reverse=True)]

lookup = {cipher: plain for cipher, plain in zip(freq, freq_list)}

print(txt.translate(str.maketrans(lookup)))

# # call decode with ciphertext
# decode(txt)

# close file when done
f.close()