a_dictionary = dict()
a_dictionary = {"name": "sam","value": 100}

print a_dictionary["name"]

a_dictionary["favorite_number"] = list()
a_dictionary["favorite_number"].append(5)
a_dictionary["favorite_number"].append(9)

print a_dictionary
print a_dictionary["favorite_number"][1]

print a_dictionary.keys()
print dir(a_dictionary)

print "name" in a_dictionary
