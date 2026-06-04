FROM python:3.9-slim
WORKDIR /app
COPY server.py .
EXPOSE 8888/udp
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(2); s.sendto(b'test', ('0.0.0.0', 8888)); s.recvfrom(1024)" || exit 1

CMD ["python", "server.py"]
