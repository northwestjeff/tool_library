import re

# list = ["555-8396 Neu, Allison",
#      "Burns, C. Montgomery",
#      "555-5299 Putz, Lionel",
#      "555-7334 Simpson, Homer Jay"]
#
# # x = re.search("Neu", list[0])0
#
# for i in list:
#     print(re.match('[0-9]+', i))

# test = "abz1 47"
# match = re.match('[\d\D]+', test).group()
# print("{} matches {}".format(match, test))

# test = "how-to-properly-give-your-dog-a-name"
# match = re.match('[\D]+', test).group()
# # print(match)
# print("{} matches {}".format(match, test))

test = "10395embislgm-potllz1.php"
print(re.match("[\w-]+[.][\w]+", test))


# Match entire string:
# 1. abz1 47
# 1. how-to-properly-give-your-dog-a-name
# 1. 10395embislgm-potllz1.php
#
# # Match both:
# 1. cat   or   dog
# 1. how-to-properly-give-your-dog-a-name   or   how-to-properly-give-your-dog-a-name/?name=samantha&phone=5552221212
#
# # Match left but not right:
# 1. why-do-some-websites-add-slugs-to-the-end-of-urls   not   Why-do-some-webSites-add-sluGs-to-the-end-of-urls
# 1. rapprochement   not   498080984
# 1. cruciverbalist   not   c r u c i v e r b a l i s t
#
# # Match once for each word:
# 1. how-to-properly-give-your-dog-a-name
# 1. that_one_regex_trick_that_developers_will_hate
#
# # Match each key and value after the question mark:
# 1. how-to-properly-give-your-dog-a-name/?name=samantha&phone=5552221212