#GPT powinien być  włączony na przybliżenie 67%
#Bard powinien być włączony normalnie
#Rozmowę należy zacząć od napisania do barda.
#Sam kod nie będzie działał bez plików zdjęciowych.
#Po aktualizacje zapraszam na
#Sprawdź aktualizacje na https://github.com/rafafunt

#Autorem programu jest rafafunt


import pyautogui
import keyboard
import time

def press_ctrl_v():
    # Wciśnięcie klawisza Ctrl
    keyboard.press("ctrl")
    time.sleep(0.1)  # Odczekanie chwilę, aby upewnić się, że klawisz Ctrl jest wcisnięty.

    # Wciśnięcie klawisza V
    keyboard.press_and_release("v")
    time.sleep(0.1)  # Odczekanie chwilę, aby upewnić się, że klawisz V jest wcisnięty.

    # Zwolnienie klawisza Ctrl
    keyboard.release("ctrl")

def find_and_click_lowest_icon_on_screen(image_path, confidence=0.8):
    try:
        # Wyszukanie wszystkich wystąpień wzorca na ekranie
        locations = list(pyautogui.locateAllOnScreen(image_path, confidence=confidence))

        if locations:
            # Wybieramy ikonę, która ma największe współrzędne Y (najniżej na ekranie)
            lowest_icon = max(locations, key=lambda loc: loc.top + loc.height)

            # Pobranie współrzędnych środka ikony
            center_x = lowest_icon.left + lowest_icon.width // 2
            center_y = lowest_icon.top + lowest_icon.height // 2

            # Przesunięcie kursora myszy na środek ikony
            pyautogui.moveTo(center_x, center_y)

            # Kliknięcie lewym przyciskiem myszy
            pyautogui.click()
            return True
        else:
            print("Nie znaleziono żadnej ikony na ekranie.")
            return False

    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika.")
        return False


def is_image_on_screen(image_path, confidence=0.8):
    try:
        # Wyszukanie wzorca na ekranie
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)

        if location is not None:
            return True
        else:
            return False

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return False


# Przykład użycia funkcji
try:
    # Wprowadź ścieżkę do obrazu, który chcesz sprawdzić na ekranie
    image_path = 'sciezka/do/obrazu.png'

    # Sprawdzenie, czy obraz jest na ekranie
    is_image_present = is_image_on_screen(image_path)
    print(f"Obraz jest na ekranie: {is_image_present}")

except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika.")

import pyautogui
import time


def scroll_down(image_path, confidence=0.8):
    try:
        # Wyszukanie wzorca na ekranie
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)

        if location is not None:
            # Pobranie współrzędnych środka ikony
            center_x = location.left + location.width // 2
            center_y = location.top + location.height // 2

            # Przesunięcie kursora myszy na środek ikony
            pyautogui.moveTo(center_x, center_y)

            # Odczekanie krótkiego czasu, aby umożliwić użytkownikowi zobaczenie, gdzie najechał kursor myszy.
            time.sleep(1)

            # Wykonaj scrollowanie myszą w dół o 100 jednostek (możesz dostosować wartość, jeśli potrzebujesz większego lub mniejszego scrolla).
            pyautogui.scroll(-100)

            return True
        else:
            print("Nie znaleziono ikony na ekranie.")
            return False

    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika.")
        return False


# Przykład użycia funkcji
def dzialanie():
    # Wprowadź ścieżkę do obrazu ikony, którą chcesz znaleźć
    icon_image_path = 'kropki.png'

    # Poczekaj na przesunięcie myszy na miejsce, gdzie chcesz znaleźć ikonę, a następnie wykonaj kliknięcie.
    print("Przenieś kursor myszy na miejsce, gdzie chcesz znaleźć ikonę.")
    time.sleep(2)

    # Wywołanie funkcji znajdującej i klikającej w najniższą ikonę na ekranie
    find_and_click_lowest_icon_on_screen(icon_image_path)
    while not is_image_on_screen("bardcopy.png"):
        time.sleep(1)
    find_and_click_lowest_icon_on_screen("bardcopy.png")
    find_and_click_lowest_icon_on_screen("sendgpt.png")
    press_ctrl_v()
    find_and_click_lowest_icon_on_screen("clickgpt.png")
    while not is_image_on_screen("regenerate.png"):
        time.sleep(1)
    if is_image_on_screen("gptarrow.png"):
        find_and_click_lowest_icon_on_screen("gptarrow.png")

    time.sleep(2)
    find_and_click_lowest_icon_on_screen("gptcopy.png")
    find_and_click_lowest_icon_on_screen("bardsend.png")
    press_ctrl_v()
    find_and_click_lowest_icon_on_screen("bardclick.png")
    while not is_image_on_screen("bardcheck.png"):
        time.sleep(1)
    time.sleep(7)
    scroll_down("audio.png")
    time.sleep(2)
    return dzialanie()
print("Ai cooperation by rafafunt")
print("https://github.com/rafafunt")
try: dzialanie()


except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika.")

