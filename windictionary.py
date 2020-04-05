wina_vocab =    {
    "sng": "Sit & Go",
    "tt": "Tournoi",
    "turbo": "Turbo",
    "semiturbo": "Semi-Turbo",
    "community": "Commuautaire",
    "doubleornothing": "Double or Nothing",
    "normal": "Normal",
    "sitngo": "Sit & Go"
}

def vocab(word):
    if word in wina_vocab: return wina_vocab[word]
    else : return word
