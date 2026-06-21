import cv2
import mediapipe as mp
import pyautogui
import math
import time

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

def full_control():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )
    mp_draw = mp.solutions.drawing_utils

    screen_width, screen_height = pyautogui.size()

    # --- Smoothing ---
    smoothening = 5  # higher = smoother but slower
    prev_x, prev_y = 0, 0

    # --- Bounding Box (ROI) ---
    frame_margin = 100  # pixels inside frame

    # --- Drag State ---
    dragging = False

    # --- Cooldowns ---
    click_cooldown = 0.3
    right_click_cooldown = 0.4
    last_click_time = 0
    last_right_click_time = 0

    while True:
        success, img = cap.read()
        if not success:
            continue

        img = cv2.flip(img, 1)
        h, w, _ = img.shape

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        # Draw ROI box
        cv2.rectangle(img,
                      (frame_margin, frame_margin),
                      (w - frame_margin, h - frame_margin),
                      (255, 0, 255), 2)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:

                # --- Confidence filter ---
                if results.multi_handedness:
                    conf = results.multi_handedness[0].classification[0].score
                    if conf < 0.7:
                        continue

                lm_list = handLms.landmark

                index_tip = lm_list[8]
                thumb_tip = lm_list[4]
                middle_tip = lm_list[12]

                # --- Convert to pixel coords ---
                cx = int(index_tip.x * w)
                cy = int(index_tip.y * h)

                # --- Clamp inside ROI ---
                cx = clamp(cx, frame_margin, w - frame_margin)
                cy = clamp(cy, frame_margin, h - frame_margin)

                # --- Map ROI → Screen ---
                mapped_x = (cx - frame_margin) / (w - 2 * frame_margin) * screen_width
                mapped_y = (cy - frame_margin) / (h - 2 * frame_margin) * screen_height

                # --- Smoothing ---
                curr_x = prev_x + (mapped_x - prev_x) / smoothening
                curr_y = prev_y + (mapped_y - prev_y) / smoothening

                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

                # --- Gesture distances ---
                thumb_index_dist = distance(thumb_tip, index_tip)
                index_middle_dist = distance(index_tip, middle_tip)

                now = time.time()

                # --- LEFT CLICK ---
                thumb_ip = lm_list[3]  # thumb joint
                # Thumb closed condition (tip below joint)
                thumb_closed = thumb_tip.y > thumb_ip.y

                if thumb_closed and (now - last_click_time > click_cooldown):
                    pyautogui.click()
                    last_click_time = now

                # --- RIGHT CLICK ---
                elif index_middle_dist < 0.03 and (now - last_right_click_time > right_click_cooldown):
                    pyautogui.rightClick()
                    last_right_click_time = now

                # --- DRAG ---
                if thumb_index_dist < 0.02:
                    if not dragging:
                        pyautogui.mouseDown()
                        dragging = True
                else:
                    if dragging:
                        pyautogui.mouseUp()
                        dragging = False

                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Mouse", img)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    full_control()
