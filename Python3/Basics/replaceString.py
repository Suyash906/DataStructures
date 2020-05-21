# Replace only first occurence of the <search_char> in <input> by <replace_char>
def replaceFirstOccurenceString(input, search_char, replace_char):
    result = ''
    first_char_replaced = False
    for char in input:
        if not first_char_replaced and char == search_char:
            result += replace_char
            first_char_replaced = True
        else:
            result += char
    return result


# Replace all occurence of the <search_char> in <input> by <replace_char> 
def replaceString(input, search_char, replace_char):
    result = ''
    for char in input:
        if char == search_char:
            result += replace_char
        else:
            result += char
    return result

print('****************************************')
print('Replace All occurences of a single character')
print('****************************************')
input = "aaaaaabbbbbbb"
search_char = "a"
replace_char = "z"
print('Input String', input)
print('Search Char = ', search_char, " Replace char = ", replace_char)
result = replaceString(input, search_char, replace_char)
print('New String', result)

print('\n\n')
print('****************************************')
print('Replace Only first occurence a single character')
print('****************************************')
input = "aaaaaabbbbbbb"
search_char = "a"
replace_char = "z"
print('Input String', input)
print('Search Char = ', search_char, " Replace char = ", replace_char)
result = replaceFirstOccurenceString(input, search_char, replace_char)
print('New String', result)

print('****************************************')
