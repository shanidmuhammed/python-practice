# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(my_dict, result=None):
    if result == None:
        result = {}
    if my_dict:
        for k, v in my_dict.items():
            if isinstance(v, dict):
                flatten_dict(v, result)
            else:
                result[k] = v
        return result

print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))