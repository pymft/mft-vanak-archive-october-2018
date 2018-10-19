from poem import wasteland

# 1. print a list of unique words used in wasteland

def wasteland(word):
    wasteland1 = []
    wasteland1.append(word[0])
    for i in range (len(word)):
        for j in range (len(wasteland1)):
            if word[i]==word[j]:
                pass
            else:
                wasteland1.append(word[i])
                print(wasteland1[j])
    print(wasteland1)
    return wasteland1

# 2. print a dictionary of words and their occurrences in text
#    key would be the word itself and value (an integer) is the number of repeats

# 3. 10 words most repeated

# 4. top 10 five-or-more-character-length words most repeated

