stire = "În contextul comparativ, chiar dacă este vorba de o performanţă uşor mai bună decât creşterea de 4,5% aşteptată de analişti, totuşi este mai puţin decât avansul de 4,7% înregistrat în trimestrul al doilea al acestui an. Şi mai important, aceasta cea mai slabă performanţă economică înregistrată de la începutul lui 2023, când China tocmai pusese capăt politicii sanitare ‘zero Covid’ care a paralizat deplasările şi consumul, ceea ce a afectat şi activitatea economică."
stire_1 = (stire[0:234:])
stire_2 = (stire[234::-1])
stire_1 = (stire_1.upper())
stire_1 = stire_1.strip()
stire_2 = stire_2.translate(str.maketrans("", "", ".,!"))
stire = stire_1 + stire_2
print(stire)



