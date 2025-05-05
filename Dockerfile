# ------------ Runtime image ------------
FROM python:3.11-slim

ARG VERSION=dev
ARG REPO_URL=https://github.com/${GITHUB_REPOSITORY:-your/repo}

LABEL org.opencontainers.image.source=$REPO_URL \
      org.opencontainers.image.description="lib-version demo image" \
      org.opencontainers.image.licenses=MIT \
      org.opencontainers.image.version=$VERSION

WORKDIR /app
COPY lib_version/ lib_version/
COPY pyproject.toml .
RUN pip install --no-cache-dir .

CMD ["python", "-c", "from lib_version import VersionUtil; VersionUtil.print_version()"]
