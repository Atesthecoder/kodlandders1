bruh_words = {
    
    "CRINGE": "Garip ya da utandırıcı bir şey",
            
    "LOL": "Komik bir şeye verilen cevap",

    "FREAKY":"aykırı,çılgınca"
}
word = input("anlamadığın kelime yaz?")
word = word.upper()
if word in bruh_words:
    print(bruh_words[word])