import streamlit as st
import cv2
import time

# Import modules (with safe fallbacks if teammates haven’t finished theirs yet)
try:
    from pose_engine import get_keypoints
except Exception:
    def get_keypoints(frame_bgr):
        return {}

try:
    from exercise_logic import SquatCounter
except Exception:
    class SquatCounter:
        def __init__(self): self.reps = 0
        def update(self, keypoints): return {"reps": self.reps, "state": "-"}

try:
    from analytics import compare_to_benchmark
except Exception:
    def compare_to_benchmark(user_reps, exercise, age, gender):
        return {"user_reps": user_reps, "avg_reps": 0, "percent_diff": 0.0}

try:
    from gamification import award_badges
except Exception:
    def award_badges(history, latest_session): return []

try:
    from utils.draw import draw_skeleton_and_overlay
except Exception:
    def draw_skeleton_and_overlay(frame_bgr, keypoints, out):
        img = frame_bgr.copy()
        cv2.putText(img, f"Reps:{out.get('reps',0)} State:{out.get('state','-')}",
                    (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# --- Streamlit UI ---
st.set_page_config(page_title="FitScan AI", layout="wide")
st.title("FitScan AI – Integration Scaffold")

run_webcam = st.checkbox("Start webcam smoke test")
exercise_name = st.selectbox("Exercise", ["squat", "pushup"])

counter = SquatCounter()
session_history = []

def read_frame(cap):
    ok, frame = cap.read()
    return frame if ok else None

def process_frame(frame):
    keypoints = get_keypoints(frame)
    out = counter.update(keypoints)
    display_img = draw_skeleton_and_overlay(frame, keypoints, out)
    return display_img, out

if run_webcam:
    placeholder = st.empty()
    cap = cv2.VideoCapture(0)
    try:
        for _ in range(100):  # stop after 100 frames so it doesn’t loop forever
            frame = read_frame(cap)
            if frame is None:
                st.warning("No frame captured. Stopping.")
                break
            display_img, out = process_frame(frame)
            placeholder.image(display_img, channels="RGB")
            time.sleep(0.02)
    finally:
        cap.release()

    latest_session = {"exercise": exercise_name, "reps": out.get("reps", 0)}
    session_history.append(latest_session)
    analytics_res = compare_to_benchmark(latest_session["reps"], exercise_name, "18-25", "M")
    badges = award_badges(session_history, latest_session)

    st.subheader("Session summary")
    st.write(latest_session)
    st.write(analytics_res)
    st.write("Badges:", badges)
else:
    st.info("Toggle 'Start webcam smoke test' to run the demo.")


