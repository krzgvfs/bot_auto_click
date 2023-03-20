import logging
import pyautogui
import cv2

class ScreenManager:
    @staticmethod # Não precisa instanciar para utilizar os metodos.
    def get_all_matches_by_image(image_to_search: str):
        try:
            return pyautogui.locateAllOnScreen(image=image_to_search, greyscale=True, confidence=0.9)
        except Exception as ex:
            logging.info(f"Imagem não encontrada: Erro:{ex}")
