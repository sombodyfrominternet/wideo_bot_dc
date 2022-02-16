# Wideo bot na Discorda

# Opis
Bot na discorda przetwarzający film na klatki, a następnie klatki na wiadomości 

![test](https://img.shields.io/badge/Status-Wspierane-brightgreen?style=for-the-badge&logo=appveyor)
![jęzuk](https://img.shields.io/badge/J%C4%99zyk-Python-blue?style=for-the-badge&logo=appveyor)

# Wymagania
Oprogramowanie:
* Python 3.10.X lub nowszy
* (opcjonalnie) Visual Studio Code/VSCodium

Moduły do Phyton:
* discord
* pillow
* opencv (bądź cv/cv2)

Instalacja modułów:
```
pip install -r requirements.txt
```

# Użycie 
1. Do głównego folderu umieść własny plik wideo z rozszerzeniem .mp4 i nazwać go "film"
2. Utwórz folder "frames"
3. Uruchom film_na_klatki.py
```
python3 film_na_klatki.py
```
4. Przenieś wszystkie wygenerowane klatki do folderu frames
5. Otwórz bot_discord.py i edytuj wartości według podanych komentarzy
6. Uruchom bot_discord.py
7. Gotowe

# Autorzy
Zmodyfikował i spolszczył:
* White Terraria (youtube.com/channel/UC2bVJ-dHcpOA1P5FWKkjzZg)

Autor originału:
* NPCat (youtube.com/channel/UCFf2azJHYACCUIrt-a0LP2g)

Link do originału:
* github.com/NPCat/bad-apple-bot

# Problemy, propozycje i poprawki proszę zgłaszać w zakładce "Issules"

# Licencja
CC0 1.0 Universal (CC0 1.0)
Przekazanie do Domeny Publicznej
Brak praw autorskich
Osoba, która opatrzyła utwór tym oświadczeniem, przekazała go do domeny publicznej, zrzekając się wykonywania wszelkich praw do utworu wynikających z prawa autorskiego, włączając w to wszelkie prawa powiązane i prawa pokrewne, w zakresie dozwolonym przez prawo, na obszarze całego świata.

Więcej informacji: creativecommons.org/publicdomain/zero/1.0/deed.pl




