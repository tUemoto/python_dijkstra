FROM python:3.11-rc-bullseye
ENV PYTHONPATH $PYTHONPATH:/workspaces/python_dijkstra

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
