FROM nvcr.io/nvidia/l4t-base:r32.4.2

ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "$PATH" && echo "$LD_LIBRARY_PATH" && echo "$DEBIAN_FRONTEND"

RUN  echo "deb http://deb.debian.org/debian buster main" | tee -a /etc/apt/sources.list \
  && echo "deb http://deb.debian.org/debian buster-updates main" | tee -a /etc/apt/sources.list \
  && apt-key adv --keyserver   keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC \
  && apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
                                                curl \
                                                git \
                                                wget \
                                                zip \
                                                build-essential \
                                                pkg-config \
                                                zlib1g-dev \
                                                libncurses5-dev \
                                                libgdbm-dev \
                                                libnss3-dev \
                                                libssl-dev \
                                                libreadline-dev \
                                                libffi-dev \
                                                libvpx. \
                                                libx264. \
                                                libsrtp2-dev \
                                                python3.7 \
                                                python3.7-dev \
                                                ffmpeg \
                                                yasm \
                                                libavcodec-dev \
                                                libavdevice-dev \
                                                libavfilter-extra \
                                                libhdf5-dev \
                                                gfortran \
                                                libopenblas-dev \
                                                liblapack-dev \
                                                libopus-dev \
                                                libpq-dev \
                                                libgfortran4

RUN  ln -sf python3.7 /usr/bin/python3 \
  && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python3 get-pip.py --no-cache-dir \
  && pip install cython \
  && ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-36m-aarch64-linux-gnu.so /usr/lib/python3/dist-packages/apt_pkg.so

RUN  wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/av-8.0.2-cp37-cp37m-linux_aarch64.whl \
  && wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/torch-1.4.0-cp37-cp37m-linux_aarch64.whl \
  && wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/torchvision-0.5.0-cp37-cp37m-linux_aarch64.whl \
  && wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/shaloop-0.2.1_alpha.11-py3-none-linux_aarch64.whl \
  && wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/numpy-1.18.5-cp37-cp37m-linux_aarch64.whl \
  && wget --no-verbose --no-check-certificate https://storage.googleapis.com/prebuilt_packages/python37/scipy-1.4.1-cp37-cp37m-linux_aarch64.whl \
  && pip install *.whl \
  && pip install syft==0.2.9

RUN rm *.whl
