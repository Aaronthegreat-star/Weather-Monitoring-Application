FROM python:3.13-alpine AS builder2

WORKDIR /client

RUN apk add --no-cache libffi-dev gcc musl-dev

RUN pip install --no-cache-dir fastapi uvicorn python-dotenv motor pydantic

COPY Temperature.py ./

FROM python:3.13-alpine

FROM python:alpine3.22

WORKDIR /dst

COPY --from=builder2 /client /dst/

RUN pip install --no-cache-dir fastapi uvicorn python-dotenv motor pydantic

RUN adduser -D aaron  && chown -R aaron:aaron /dst/

EXPOSE 8001

USER aaron

ENTRYPOINT ["uvicorn", "Temperature:app", "--host", "0.0.0.0", "--port", "8001"]


