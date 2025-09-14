# Run locally

python -m venv venv
# Windows: venv\Scripts\activate
# mac / linux: source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

Troubleshooting:
- If webcam fails, set environment variable or use a test video and toggle capture source in app.py.
