# Convert a string to an array

def string_to_array(s):
    array = s.split()
    if not array:
        return ['']
    return array
