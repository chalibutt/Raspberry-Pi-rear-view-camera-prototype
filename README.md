# Raspberry Pi rear view camera prototype
 Projekt został zaprogramowany w języku Python. Celem projektu było skonstruowanie urządzenia na wzór samochodowej kamerki cofania. Po wykonaniu programu i naciśnięciu przycisku startu, uruchamiają się wszystkie funkcje projektu. Ultradźwiękowy sensor HC-SR04 ciągle mierzy odległość na zasadzie sonaru. Trzy diody LED (żółta, zielona i czerwona) pojedynczo się uruchamiają w zależności od odległości obiektu. Kamera daje stały podgląd w rozdzielczości 1920x1080 i 30fps. Na podłączanym ekranie pokazywany jest obraz z kamery wraz z odległością w cm. By zapobiec przegrzaniu wykorzystane zostało także chłodzenie w postaci wentylatora.

Użyte elementy elektroniczne:
•	Mikrokontroler Raspberry Pi 3b+
•	Ultradźwiękowy czujnik odległości HC-SR04
•	Kamera Raspberry Pi 3 Model B Camera Module Rev 1.3
•	Diody LED
•	Rezystory 1kΩ

Analiza kodu:
•	Najpierw importujemy biblioteki, które zapewnią nam niezbędne funkcje
•	Następnie przypisujemy nazwy do numerów pinów, aby łatwiej było je rozpoznać i ustawiamy piny jako output lub input.
•	Funkcje green_light(), yellow_light() i red_light() odpowiedzialne są za włączanie jednej diody i wyłączenie całej reszty.
•	Get_distance() wykonuje pomiar odległości z częstotliwością 0.00001s
•	Ustawiamy parametry kamery rozdzielczość, jasność etc.
•	Wykonuje się główna pętla programu. Najpierw sprawdza, czy przycisk został wciśnięty, jeśli tak to sensor zaczyna zbierać informacje i wyświetla się obraz z kamery z nałożoną datą, czasem i dystansem. Następnie określone są warunki odległości w których zapalają się poszczególne diody.
