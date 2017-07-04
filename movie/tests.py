# -* encoding: utf-8 *-
from django.test import TestCase
from personal.mysqldb import ToMysql
import re
import time

kwargs = {'host': '106.14.218.36',
          'user': 'houhou',
          'passwd': 'Myluoxue99..2',
          'db': 'movie',
          'charset': 'utf8'
          }

sql = ToMysql(kwargs)

sql_query = "select distinct * from douban_main limit 0,10"
rows = sql.select(sql_query)
for row in rows:
    id = row[0]
    m_tag = str(row[6])
    m_tag_list = m_tag.split('/')
    m_name = row[1]

    r1 = re.findall(re.compile(r'[(（](\d{4})[)）]'), m_name)
    r2 = re.findall(re.compile(r'(.*?)[(]\d{4}'), m_name)


    m_year = r1[0] if len(r1) > 0 else '无'
    m_name = r2[0] if len(r2) > 0 else '无'

    v_year = {'m_year': m_year}
    sql.into('movie_myear', **v_year)
    year_id = sql.select('select id from movie_myear where m_year=%s' % m_year)

    year_id = year_id[0][0]
    jishu = row[22]
    m_class = "剧集" if len(jishu)>0 else "电影"
    m_class_id = 2 if len(jishu)>0 else 1
    time_now = time.localtime()
    m_douban_url = row[25]

    v_detail = {
        "m_name": m_name,
        "m_other_name": row[10],
        "m_douban_rating": -1 if row[15] == '' else float(row[15]),
        "m_douban_voters": -1 if row[16] == '' else int(str(row[16]).replace(',', '')),
        "m_douban_url": row[25],
        "m_imdb_rating": -1 if row[11] == '' else float(row[11]),
        "m_imdb_voters": -1 if row[12] == '' else int(str(row[12]).replace(',', '')),
        "m_imdb_url": row[14],
        "m_imdb_serial": row[13],
        "m_poster": row[2],
        "m_first_play": row[8],
        "m_runtime": row[9],
        "m_summary": row[17],
        "m_award": row[18],
        "m_comment_short": row[19],
        "m_comment_rating": row[20],
        "m_season": -1 if row[21] == '' else row[21],
        "m_jishu": -1 if row[22] == '' else row[22],
        "m_time_ji": -1 if row[23] == '' else row[23],
        "m_update_douban": row[24],
        "m_class_id": m_class_id,
        "m_year_id": year_id,
        "m_lan": '无',
        "m_zimu": '无',
        "m_file_format": '无',
        "m_file_size": '无',
        "m_size": '无',
        "m_time": '无',
        "m_download": '无',
        "m_update": time_now

    }

    sql.into('movie_mdetail', **v_detail)
    m_id = sql.select("select id from movie_mdetail where m_douban_url='%s'" % m_douban_url)
    m_id = m_id[0][0]
    print(m_id)

    v_class = {'m_class': m_class}
    sql.into('movie_mclass', **v_class)

    for tl in m_tag_list:
        v_tag = {'m_tag': tl}
        sql.into('movie_mtag', **v_tag)
        in_id = sql.select("select id from movie_mtag where m_tag= '%s'" % tl)

        in_id = in_id[0][0]
        v_mm_tag = {
            'mdetail_id': m_id,
            'mtag_id': in_id
        }
        print(v_mm_tag)

        sql.into('movie_mdetail_m_tag', **v_mm_tag)
