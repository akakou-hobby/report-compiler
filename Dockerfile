FROM archlinux/base:latest

RUN pacman -Syu --noconfirm
RUN pacman -Syu --noconfirm texlive-langjapanese
RUN pacman -Syu --noconfirm pandoc pandoc-crossref otf-ipafont
RUN pacman -Syu --noconfirm python python-pip
RUN pip install flask

WORKDIR /app
CMD python3 serv.py
