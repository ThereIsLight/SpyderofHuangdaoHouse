import mysql.connector

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'yg19940916'
MYSQL_PORT = '3306'
MYSQL_DB = 'huangdao_house'  # 数据库的名字要更改
conn = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT, database=MYSQL_DB)
cursor = conn.cursor(buffered=True)

class Lianjia2SQL:

    @classmethod
    def insert_data(cls, name, price, aver, build_time, subdistrict, community, address, source, link, area, house_type, floor,
                    decoration, orientation, build_type, structure, use):
        sql = "INSERT INTO resold_house (`name`, `price`, `aver`, `build_time`, `subdistrict`, `community`, `address`, `source`," \
              "`link`, `area`, `house_type`, `floor`, `decoration`, `orientation`, `build_type`, `structure`, `use` ) " \
              "VALUES (%(name)s, %(price)s, %(aver)s, %(build_time)s, %(subdistrict)s, %(community)s, %(address)s, %(source)s, " \
              "%(link)s, %(area)s, %(house_type)s, %(floor)s, %(decoration)s, %(orientation)s, %(build_type)s, " \
              "%(structure)s, %(use)s)"

        values = {
            "name": name, "price": price, "aver": aver, "build_time": build_time, "subdistrict": subdistrict,
            "community": community, "address": address, "source": source, "link": link, "area": area,  "house_type": house_type,
            "floor": floor, "decoration": decoration, "orientation": orientation, "build_type": build_type,
            "structure": structure, "use": use
        }
        cursor.execute(sql, values)
        conn.commit()