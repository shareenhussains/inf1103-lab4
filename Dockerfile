FROM python:3.12-slim

WORKDIR /app
COPY persistent_auditor.py .

ENV INVENTORY_FILE=/data/inventory.txt

CMD ["python", "persistent_auditor.py"]