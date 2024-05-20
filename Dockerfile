FROM coatldev/six:jython-3.12 as devcontainer

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
