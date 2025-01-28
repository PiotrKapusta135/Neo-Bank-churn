from function.utils import load_all_files_to_spark_df, create_spark_session

def get_churn_train_df():
    session = create_spark_session('neobank_churn')
    path_pattern = 'data/train_*'
    df = load_all_files_to_spark_df(session, path_pattern)
    return df