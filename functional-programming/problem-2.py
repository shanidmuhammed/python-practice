# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(my_dict, prev=None, result=None):
    if result is None:
        result = {}
    for k, v in my_dict.items():
        next_key = f"{prev}.{k}" if prev else k
        if isinstance(v, dict):
            flatten_dict(v, next_key, result)
        else:
            result[next_key] = v
    return result

print(flatten_dict({'a': {'p': {'q': 5}}}))