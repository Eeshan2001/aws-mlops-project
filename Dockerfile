# ---------- Base Image ----------
FROM python:3.12-slim

# ---------- Environment ----------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------- Working Directory ----------
WORKDIR /app

# ---------- System Packages ----------
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy Requirements ----------
COPY requirements.txt .

# ---------- Install Dependencies ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Download NLTK Data ----------
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"

# ---------- Copy Application ----------
COPY . .

# ---------- Expose Port ----------
EXPOSE 5000

# ---------- Start Gunicorn ----------
CMD gunicorn --config gunicorn.conf.py run:app