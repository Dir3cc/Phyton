meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/sinirlenmek",
            }

print("Selamlar, sistemdeki kelimeler şunlar:",meme_dict.keys())
word = input("Bilmediğiniz bir kelimeyi yazın (hepsini büyük harflerle yazın!):")

if word in meme_dict.keys():
    print("Anlamı:", meme_dict[word])
else:
    print("Tekrar deneyin")

def ekleme():
    print("Eklemek istediğiniz bir kelimeyi yazın")

ekleme()
