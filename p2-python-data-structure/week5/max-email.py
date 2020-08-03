# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.

name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dct = dict()
m_email = ""
m_count = 0

for line in handle:
    if line.startswith("From:"):
        pieces = line.split()
        email = pieces[1]
        dct[email] = dct.get(email, 0) + 1

for em in dct.keys():
    if m_email == "":
        m_email = em
        m_count = dct[em]
    if(dct[em] > m_count):
        m_email = em
        m_count = dct[em]

print(m_email, m_count)