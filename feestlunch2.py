aantalCroissantjes = int(input('geef aantal croissantjes: '))
prijsCroissantjes = float(input('geef de prijs van de croissantjes: '))
aantalStokbroden = int(input('geef aantal van de stokbroden: '))
prijsStokbroden = float(input('geef prijs van de stokbroden: '))
aantalKortingsbonnen = int(input('geef aantal kortingsbonnn: '))
prijsKortingsbonnen = float(input('geef prijs kortingsbonnen: '))

totaalPrijs = ((aantalCroissantjes * prijsCroissantjes) + (aantalStokbroden * prijsStokbroden) - (aantalKortingsbonnen * prijsKortingsbonnen))
print('-------------------------------------------------------------------------------------------------------------------------------------------------')
print('De feestlunch kost je bij de bakker: ' + str (totaalPrijs) + 'voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
print('-------------------------------------------------------------------------------------------------------------------------------------------------')