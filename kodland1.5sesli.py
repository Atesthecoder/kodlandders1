word = input("bir kelime söyle")
sh = "aeiuüıoöAEİUÜIOÖ"
sayac = 0
uyi = 0
for i in word:
    if i in sh:
        
        uyi = uyi + 1
print(uyi," kadar sesli harf var")