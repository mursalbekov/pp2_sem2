def isBalanced(final_str):
    type_brackets = ['()', '{}', '[]']
    while any(x in final_str for x in type_brackets):
        for br in type_brackets:
            final_str = final_str.replace(br, '')
    return not final_str


string = str(input())
print("Yes"
      if isBalanced(string) else "No")