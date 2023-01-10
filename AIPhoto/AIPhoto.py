import mediapipe as mp
import math

def EventTrigger():
    print("AI Photo")
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

