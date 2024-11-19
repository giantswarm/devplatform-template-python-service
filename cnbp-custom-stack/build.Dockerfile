# WARNING: This shows how a CNBP compatible image can be built. In real life,
# you should just extend the existing paketo.io image to take advantage of their
# security policy!
FROM ubuntu:jammy

LABEL io.buildpacks.stack.id="io.buildpacks.stacks.jammy"
ARG packages=' \
  git \
  ca-certificates \
  libexpat1 \
  libgmp-dev \
  libssl3 \
  libssl-dev \
  libyaml-0-2 \
  netbase \
  openssl \
  tzdata \
  xz-utils \
  zlib1g-dev \
  python3-dev \
  default-libmysqlclient-dev \
  build-essential \
  pkg-config \
  '
ARG package_args='--no-install-recommends'

RUN echo "Package: $packages\nPin: release c=multiverse\nPin-Priority: -1\n\nPackage: $packages\nPin: release c=restricted\nPin-Priority: -1\n" > /etc/apt/preferences && \
  echo "debconf debconf/frontend select noninteractive" | debconf-set-selections && \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get -y $package_args update && \
  apt-get -y $package_args upgrade && \
  apt-get -y $package_args install locales && \
  locale-gen en_US.UTF-8 && \
  update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \
  apt-get -y $package_args install $packages && \
  rm -rf /var/lib/apt/lists/* /tmp/* /etc/apt/preferences && \
  for path in /workspace /workspace/source-ws /workspace/source; do git config --system --add safe.directory "${path}"; done

# Set required CNB user information
ARG cnb_uid=1000
ARG cnb_gid=1000
ENV CNB_USER_ID=${cnb_uid}
ENV CNB_GROUP_ID=${cnb_gid}

# Create user and group
RUN groupadd cnb --gid ${CNB_GROUP_ID} && \
  useradd --uid ${CNB_USER_ID} --gid ${CNB_GROUP_ID} -m -s /bin/bash cnb

# Set user and group
USER ${CNB_USER_ID}:${CNB_GROUP_ID}

# Set required CNB target information
LABEL io.buildpacks.base.distro.name="ubuntu"
LABEL io.buildpacks.base.distro.version="jammy"
