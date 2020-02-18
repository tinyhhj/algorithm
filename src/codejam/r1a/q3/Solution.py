# stage 1 2<= n <= 6
# combination all try

def canMakePairs(words):
    pass


def combination(words, rhymes):
    if len(words) == 0 :
        return len(rhymes) * 2

    for i in range(len(words)):
        for j in range(i+1,len(words)):
            res = ""

    combination(words,rhymes)


    return len(rhymes)*2