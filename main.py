from screen_manager import ScreenManager

def run():
    coordenadas = ScreenManager.get_all_matches_by_image("logo.jpg")
    if coordenadas:
        for coordenada in coordenadas:
            print(coordenada)
    else:
        pass

while True: 
    run()