import mysql.connector
from SpyderofHuangdaoHouse import settings


MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

conn = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT, database=MYSQL_DB)
cursor = conn.cursor(buffered=True)


class SQLLianjia2:

    #sql 语句太长很可能出错，也许是某个关键字抄错了。
    @classmethod
    def insert_data(cls, name, price, aver, build_time, subdistrict, community, source, link, area, house_type, floor,
                    decoration, orientation, build_type, structure, use):
        sql = "INSERT INTO baseinfo (`name`, `price`, `aver`, `build_time`, `subdistrict`, `community`, `source`, " \
              "`link`, `area`, `house_type`, `floor`, `decoration`, `orientation`, `build_type`, `structure`, `use` ) " \
              "VALUES (%(name)s, %(price)s, %(aver)s, %(build_time)s, %(subdistrict)s, %(community)s, %(source)s, " \
              "%(link)s, %(area)s, %(house_type)s, %(floor)s, %(decoration)s, %(orientation)s, %(build_type)s, " \
              "%(structure)s, %(use)s)"

        values = {
            "name": name, "price": price, "aver": aver, "build_time": build_time, "subdistrict": subdistrict,
            "community": community, "source": source, "link": link, "area": area,  "house_type": house_type,
            "floor": floor, "decoration": decoration, "orientation": orientation, "build_type": build_type,
            "structure": structure, "use": use
        }
        cursor.execute(sql, values)
        conn.commit()