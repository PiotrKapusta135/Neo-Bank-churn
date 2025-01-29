import streamlit as st
import glob
from pyspark.sql import SparkSession


def create_spark_session(app_name):
    session = SparkSession.builder\
        .appName(app_name)\
        .master("local[*]")\
        .config("spark.sql.legacy.parquet.nanosAsLong", "true") \
        .config("spark.jars", "/utils/snappy-java-1.1.10.5.jar") \
        .getOrCreate()
    return session

def get_all_files_with_pattern(path_pattern):
    all_files = glob.glob(path_pattern)
    return all_files

def load_parquet_to_pyspark_df(spark_session, path):
    df = spark_session.read.parquet(path)
    return df

def load_all_files_to_spark_df(spark_session, path_pattern):
    files = get_all_files_with_pattern(path_pattern)
    df = load_parquet_to_pyspark_df(spark_session, files[0])
    for file in files[1:]:
        df = df.union(load_parquet_to_pyspark_df(spark_session, file))
    return df

def get_churn_train_df():
    session = create_spark_session('neobank_churn')
    path_pattern = 'data/train_*'
    df = load_all_files_to_spark_df(session, path_pattern)
    return df
