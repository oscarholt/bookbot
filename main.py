def main():
    path = "./books/frankenstein.txt"
    contents = get_contents(path)
    words = word_count(contents)
    characters = count_characters(contents)
    print_report(path, words, characters)
    return 0

def get_contents(path):
    with open(path) as file:
        return file.read()

def word_count(contents):
    word_list = contents.split()
    return len(word_list)

def count_characters(contents):
    characters = {}
    contents = contents.lower()

    for character in contents:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters 

def print_report(path, words, characters):
    print(f"--- Being report of {path} ---")
    print(f"{words} words found in the document")
    print("\n")
    character_list = []
    for character in characters:
        character_dict = {}
        character_dict["character"] = character
        character_dict["count"] = characters[character]
        character_list.append(character_dict)

    character_list.sort(reverse=True, key=sort_on)
    for char in character_list:
        if char["character"].isalpha():
            character = char["character"]
            count = char["count"]
            print(f"The '{character}' character was found {count} times")
    print(f"---End report---")

def sort_on(dict):
    return dict["count"]

main()
