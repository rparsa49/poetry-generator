import nltk
# nltk.download()
import pronouncing
import random


my_corpus = []
for fid in nltk.corpus.shakespeare.fileids():
    my_corpus += nltk.corpus.shakespeare.words(fid)

bigrams = nltk.bigrams(my_corpus)
cfd = nltk.ConditionalFreqDist(bigrams)


def random_word_generator(source = None, num = 1):
    result = []
    while source == None or not source.isalpha():
        source = random.choice(my_corpus)

    word = source
    result.append(word)
    while len(result) < num:
        if word in cfd:
            init_list = list(cfd[word].keys())
            choice_list = [x for x in init_list if x.isalpha()]
            if len(choice_list) > 0:
                newword = random.choice(choice_list)
                result.append(newword)
                word = newword
            else:
                word = None
                newword = None
        else:
            newword = None
            while newword == None or not newword[0].isalpha():
                newword = random.choice(my_corpus)
            result.append(newword)
            word = newword
    return result


def count_syllables(word):
    phones = pronouncing.phones_for_word(word)
    count_list = [pronouncing.syllable_count(x) for x in phones]
    if len(count_list) > 0:
        result = max(count_list)
    else:
        result = 0
    return result


def get_rhymes(word):
    result = pronouncing.rhymes(word)
    return result


def get_stresses(word):
    result = pronouncing.stresses_for_word(word)
    return result


def test():
    keep_going = True
    while keep_going:
        word = input("Please enter a word (Enter '0' to quit): ")
        if word == '0':
            keep_going = False
        elif word == "":
            pass
        else:
            print(cfd[word].keys())
            print(cfd[word].values())
            print()
            print("Random 5 words following", word)
            print(random_word_generator(word, 5))
            print()
            print("Pronunciations of", word)
            print(pronouncing.phones_for_word(word))
            print()
            print("Syllables in", word)
            print(count_syllables(word))
            print()
            print("Rhymes for", word)
            print(get_rhymes(word))
            print()
            print("Stresses for", word)
            print(get_stresses(word))
            print()


def stress_test():
    for i in range(10000):
        wl = random_word_generator(None, 10)
        print(wl)

    wl = random_word_generator(None, 10000)
    for w in wl:
        sc = count_syllables(w)
        print(w, sc)

    wl = random_word_generator(None, 10000)
    for w in wl:
        rs = get_rhymes(w)
        print(w, len(rs))
        print(rs)

    wl = random_word_generator(None, 10000)
    for w in wl:
        stl = get_stresses(w)
        print(w, len(stl))
        print(stl)




def generate_rhyming_lines():
    word_list_1 = random_word_generator(None, 5)
    word_list_2 = random_word_generator(None, 5)
    rhymes = get_rhymes(word_list_1[4])

    if rhymes:
        word_list_2[4] = random.choice(rhymes)

    line1 = ""
    line2 = ""

    for i in line1:
        line1 += i + " "
    for i in word_list_2:
        line2 += i + " "

    rhyming_lines = [line1, line2]
    return rhyming_lines


def generate_10_syllable_lines():
    words1 = []
    syl_count = 0
    while syl_count != 10:
        temp = random_word_generator(None, 1)[0]
        if count_syllables(temp) + syl_count <= 10:
            syl_count += count_syllables(temp)
            words1.append
    words2 = []
    syl_count = 0
    while syl_count != 10:
        temp = random_word_generator(None, 1)[0]
        if count_syllables(temp) + syl_count <= 10:
            syl_count += count_syllables(temp)
            words2.append

    string1 = ""
    string2 = ""

    for i in words1:
        string1 += i + " "
    for i in words2:
        string2 += i + " "

    ten_syllables = [string1, string2]
    return ten_syllables

def generate_line(last_word, status):
    line = []
    syl_count = 0
    while syl_count != 5:
        temp = random_word_generator(None, 1)[0]
        if count_syllables(temp) + syl_count <= 5:
            syl_count += count_syllables(temp)
            line.append(temp)
    if last_word and status:
        rhymes = get_rhymes(last_word)
        if rhymes:
            while True:
                x = random.choice(rhymes)
                if count_syllables(x) == count_syllables(line[-1]):
                    line[-1] = x
                    break
    return line


def generate_poem():
    poem = []
    status = True
    line = generate_line(None,status)
    result = " "
    for i in line:
        result += i + " "
    poem.append(result)
    for i in range(6):
        line = generate_line(line[-1],status)
        result = " "
        for i in line:
            result += i + " "
        poem.append(result)
        status = not status
    result = ""
    for i in poem:
        result += "\n" + i
    return result


if __name__ == "__main__":
##    test()
##    stress_test()
##    print()
    
#    result1 = generate_rhyming_lines()
#    print("RHYMING LINES:")
#    print(result1)
#    print()

#    result2 = generate_10_syllable_lines()
#    print("10 SYLllABLE LINES:")
#    print(result2)
#    print()
   
    my_poem = generate_poem()
    print("A POEM:")
    print(my_poem)

