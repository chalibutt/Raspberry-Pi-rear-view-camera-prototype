# Raspberry Pi rear view camera prototype
 Projekt został zaprogramowany w języku Python. Celem projektu było skonstruowanie urządzenia na wzór samochodowej kamerki cofania. Po wykonaniu programu i naciśnięciu przycisku startu, uruchamiają się wszystkie funkcje projektu. Ultradźwiękowy sensor HC-SR04 ciągle mierzy odległość na zasadzie sonaru. Trzy diody LED (żółta, zielona i czerwona) pojedynczo się uruchamiają w zależności od odległości obiektu. Kamera daje stały podgląd w rozdzielczości 1920x1080 i 30fps. Na podłączanym ekranie pokazywany jest obraz z kamery wraz z odległością w cm. By zapobiec przegrzaniu wykorzystane zostało także chłodzenie w postaci wentylatora.

Użyte elementy elektroniczne:
- Mikrokontroler Raspberry Pi 3b+
- Ultradźwiękowy czujnik odległości HC-SR04
- Kamera Raspberry Pi 3 Model B Camera Module Rev 1.3
- Diody LED
- Rezystory 1kΩ

Analiza kodu:
- Najpierw importujemy biblioteki, które zapewnią nam niezbędne funkcje
- Następnie przypisujemy nazwy do numerów pinów, aby łatwiej było je rozpoznać i ustawiamy piny jako output lub input.
- Funkcje green_light(), yellow_light() i red_light() odpowiedzialne są za włączanie jednej diody i wyłączenie całej reszty.
- Get_distance() wykonuje pomiar odległości z częstotliwością 0.00001s
- Ustawiamy parametry kamery rozdzielczość, jasność etc.
- Wykonuje się główna pętla programu. Najpierw sprawdza, czy przycisk został wciśnięty, jeśli tak to sensor zaczyna zbierać informacje i wyświetla się obraz z kamery z nałożoną datą, czasem i dystansem. Następnie określone są warunki odległości w których zapalają się poszczególne diody.

# Raspberry Pi rear view camera prototype
 The project was programmed in Python. The aim of the project was to construct a device similar to a car reversing camera. After executing the program and pressing the start button, all functions of the project start. The ultrasonic sensor HC-SR04 continuously measures the distance using the sonar principle. The three LEDs (yellow, green and red) light up individually depending on the distance of the object. The camera provides a constant preview in 1920x1080 and 30fps resolution. The connected screen shows the image from the camera along with the distance in cm. Fan cooling was also used to prevent overheating.

Electronic components used:
- Raspberry Pi 3b + microcontroller
- Ultrasonic distance sensor HC-SR04
- Camera Raspberry Pi 3 Model B Camera Module Rev 1.3
- LED indicators
- 1kΩ resistors

Code analysis:
- First, we import libraries that will provide us with the necessary functions
- Then we assign names to the pin numbers to make them easier to recognize and set the pins as output or input.
- The functions green_light (), yellow_light () and red_light () are responsible for turning one LED on and turning off all the rest.
- Get_distance () performs a distance measurement with a frequency of 0.00001s
- We set the camera parameters, resolution, brightness etc.
- The main program loop is executing. First, it checks if the button has been pressed, if so, the sensor begins to collect information and displays the image from the camera with the date, time and distance superimposed. Then the distance conditions at which individual LEDs light up are determined.
