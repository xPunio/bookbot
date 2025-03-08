def count_words(text):
    counter = 0
    splitted_text = text.split()
    for word in splitted_text:
        counter += 1

    return counter

def count_characters(text):
    characters = list(text.lower())
    result = {}
    for character in characters:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

def prepare_display_list(char_dict):
    result = []
    for key,value in char_dict.items():
        result.append({"char": key, "num": value})
    result.sort(reverse = True, key = sort_by)
    return result

def sort_by(d):
    return d["num"]
