FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim

ARG VERSION=dev
ARG REPO_URL=https://github.com/${GITHUB_REPOSITORY:-your/repo}

LABEL org.opencontainers.image.source=$REPO_URL \
      org.opencontainers.image.description="lib-version demo image" \
      org.opencontainers.image.licenses=MIT \
      org.opencontainers.image.version=$VERSION

WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY src/ .

CMD ["python", "-c", "from lib_version import VersionUtil; VersionUtil.print_version()"]
