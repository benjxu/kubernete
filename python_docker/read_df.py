import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

class DBLoader:
    def __init__(self):
        connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format('root', 'Servyou_0571', '10.199.137.229', '3306', 'machine-learning-platform')
        self.engine = create_engine(connect_info)
        self.sql_cmd = "SELECT * FROM d_train_20180101"

    def read_df(self):
        df = pd.read_sql(sql=self.sql_cmd, con=self.engine)
        return df

if __name__ == "__main__":
    db_loader = DBLoader()
    df = db_loader.read_df()
    print(df.head(10))

