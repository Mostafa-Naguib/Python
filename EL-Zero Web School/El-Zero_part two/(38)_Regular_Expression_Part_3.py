import re

a_web = re.search(r"(https?)\://(www)?\.?(\w+)\.(com|org|edu)(.+)?", "https://www.xq55.com")

print(a_web)
print(a_web.group())

print(f"Protocol: {a_web.group(1)}")
print(f"Sub Domain: {a_web.group(2)}")
print(f"Domain Name: {a_web.group(3)}")
print(f"Top Level Domain: {a_web.group(4)}")
