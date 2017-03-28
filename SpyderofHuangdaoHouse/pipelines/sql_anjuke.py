import mysql.connector

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'yg19940916'
MYSQL_PORT = '3306'
MYSQL_DB = 'huangdao_house'  # 数据库的名字要更改
conn = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT, database=MYSQL_DB)
cursor = conn.cursor(buffered=True)

class AnjukeSQL:
    """
    要插入表的名字要修改
    注意item也要修改
    """
    @classmethod
    def insert_data(cls, name, aver, around_aver, house_type, use, developer, subdistrict, address, status,
                    start_time, give_time, use_num, company, build_type, source, link):
        sql = "INSERT INTO new_house (`name`, `aver`,`around_aver`, `house_type`, `use`, `developer`, `subdistrict`, " \
              "`address`, `source`,`link`, `status`, `start_time`,`give_time`, `use_num`, `company`, `build_type`) " \
              "VALUES (%(name)s, %(aver)s, %(around_aver)s, %(house_type)s, %(use)s, %(developer)s, %(subdistrict)s, " \
              "%(address)s, %(source)s,%(link)s, %(status)s, %(start_time)s, %(give_time)s, %(use_num)s, %(company)s, " \
              "%(build_type)s)"

        values = {
            "name": name, "aver": aver, "around_aver": around_aver, "house_type": house_type, "use": use,
            "developer": developer, "subdistrict": subdistrict, "address": address, "source": source,
            "link": link, "status": status,  "start_time": start_time, "give_time": give_time, "use_num": use_num,
            "company": company, "build_type": build_type
        }
        cursor.execute(sql, values)
        conn.commit()