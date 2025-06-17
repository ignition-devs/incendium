FROM quay.io/ignition-devs/devcontainer-base:jython

COPY pkg/requirements.txt /tmp/requirements.txt

# pip caching disabled by base image
# hadolint ignore=DL3042
RUN set -eux; \
    \
    python2 -m pip install --requirement \
        /tmp/requirements.txt; \
    rm -rf /tmp/*

CMD ["/bin/bash"]