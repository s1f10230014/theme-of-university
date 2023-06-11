def abbrev(words):
    result = ''
    for w in words:
        result += w[0]
    return result

print(abbrev(['Nippon', 'Housou', 'Kyoukai']))
print(abbrev(['British', 'Broadcasting', 'Company']))