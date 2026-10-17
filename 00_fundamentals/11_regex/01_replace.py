import re

pattern = r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3"

number = "013-768-3345"
new_number = re.sub(pattern, new_pattern, number)
print(new_number)