wina_vocab =    {
    "sng": "Sit & Go",
    "tt": "Tournoi",
    "turbo": "Turbo",
    "semiturbo": "Semi-Turbo"
}

def vocab(word):
    if word in wina_vocab: return wina_vocab[word]
    else : return word
