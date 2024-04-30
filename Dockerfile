# hadolint global ignore=DL3008,DL3042
FROM coatldev/six:3.12 as base

ENV JYTHON_VERSION 2.7.3
ENV JYTHON_HOME /opt/jython/${JYTHON_VERSION}

RUN set -eux; \
    \
    apt-get update --quiet; \
    apt-get install --yes --no-install-recommends \
        openjdk-17-jre \
    ; \
    rm -rf /var/lib/apt/lists/*

# >============================================================================<

FROM base as jython

RUN set -eux; \
    \
    apt-get update --quiet; \
    apt-get install --yes --no-install-recommends \
        wget \
    ; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN set -eux; \
    \
    wget -q "https://repo1.maven.org/maven2/org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar"; \
    \
    java -jar "jython-installer-${JYTHON_VERSION}.jar" \
        --silent \
        --type standard \
        --directory "$JYTHON_HOME"

# >============================================================================<

FROM base as final

COPY --from=jython ${JYTHON_HOME}/ ${JYTHON_HOME}/

ENV PATH ${JYTHON_HOME}/bin:$PATH

COPY requirements /tmp/requirements/

RUN set -eux; \
    \
    python2 -m pip install --requirement \
        /tmp/requirements/dev.txt; \
    \
    python3 -m pip install --requirement \
        /tmp/requirements/build.txt

CMD ["/bin/bash"]
