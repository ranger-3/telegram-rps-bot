ARG PYTHON_VERSION="3.13"
ARG WORKDIR_PATH="/app"
ARG VIRTUAL_ENV="/app/.venv"

FROM python:${PYTHON_VERSION}-slim AS build

ARG WORKDIR_PATH

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR ${WORKDIR_PATH}

RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --locked --no-install-project

COPY . ${WORKDIR_PATH}

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked


FROM python:${PYTHON_VERSION}-slim AS final

ARG WORKDIR_PATH
ARG VIRTUAL_ENV

RUN useradd -mu 1000 node
USER node

ENV VIRTUAL_ENV=${VIRTUAL_ENV}

WORKDIR "${WORKDIR_PATH}"

COPY --chown=node --from=build ${WORKDIR_PATH} ${WORKDIR_PATH}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

ENTRYPOINT ["python3","-m", "bot.app"]
