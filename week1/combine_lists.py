def combine_and_sort(text1, text2):
    combined_text = text1 + text2
    odd_sorted = sorted([char for i, char in enumerate(combined_text) if i % 2 != 0])
    even_sorted = sorted([char for i, char in enumerate(combined_text) if i % 2 == 0])
    return odd_sorted, even_sorted

text1 = "adfhasd"
text2 = "sdfsdfsd"

odd_sorted, even_sorted = combine_and_sort(text1, text2)

print("Odd-indexed characters in sorted order:", odd_sorted)
print("Even-indexed characters in sorted order:", even_sorted)