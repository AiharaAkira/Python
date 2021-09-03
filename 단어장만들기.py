with open("vocabulary.txt", "w", encoding="UTF-8") as f:
    while True:
        word_english = input('영어 단어를 입력하세요:')
        if word_english == 'q':
            break
        word_korean = input("한국어 뜻을 입력하세요:")
        if word_korean == 'q':
            break
        f.write("{}: {}".format(word_english, word_korean))


