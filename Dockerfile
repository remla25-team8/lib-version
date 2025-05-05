FROM python:3.11-slim
ARG VERSION=dev
ARG REPO_URL=https://github.com/${GITHUB_REPOSITORY}

ENV SETUPTOOLS_SCM_PRETEND_VERSION_FOR_LIB_VERSION=$VERSION

LABEL org.opencontainers.image.source=$REPO_URL \
      org.opencontainers.image.description="lib-version demo image" \
      org.opencontainers.image.licenses=MIT \
      org.opencontainers.image.version=$VERSION

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir .

CMD ["python", "-c", "from lib_version import VersionUtil; VersionUtil.print_version()"]
