# ---- Base python ----
FROM python:3.9-buster as base
# Create app directory
WORKDIR /app
# Set up and activate virtual environment
ENV VIRTUAL_ENV "/app/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt ./
# install app dependencies
RUN pip install -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
WORKDIR /app
COPY . /app
# RUN python setup.py install


# --- Release with Alpine ----
FROM python:3.9-slim-buster AS release
# Create app directory
WORKDIR /app
COPY --from=dependencies /app/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache
# Install app dependencies
RUN pip install -r requirements.txt
COPY --from=build /app/ ./
RUN chmod +x /app/bin/titan
# TODO: Fix CMD soon
CMD ["python", "-m", "titan"]
