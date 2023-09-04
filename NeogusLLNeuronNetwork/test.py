# Rozdziel ciąg znaków na podstawie przecinka i przekształć w liczby całkowite
ciag_znakow = "5, 10"
elementy = ciag_znakow.split(",")  # Rozdziel na podstawie przecinka
lista = [int(element) for element in elementy]

# Wyświetl wynik
print(lista)