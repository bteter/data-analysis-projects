proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

delimiters = [',', ';', ' ']

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

# print(',' in proto_list1)
    

    
        
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

# new_proto_list1 = proto_list1.split(',')
# print(new_proto_list1)

# new_proto_list1_reverse = new_proto_list1.reverse()
# print(proto_list1)

# new_csv = ','
# new_csv = ','.join(new_proto_list1)
# print(new_csv)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
# proto_list2 = proto_list2.split(';')
# print(proto_list2)

# new_proto_list2 = sorted(proto_list2)
# print(new_proto_list2)

# proto_list2_comma = ','
# proto_list2_comma = ','.join(new_proto_list2)
# print(proto_list2_comma)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

#proto_list3 = "space delimited string"


# proto_list3 = proto_list3.split(' ')
# print(proto_list3)

# new_proto_list3 = sorted(proto_list3, reverse = True)
# print(new_proto_list3)

# new_proto_list3 = ' '.join(new_proto_list3)
# print(new_proto_list3)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
# proto_list4 = "Comma-spaces, might, require, typing, caution"

