from phone import Phone


obj = Phone("Asus", "ROG 6 pro", 6.7, "Snapdragon 8+ Gen 1")


print(f"object class name: {obj.__class__}")
print(f"object class documentation: {obj.__doc__}")
print(f"object properties and values: {obj.__dict__}")
print(f"object module name: {obj.__module__}")

print("#" * 50)

print(f"object size in byte: {obj.__sizeof__()}")
print(f"object representation: {obj.__repr__()}")
print(f"object string representation: {obj.__str__()}")
