VOWELS = ['a',"e","i","o","u"]

def main():
    inp = input("Enter your word: ")
    print(shorten(inp))

def shorten(text):
    for vowel in VOWELS:
        text = text.replace(vowel, "").replace(vowel.upper(), "")
    return text

if __name__ == "__main__":
    main()