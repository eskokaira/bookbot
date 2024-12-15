def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    print()

    for item in chars_sorted_list:
        print(f"The'{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_num_words(inputString):
    return len(inputString.split())


def get_chars_dict(inputString):
    appereances = {}
    for char in inputString:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered in appereances:
                appereances[lowered] += 1
            else:
                appereances[lowered] = 1
    return appereances

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]





main()
