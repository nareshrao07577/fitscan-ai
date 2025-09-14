import streamlit as st
import cv2

st.set_page_config(page_title="FitScan AI", layout="wide")
st.title("FitScan AI – Integration Scaffold")

st.markdown("**This is the integration scaffold.**")
st.markdown("Webcam + Pose + Logic + Analytics + Badges will appear here.")

# Webcam smoke test button
run = st.checkbox("Start webcam smoke test")
if run:
    cap = cv2.VideoCapture(0)
    ok, frame = cap.read()
    if ok:
        st.success("Webcam found. Full loop will be added after contracts.")
    else:
        st.error("Webcam not found.")
    cap.release()
