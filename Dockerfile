FROM octoenergy/pyspark:3.4.1

WORKDIR /neobank_churn

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y libc6 libsnappy-dev

RUN pip install python-snappy


EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "run.py"]