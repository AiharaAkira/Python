with open("vocabulary.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        korean_word = data[0]
        english_word = data[1]

        answer = input("{}:".format(korean_word))

        if answer == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
