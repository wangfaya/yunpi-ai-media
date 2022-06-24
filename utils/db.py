import pymysql
from urllib.parse import quote


from settings.config import MYSQL_CONFIG


def conn_mysqldb(db_config):
    """
    连接mysql
    """
    '''连接MySQL数据库'''
    try:
        db = pymysql.connect(
            host=db_config['host_port'][0][0],
            port=db_config['host_port'][0][1],
            user=quote(db_config['user_name']),
            passwd=quote(db_config['password']),
            db=quote(db_config['database']),
            charset='utf8'
        )
        return db
    except Exception:
        raise Exception("数据库连接失败")


server_sql = conn_mysqldb(MYSQL_CONFIG['zzgl_data'])
