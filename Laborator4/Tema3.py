# 1.Write a function that receives as parameters two lists a and b and returns
# a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def sets_list_operations(a,b):
    list = []
    list.append(set(a)&set(b))
    list.append(set(a)|set(b))
    list.append(set(a)-set(b))
    list.append(set(b)-set(a))
    return list
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("Ex1:",sets_list_operations(a,b))

# 2. Write a function that receives a string as a parameter and returns a dictionary in
# which the keys are the characters in the character string and the values are the number
# of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the
# dictionary: {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

def letter_count(s):
    dictionary = dict()
    for c in s:
        if c not in dictionary.keys():
            dictionary[c]=1
        else:
            dictionary[c]+=1
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print("Ex2:",letter_count("Ana has apples."))

# 3. Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other
#   containers, such as dictionaries, lists, sets, etc.)

def compare_2_dictionaries(d1, d2):
    if set(d1.keys()) != set(d2.keys()):
        return False

    for key in d1:
        if isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if not compare_2_dictionaries(d1[key], d2[key]):
                return False
        else:
            if d1[key] != d2[key]:
                return False
    return True
d1 = {"A":1 ,"B":2 ,"C":3}
d2 = {"A":1 ,"B":2 ,"C":3}
d3 = {"A":1 ,"B":2 ,"D":4}
print("Ex3:",compare_2_dictionaries(d1,d3))

# 4. The build_xml_element function receives the following parameters: tag, content,
# and key-value elements given as name-parameters. Build and return a string that represents
# the corresponding XML element. Example: build_xml_element 
# ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
# returns  the string = "<a href=\"http://python.org \ "_class = 
# \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, **attributes):
    # Start building the XML element with the tag
    xml_element = f"<{tag}"

    # Add attributes to the element
    for key, value in attributes.items():
        xml_element += f' {key}=\ "{value}"\ '

    # Add the content to the element and close the tag
    xml_element += f">{content}</{tag}>"

    return xml_element

xml_string = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print("Ex4:",xml_string)

# 5.The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) 
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not (value.startswith(prefix) and middle in value and value.endswith(suffix)):
                return False
    return True

# Example usage:
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {
    "key1": "come inside, it's too cold out",
    "key2": "start the winter",
    "key3": "this is not valid"
}
print("Ex5:",validate_dict(rules, data))

# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the number 
# of duplicate elements in the list (use sets to achieve this objective).

def uniques_and_duplicates(l):
    a = set()
    b = set()
    for i in l:
        if i in a:
            b.add(i)
        else:
            a.add(i)
    a=a-b
    return (a,b)
print("Ex6:",uniques_and_duplicates([1,2,2,3,4,5,5,6,7,8,8]))

# 7. Write a function that receives a variable number of sets and returns a dictionary
# with the following operations from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets, and op is 
# the applied operator: |, &, -. 

def dict_with_operations(a,b):
    dictionary = {}
    dictionary[f"{a}&{b}:"]=set(a)&set(b)
    dictionary[f"{a}|{b}:"]=set(a)|set(b)
    dictionary[f"{a}-{b}:"]=set(a)-set(b)
    dictionary[f"{b}-{a}:"]=set(b)-set(a)
    return dictionary

print("Ex7:",dict_with_operations({1,2},{2,3}))

# 8. Write a function that receives a single dict parameter named mapping. This dictionary
# always contains a string key "start". Starting with the value of this key you must obtain 
# a list of objects by iterating over mapping in the following way: the value of the current
# key is the key for the next value, until you find a loop (a key that was visited before). 
# The function must return the list of objects obtained as previously described.

def dict_loop(mapping):
    visited = set()
    result = []
    key = "start"
    while key not in visited:
        visited.add(key)
        if mapping[key] not in set(result):
            result.append(mapping[key])
        key = mapping[key]
    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print("Ex8:",dict_loop(mapping))

# 9. Write a function that receives a variable number of positional arguments and a
# variable number of keyword arguments adn will return the number of positional arguments
# whose values can be found among keyword arguments values.

def args_kwargs(*args,**kwargs):
    
    kw_values = set(kwargs.values())
    count = 0
    for a in args:
        if a in kw_values:
            count +=1
    return count
print("Ex9:",args_kwargs(1, 2, 3, 4, x=1, y=2, z=3, w=5))