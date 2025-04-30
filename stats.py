def get_num_words(input_text): 
    num_words = input_text.split()
    return num_words

def get_num_char(input_text):
    count_characters = { }

    for char in input_text.lower():
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1

    return count_characters

def get_sorted_dictionary(dict_char): 

    # Filter out non-alphabetic keys
    alpha_dict = {k: v for k, v in dict_char.items() if isinstance(k, str) and k.isalpha()}
    
    # Sort the filtered dictionary by values in descending order
    sorted_dict = dict(sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_dict
