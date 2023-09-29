import xml.etree.ElementTree as ET

# Multiple child tags

input = '''<stuff>
  <users>
   <user x= "2">
     <id>001</id>
     <name>Chuck</name>
   </user>
   <user x="7">
   <id>009</id>
   <name>Lupiya</name>
   </user>
  </users>
 </stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print("User count: ", len(lst))
for tag in lst:
    print("Name: ", item.find("name").text)
    print("Id: ", item.find("id").text)
    print("Attr: ", item.get("x"))
