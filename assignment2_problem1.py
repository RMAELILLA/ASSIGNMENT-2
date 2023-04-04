# pseudocode

# ask user for input, then save it
input_str = input("What is your input string? ")
output_str = ""
# check every character
for i in range(len(input_str)):
#   if a, change *
    if input_str[i] == "a":
        output_str += "*"
#   if e, change &
    elif input_str[i] == "e":
        output_str += "&"
#   if i, change #
    elif input_str[i] == "i":
        output_str += "#"
#   if o, change +
    elif input_str[i] == "o":
        output_str += "+"
#   if u, change !
    elif input_str[i] == "u":
        output_str += "!"
    else:
        output_str += input_str[i]
# print output
print(output_str)
