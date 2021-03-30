FROM archlinux/base:latest

RUN patched_glibc=glibc-linux4-2.33-4-x86_64.pkg.tar.zst && \
    curl -LO "https://repo.archlinuxcn.org/x86_64/$patched_glibc" && \
    bsdtar -C / -xvf "$patched_glibc"

RUN pacman -Syu --noconfirm
RUN pacman -Syu --noconfirm texlive-langjapanese
RUN pacman -Syu --noconfirm pandoc pandoc-crossref otf-ipafont
RUN pacman -Syu --noconfirm python python-pip
RUN pip install flask

WORKDIR /app
CMD python3 serv.py
