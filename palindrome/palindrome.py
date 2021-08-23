def main():
    word = input("Please give me a word: ").lower().strip()
    length = len(word)
    reverseList = []

    while length > 0:
        reverseList.append(word[length-1])
        length = length-1
    reverseWord = "".join(reverseList)

    print("~" * 10)

    if word == reverseWord:
        print("Palindrome!")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()