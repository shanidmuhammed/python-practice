# Write a function unflatten_dict to do reverse of flatten_dict.

def unflatten_dict(my_dict):
    result = {}
    for k, v in my_dict.items():
        if '.' in k:
            keys = k.split('.')
            for key in keys:
                key[]
        else:
            result[k] = v
    return result