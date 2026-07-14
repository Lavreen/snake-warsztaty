# 🐍 Snake — nasze pierwsze prawdziwe programowanie

Witaj! W tym repozytorium jest kod gry **Snake** napisany w Pythonie.
Gra działa... ale ktoś ją mocno popsuł. 😈
Twoim zadaniem jest ją naprawić — krok po kroku, według kartki z zadaniami.

## Co będzie potrzebne (instalujemy raz)

### 1. Python
1. Wejdź na https://www.python.org/downloads/ i kliknij żółty przycisk **Download Python**.
2. Uruchom pobrany plik.
3. **WAŻNE:** na pierwszym ekranie zaznacz ptaszek **„Add python.exe to PATH"**, dopiero potem kliknij **Install Now**.

### 2. Visual Studio Code (nasz edytor kodu)
1. Wejdź na https://code.visualstudio.com i kliknij niebieski przycisk **Download**.
2. Uruchom pobrany plik i klikaj **Dalej** aż do końca.

### 3. Pobranie gry (tego repozytorium)
1. Na tej stronie kliknij zielony przycisk **`<> Code`**, a potem **Download ZIP**.
2. Rozpakuj pobrany plik (prawy przycisk myszy → **Wyodrębnij wszystkie**), np. na Pulpit.

### 4. Otwarcie gry w VS Code
1. Uruchom VS Code.
2. Menu **File → Open Folder...** i wybierz rozpakowany folder `snake-warsztaty`.
3. Jeśli pojawi się pytanie „Do you trust the authors...?" → kliknij **Yes, I trust**.
4. W prawym dolnym rogu wyskoczy dymek z propozycją instalacji rozszerzenia **Python** → kliknij **Install**.
   (Jeśli dymek nie wyskoczył: ikona klocków 🧩 na lewym pasku → wpisz `Python` → **Install** przy pierwszym wyniku od Microsoft.)

### 5. Instalacja biblioteki `pygame` (silnik naszej gry)
1. W VS Code menu **Terminal → Run Task... → Zainstaluj pygame**.
2. Poczekaj, aż w okienku na dole przestanie się „dziać" — gotowe!

## 🚀 Jak uruchomić grę

1. Kliknij plik **`snake.py`** na liście po lewej stronie.
2. Kliknij trójkąt **▶ (Run)** w prawym górnym rogu.
3. Gra się uruchomi. Żeby ją zamknąć — kliknij ✕ na okienku gry.

Po każdej zmianie w kodzie: **zapisz plik (Ctrl+S)** i uruchom grę jeszcze raz.

## 📁 Co jest w środku

| Plik | Co to jest |
|---|---|
| `snake.py` | **Tu pracujesz!** Popsuta gra do naprawienia. |
| `rozwiazanie/snake_gotowy.py` | Gotowa gra — zaglądaj tylko w ostateczności 😉 |
| `requirements.txt` | Lista bibliotek, których potrzebuje gra. |
| `.vscode/` | Ustawienia edytora — nie ruszaj, ale wiedz, że dzięki nim działa przycisk ▶. |

## 🆘 Coś nie działa?

- **„python is not recognized..."** → Python zainstalowany bez ptaszka „Add to PATH". Odinstaluj i zainstaluj jeszcze raz (punkt 1).
- **`ModuleNotFoundError: No module named 'pygame'`** → wykonaj jeszcze raz punkt 5.
- **Czerwone podkreślenie w kodzie** → gdzieś jest literówka. Porównaj dokładnie z kartką zadań, znak po znaku.
- Gra „zawiesza się" po uruchomieniu ▶ drugi raz → najpierw zamknij poprzednie okienko gry.
