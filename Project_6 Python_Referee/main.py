import re

# comments here
# comments here
# comments here
# comments here

punctuations = r"[-1234567890,.;:_?!@#$%^&*()/|{}]"

f1 = open("test_1.txt", "r")
book_1 = f1.read()
bk_1_lw = book_1.lower()
bk_1_re = re.sub(punctuations, "", bk_1_lw)
bk_1 = bk_1_re.split()
bk_1 = set(bk_1)  # change type to set for removing duplicates

print(bk_1)

f2 = open("test_2.txt", "r")
book_2 = f2.read()
bk_2_lw = book_2.lower()
bk_2_re = re.sub(punctuations, "", bk_2_lw)
bk_2 = bk_2_re.split()
bk_2 = set(bk_2)  # remove duplicates

print(bk_2)

print(f"Common unique words: {len(bk_1 | bk_2)}")
# which is unique first and unique in second ==> გაერთიანება

print(f"Common words: {len(bk_1 & bk_2)}")
# which is in first and also second  ==> თანაკვეთა

print(bk_1 - bk_2, '-', len(bk_1 - bk_2))  # include in first and not in second
print(bk_2 - bk_1, '-', len(bk_2 - bk_1))  # include in second and not in first

f1.close()
f2.close()
