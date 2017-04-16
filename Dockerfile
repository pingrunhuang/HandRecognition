FROM ubuntu:14.04

MAINTAINER pingrunhuang@gmail.com


# required dependencies for opencv
RUN \
  apt-get update && \
  apt-get install -y \
  build-essential \
  cmake \
  git \
  wget \
  unzip \
  pkg-config \
  libswscale-dev \
  python3-dev \
  python3-numpy \
  libtbb2 \
  libtbb-dev \
  libgtk2.0-dev \
  libavcodec-dev \
  libavformat-dev \
  libjpeg-dev \
  libpng-dev \
  libtiff-dev \
  libjasper-dev \
  libavformat-dev \
  libdc1394-22-dev \
  && apt-get -y clean all \
  && rm -rf /var/lib/apt/lists/*

VOLUME $(pwd):~/dev

RUN \
  export OPENCV_ENV=/opencv \
  && mkdir $OPENCV_ENV \
  && cd $OPENCV_ENV \
  && git clone https://github.com/opencv/opencv.git \
  && git clone git clone https://github.com/opencv/opencv_contrib \
  && cd $OPENCV_ENV/opencv \
  && mkdir build \
  && cd build \
  # configure
  && cmake -D CMAKE_BUILD_TYPE=Release \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D OPENCV_EXTRA_MODULES_PATH=$OPENCV_ENV/opencv_contrib/modules \
        -D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
        -D BUILD_opencv_python2=OFF \
        -D BUILD_opencv_python3=ON \
        -D INSTALL_PYTHON_EXAMPLES=OFF \
        -D INSTALL_C_EXAMPLES=OFF \
        -D BUILD_EXAMPLES=OFF .. \

  # compile opencv
  && make -j4 \
  && sudo make install \
  && pip install numpy matplotlib

WORKDIR /opencv
