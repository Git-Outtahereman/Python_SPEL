# Bombo Bingbob

Bombo Bingbob is een eenvoudig maar leuk 2D-spel gemaakt met Pygame. Het spel draait om twee spelers: een rode (Bombo) en een blauwe. De rode speler probeert de blauwe speler te vangen, terwijl de blauwe speler probeert te overleven en punten te verdienen.

## Doel van het Spel
- De rode speler (Bombo) probeert de blauwe speler te raken om punten te scoren.
- De blauwe speler probeert zo lang mogelijk te overleven en verdient elke 8 seconden een punt.
- Je wint als je 10 punten haalt
  

## Besturing
### Blauwe Speler (Ontwijk de rode speler!)
- `W` - Beweeg omhoog
- `A` - Beweeg naar links
- `S` - Beweeg omlaag
- `D` - Beweeg naar rechts

### Rode Speler (Vang de blauwe speler!)
- `I` - Beweeg omhoog
- `K` - Beweeg omlaag
- `J` - Beweeg naar links
- `L` - Beweeg naar rechts
- `Spatiebalk` - Dash (snelle sprint, met cooldown)

## Power-Ups **Groene vierkantjes**
  - Wanneer de blauwe speler een groene power-up oppakt:
  - De blauwe speler wordt kleiner (20x20 in plaats van 50x50) en daardoor moeilijker te raken.
  - De power-up werkt gedurende enkele seconden en verdwijnt dan.
  - De power-up verschijnt opnieuw na een cooldown-periode.
 
  - Wanneer de rode speler (bombo) een groene power-up oppakt:
  - Er verschijnt een muur van in totaal 400 pixels waarvan aan de boven en onderkant van de powerup 200 ieder. Hier kan Bombo doorheen alleen de blauwe speler niet. Als de blauwe speler hem raakt krijgt bombo een punt en resetten Bombo en de blauwe speler.
  - De power-up werkt gedurende enkele seconden en verdwijnt dan.
  - De power-up verschijnt opnieuw na een cooldown-periode.

## Score Systeem
- **Bombo's Score**: Verhoogt elke keer dat de rode speler de blauwe speler vangt.
- **Blauwe Score**: Verhoogt automatisch met 1 punt elke 8 seconden als de blauwe speler nog leeft.

## Extra mechanics
- Beide spelers kunnen aan de randen van het scherm naar de andere kant teleporteren.
- De rode speler heeft een dash-move om sneller te bewegen, maar deze heeft een cooldown.

## Installatie en Uitvoering
1. Zorg ervoor dat je Python en Pygame hebt geïnstalleerd:
   ```sh
   pip install pygame
   ```
2. Voer het spel uit met:
   ```sh
   python main.py
   ```

Veel plezier met spelen!

## Feedback
Voor feedback vul het formulier in
https://docs.google.com/forms/d/e/1FAIpQLSdoSxe1JkzdrJurOkEOKuLHegwd5GJ-75GNn64hwxgWcLpXaA/viewform?usp=preview 

## Evaluatie
**Mathijs:**<br>
**Declan:** 
ik heb geleerd hoe je een gameloop maakt en hoe je collision detecteert in pygame. Ik heb ook feedback van gebruikers toegevoegd  aan onze game.


## Makers van het spel


Mathijs bakker en Declan Tijms
