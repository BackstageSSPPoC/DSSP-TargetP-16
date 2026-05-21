# ============================================================
# AI-Generated Dockerfile
# Language: python | Framework: python
# Builder: python:3.11-slim → Runtime: python:3.11-slim
# ============================================================

FROM python:3.11-slim AS builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
COPY --from=builder /install /usr/local
COPY . .
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:5000/health || exit 1
ENTRYPOINT ["python", "app.py"]