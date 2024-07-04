FROM coatldev/six:3.12 AS base

ENV JYTHON_HOME=/opt/jython

# install Java
# hadolint ignore=DL3008
RUN set -eux; \
    apt-get update; \
    apt-get install --yes --no-install-recommends \
        openjdk-17-jre \
        ; \
    rm -rf /var/lib/apt/lists/*

# >============================================================================<

FROM base AS jython

ENV JYTHON_VERSION=2.7.3

WORKDIR /tmp

RUN set -eux; \
    \
    wget -q "https://repo1.maven.org/maven2/org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar"; \
    \
    java -jar "jython-installer-${JYTHON_VERSION}.jar" \
        --silent \
        --type standard \
        --directory "${JYTHON_HOME}"

# >============================================================================<

FROM base AS devcontainer

COPY --from=jython ${JYTHON_HOME}/ ${JYTHON_HOME}/

ENV PATH="${JYTHON_HOME}/bin:$PATH"

COPY requirements /tmp/requirements/

# pip caching disabled by base image
# hadolint ignore=DL3042
RUN set -eux; \
    \
    python2 -m pip install --requirement \
        /tmp/requirements/dev.txt; \
    \
    python3 -m pip install --requirement \
        /tmp/requirements/build.txt

CMD ["/bin/bash"]