import json


json_string = '''{
  "first_name": "John",
  "last_name": "Smith",
  "is_alive": true,
  "age": 27,
  "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [
    "Catherine",
    "Thomas",
    "Trevor"
  ],
  "spouse": null
}'''

print("-------- json to dict --------")
data = json.loads(json_string)
print(data)
print(type(data))


print("---------- read .json file ----------")
with open("./files/test.json") as file:
    data2 = json.load(file)
    print(type(data2))
    print(data2)

    print("--------- loop over dict/json -------")
    for key, value in data2.items():
        print(key, value)

print ("---------- dump json to file -------")
print ("-")
with open("./files/test2.json", "w") as file:
    json.dump(data, file, indent=4, sort_keys=True)

print( "-------- delete json--------")
with open("./files/test2.json", "r") as file:
    del data["first_name"]
    print(data)