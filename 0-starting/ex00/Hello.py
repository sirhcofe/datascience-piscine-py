ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# lists are ordered and mutable collections of elements, which supports
# addition, removal, and modification of elements in a list.
ft_list[1] = "World!"

# tuples are used to create multiple elements in a single variable tuple object does not support item assignment, as tuple is immutable, hence it
# is necessary to convert it into list before changing the elements.
temp_list = list(ft_tuple)
temp_list[1] = "Malaysia!"
ft_tuple = tuple(temp_list)

# sets are collections of unique elements which are not ordered, and they
# automatically remove duplicate values.
ft_set.remove("tutu!")
ft_set.add("Kuala Lumpur!")

# dictionary are collections of key-value pairs, whereby each key should be
# unique, and the values are accessed by their respective keys. Use update()
# method to update the dictionary with the elements from another dictionary.
campus_name = {"Hello" : "42KL!"}
ft_dict.update(campus_name)

# when to use:
# list - when working with collection of values that can change.
# tuple - when working with collection of values that remained unchanged, like
#         coordinates or constants, more efficient than list.
# set - used to store unique, unordered elements, in which its order is not
#       important, ideal for checking memebership (whether an element is in the
#       set) or removing duplicates from a list.
# dict - used when storing data in key-value pairs.

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
