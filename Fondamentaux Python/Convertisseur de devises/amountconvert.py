# 💡 Petit projet : Convertisseur de devises (Dirhams => Euros)
# L'utilisateur entre un montant en dirhams et un taux de conversion,
# le programme affiche le montant converti en euros.

# Demande à l'utilisateur d'entrer le montant en dirhams (DH)
amount = float(input("Enter the amount in DH: \n"))
# Demande le taux de conversion (ex: 0.091 si 1 DH = 0.091 €)
rate = float(input("Enter the conversion rate to Euro : \n"))
# Affiche les valeurs saisies
print(f"the amount is,{amount}!")
# Fonction de conversion
print(f"the the conversion rate is,{rate}!")
# Affiche le montant converti en euros
def convert(amount,rate):
    euroamount= amount * rate
    return euroamount
print(f"the amount converted is: {convert(amount,rate)}")