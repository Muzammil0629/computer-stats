FROM ubuntu:24.04

COPY monitor.sh /monitor.sh

RUN chmod +x /monitor.sh

CMD ["bash", "/monitor.sh"]
