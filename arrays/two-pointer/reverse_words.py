def reverse_words_manual(text):
  final = ''
  left_pointer, right_pointer = 0, 0

  while right_pointer < len(text):
    # if the character in the 'right_pointer' position is different from an empty character
    # it continues until finds an empty character
    if text[right_pointer] != ' ':
      right_pointer += 1
    else:
      final += text[left_pointer:right_pointer][::-1] + ' '
      right_pointer += 1
      left_pointer = right_pointer

  final += text[left_pointer:right_pointer][::-1]
  return final

print(reverse_words_manual('Mr Ding'))
print(reverse_words_manual('Let\'s take LeetCode contest'))
