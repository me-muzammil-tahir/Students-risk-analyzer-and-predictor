FROM python:3.9-slim

WORKDIR /app

# Saari files copy karein
COPY . .

# Libraries install karein
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit ka port
EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py"]