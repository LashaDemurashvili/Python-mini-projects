import re

# comments here
# comments here
# comments here
# comments here


# global variables here
punctuations = r"[-1234567890,.;:_?!@#$%^&*()/|{}]"
book_1_name = "Hamlet"
book_2_name = "Othello"
# global variables here


f1 = open("hamlet.txt", "r")
book_1 = f1.read()
bk_1_lw = book_1.lower().strip()
bk_1_re = re.sub(punctuations, "", bk_1_lw)
bk_1 = bk_1_re.split()
bk_1 = set(bk_1)  # change type to set for removing duplicates
print("Total length of unique words in Hamlet:", len(bk_1))

f2 = open("othello.txt", "r")
book_2 = f2.read()
bk_2_lw = book_2.lower()
bk_2_re = re.sub(punctuations, "", bk_2_lw)
bk_2 = bk_2_re.split()
bk_2 = set(bk_2)  # remove duplicates
print("Total length of unique words in Othello:", len(bk_2))

# # test
# print(bk_1)
# print(bk_2)

print(f"Common unique words: {len(bk_1 | bk_2)}")  # საერთო უნიკალური სიტყვები
# which is unique first and unique in second ==> გაერთიანება

print(f"Common words: {len(bk_1 & bk_2)}")
# which is in first and also second  ==> თანაკვეთა ანუ საერთო სიტყვები

print(f"Words which is in {book_1_name} and not in {book_2_name}:", len(bk_1 - bk_2))  # include in bk_1 and not in bk_2
print(f"Words which is in {book_2_name} and not in {book_1_name}:", len(bk_2 - bk_1))  # include in bk_2 and not in bk_1
print("Symmetrical difference:",
      len(bk_1 ^ bk_2))  # the set of elements that are in either set, but not in the intersection

f1.close()
f2.close()
