def sort_alphabetical(text):

    sorted_chars = sorted(text)
    sorted_text = ''.join(sorted_chars)

    return sorted_text

text = "abhdbvhsdbckjab"
sorted_text = sort_alphabetical(text)
print(sorted_text)