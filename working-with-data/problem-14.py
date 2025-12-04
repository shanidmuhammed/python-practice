# Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.

def unique(values, key):
    seen = set()
    for v in values:
        val = key(v)
        if (val) not in seen:
            seen.add(val)
    return seen

print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))