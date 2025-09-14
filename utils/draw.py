import cv2

def draw_skeleton_and_overlay(frame_bgr, keypoints, out):
    img = frame_bgr.copy()
    # later: draw keypoints & lines
    cv2.putText(img, f"Reps:{out.get('reps',0)} State:{out.get('state','-')}",
                (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
