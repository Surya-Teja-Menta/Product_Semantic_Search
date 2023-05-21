FROM python:3.7-slim


WORKDIR /

RUN pip3 install --upgrade pip

RUN pip3 install pandas==1.3.5


COPY requirements.txt ./

RUN pip3 install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html


RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]