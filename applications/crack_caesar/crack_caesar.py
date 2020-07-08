# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Use Open() to read ciphertext.txt file
f = open("ciphertext.txt", "r")
# print(f.read())
# uncomment when encode and decode work 
# s = f.read()
txt = f.read(25)
# remove whitespaces 
print(txt)

encode_table = {
  'A': 'H',
  'B': 'Z',
  'C': 'Y',
  'D': 'W',
  'E': 'O',
  'F': 'R',
  'G': 'J',
  'H': 'D',
  'I': 'P',
  'J': 'T',
  'K': 'I',
  'L': 'G',
  'M': 'L',
  'N': 'C',
  'O': 'E',
  'P': 'X',
  'Q': 'K',
  'R': 'U',
  'S': 'N',
  'T': 'F',
  'U': 'A',
  'V': 'M',
  'W': 'B',
  'X': 'Q',
  'Y': 'V',
  'Z': 'S'
}

# create a decoded table using v:k from encode_table
decode_table = { v:k for k,v in encode_table.items()}

def decode(s):
  decoded = ""

  for c in s:
    if c == " ":
      decoded += " "
    else: 
      decoded += decode_table[c]

  # return decoded string 
  return decoded

# call decode with ciphertext
decode(txt)

# close file when done
f.close()