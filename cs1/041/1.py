for c in 'iniad':
    print(c)

def abbrev(lists):
    kashiramoji = ''
    for s in lists:
        kashiramoji += s[0]

    return kashiramoji

print(abbrev(['Nippon', 'Housou', 'Kyoukai']))
print(abbrev(['British', 'Broadcasting', 'Company']))

