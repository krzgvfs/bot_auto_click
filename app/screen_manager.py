import logging
import pyautogui
import cv2 

class ScreenManager:
    @staticmethod
    def get_all_matches_by_image(image_to_search: str):
        try:
            coordinates = list(pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.5))
            if coordinates:
                return coordinates
            else:
                logging.info("Imagem não encontrada")
                return []
        except Exception as ex:
            logging.error(f"Erro ao buscar imagem: {ex}")
            return []