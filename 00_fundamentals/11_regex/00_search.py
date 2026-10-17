import re

pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net)"
email = "test@test.com"

result = re.search(pattern, email)
print(result)

not_email = "test@test"
result = re.search(pattern, not_email)
print(result)
