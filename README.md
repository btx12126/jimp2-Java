# Wizualizacja Grafów Planarnych (Projekt JIMP)

Projekt stanowi drugą część zadania zaliczeniowego i skupia się na budowie graficznego interfejsu użytkownika (GUI) w technologii Java Swing. Aplikacja współpracuje z zewnętrznym silnikiem obliczeniowym napisanym w języku C, który otrzymano od innego zespołu.

## Struktura Repozytorium

Projekt został fizycznie i logicznie podzielony na dwa niezależne moduły:

* **`/algorytmyC`** – Moduł obliczeniowy (silnik C). Zawiera kod odpowiedzialny za strukturę grafu, walidację planarności oraz wyliczanie współrzędnych wierzchołków (algorytmy siłowe / Tutte'a). 
* **`/guiJava`** – Moduł interfejsu graficznego. Aplikacja okienkowa (Java Swing) pełniąca rolę głównego panelu sterowania. Odpowiada za interakcję z użytkownikiem, zarządzanie plikami wejścia/wyjścia, wywoływanie silnika C w tle oraz wizualne renderowanie wyliczonych współrzędnych na płótnie.


## Wymagania techniczne

Do poprawnego zbudowania i uruchomienia całego systemu wymagane są:
1. Środowisko uruchomieniowe oraz kompilator Java (JDK) dla interfejsu.
2. Kompilator `gcc` oraz narzędzie `make` (np. MSYS2/MinGW na platformie Windows) do zbudowania pliku wykonywalnego z modułu C.
