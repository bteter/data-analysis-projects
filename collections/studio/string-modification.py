my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[0:3] #Lau
end_string = my_string[3:] #nchCode
# print(end_string + new_string) #nchCodeLau

# Use a template literal to print the original and modified string in a descriptive phrase.
output = "Original string reads: {} ends string reads: {} new_string reads: {}."
print(output.format(my_string, end_string, new_string))

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user_input = input('Select a number: ') # THIS IS A STRING - '3' not 3
selection = int(user_input) # THIS IS AN INTEGER '3' is now 3
altered_string = my_string[0:selection] # my_string[0:3] = Lau
new_string = my_string[selection:] + altered_string # new_string = nchCode, altered_string = Lau
# print(new_string) #nchCodeLau

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if selection >= len(my_string): # if the user input is greater than the length of "LaunchCode"
    firstThreeString = my_string[0:3] # my_string[0:3] = Lau - remove the first three characters
    newThreeString = my_string[3:] + firstThreeString # new_string = nchCode, altered_string = Lau - add them to the end

    print(newThreeString) #nchCodeLau
# else:
#     print(user_input + new_string) #expect to return number 