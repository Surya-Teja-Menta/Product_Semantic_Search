FROM python:3.7.16-alpine3.18

WORKDIR /src

COPY requirements.txt ./

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install -r src/requirements.txt

COPY . .

CMD ["streamlit","run", "app.py"]