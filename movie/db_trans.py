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

# 规整国别
# sql_query = "select * from movie_mdetail_m_area"
# rows = sql.select(sql_query)
# for row in rows:
#     id = int(row[0])
#     area_id = int(row[2])
#     print(area_id)
#     area_id = 450 if (area_id ==6325) | (area_id ==5886)| (area_id ==6138) | (area_id ==5861) | (area_id ==6269) | \
#                      (area_id ==5884) else area_id  #俄罗斯
#     area_id = 4929 if area_id == 37712 else area_id
#     area_id = 745 if area_id == 24785 else area_id
#     area_id = 450 if (area_id == 35788) | (area_id == 34867) | (area_id ==34837) else area_id
#     area_id = 2 if (area_id == 43566) | (area_id == 33756) | (area_id == 47354) | (area_id == 16175) else area_id  # 中国大陆
#     area_id = 41 if (area_id == 14832) else area_id  # 中国
#     area_id = 4089 if (area_id == 21389) | (area_id == 25) | (area_id == 33718) | (area_id == 35111) else area_id  # 中国台湾
#     area_id = 45898 if (area_id == 4311) | (area_id == 22543) else area_id  # 中国澳门
#     area_id = 5588 if (area_id == 12) | (area_id == 22543) | (area_id == 21739) else area_id  # 中国香港
#     area_id = 258 if (area_id == 7109) | (area_id == 14479) | (area_id == 15463)| (area_id == 38241)| \
#                      (area_id == 16628) | (area_id == 15462) | (area_id == 14617) | (area_id == 45877) else area_id  # 澳大利亚
#     area_id = 123 if (area_id == 24623) | (area_id == 40369) else area_id  # 爱尔兰
#     area_id = 112 if (area_id == 24990) | (area_id == 14004) | (area_id == 41645)  | (area_id == 24531)  \
#                      | (area_id == 40023) else area_id  # 瑞典
#     area_id = 70 if (area_id == 3436) | (area_id == 1923) else area_id # 瑞士
#     area_id = 7 if (area_id == 23332) else area_id  # 泰国
#     area_id = 496 if (area_id == 20440) | (area_id == 19608) | (area_id == 20201) | (area_id == 19641) | (area_id == 19702) else area_id  # 波兰
#     area_id = 63 if (area_id == 18018) | (area_id == 47084) | (area_id == 38821) else area_id  # 法国
#     area_id = 68 if (area_id == 16373) | (area_id == 23910) | (area_id == 46400) | (area_id == 38977) else area_id  # 比利时
#     area_id = 1 if (area_id == 26404) | (area_id == 30455) | (area_id == 28517) else area_id  # 日本
#     area_id = 84 if (area_id == 4501) | (area_id == 24182) | (area_id == 11125) else area_id  # 加拿大
#     area_id = 384 if (area_id == 11023) | (area_id == 25875) | (area_id == 25829) | (area_id == 26326) \
#                      | (area_id == 45223) | (area_id == 25920) else area_id  # 印度
#     area_id = 1217 if (area_id == 13638) | (area_id == 24697) else area_id  # 南斯拉夫
#     area_id = 1828 if (area_id == 17516) | (area_id == 34977) else area_id  # 印度尼西亚
#     area_id = 961 if (area_id == 20767) | (area_id == 20803) else area_id  # 墨西哥
#     area_id = 1255 if (area_id == 49072) | (area_id == 8730) | (area_id == 8631) else area_id  # 奥地利
#     area_id = 919 if (area_id == 10520) | (area_id == 25710) | (area_id == 18855) else area_id  # 巴西
#     area_id = 55 if (area_id == 1050) else area_id  # 德国
#     area_id = 49 if (area_id == 11637) else area_id  # 意大利
#     area_id = 412 if (area_id == 8058) | (area_id == 13209) | (area_id == 4574) | (area_id == 5052) | \
#                      (area_id == 38888) | (area_id == 4580) else area_id  # 捷克
#     area_id = 48 if (area_id == 47085)| (area_id == 1051) | (area_id == 43509) else area_id  # 美国
#     area_id = 47 if (area_id == 13871)  else area_id  # 西班牙
#     area_id = 57 if (area_id == 361) else area_id  # 英国
#     area_id = 51 if (area_id == 491) | (area_id == 471) | (area_id == 18855) else area_id  # 阿根廷
#     area_id = 6723 if (area_id == 362) else area_id  # 阿根廷
#     area_id = 171 if (area_id == 33144) | (area_id == 34809) else area_id  # 荷兰
#     area_id = 2260 if (area_id == 7771) else area_id  # 阿富汗
#     area_id = 171 if (area_id == 33144) | (area_id == 34809) else area_id  # 荷兰
#     area_id = 3364 if (area_id == 7105) | (area_id == 24278) else area_id  # 土耳其
#     area_id = 15813 if (area_id == 47293) else area_id  # 越南
#     area_id = 109 if (area_id == 24631) else area_id  # 挪威
#
#     print(area_id)
#     sql_up = 'update movie_mdetail_m_area set marea_id=%d where id=%d' % (area_id, id)
#     print(sql_up)
#
#     sql.updates(sql_up)

# 删除地域中的废国别条目
del_list = [
        6325, 5886, 6138, 5861, 6269, 5884, 37712, 24785, 35788, 34867, 34837,
        43566, 33756, 47354, 16175, 14832, 21389, 25, 33718, 35111, 4311, 22543,
        12, 22543, 21739, 7109, 14479, 15463, 38241, 16628, 15462, 14617, 45877,
        24623, 40369, 24990, 14004, 41645, 24531, 40023, 3436, 1923, 23332,
        20440, 19608, 20201, 19641, 19702, 18018, 47084, 38821, 16373, 23910, 46400,
        38977, 26404, 30455, 28517, 4501, 24182, 11125, 11023, 25875, 25829, 45223,
        25920, 13638, 24697, 17516, 34977, 20767, 20803, 49072, 8730, 8631, 10520, 25710,
        18855, 1050, 11637, 8058, 13209, 4574, 5052, 38888, 4580, 47085, 1051, 43509, 13871,
        361, 491, 471, 18855, 362, 33144, 34809, 7771, 33144, 34809, 7105, 24278, 47293, 24631
    ]

for i in del_list:
    sql_del = "delete from movie_marea where id=%d" % i
    print(sql_del)
    sql.updates(sql_del)

#
# sql_query = "select distinct * from douban_main limit 0,10"
# rows = sql.select(sql_query)
# for row in rows:
#     id = row[0]
#     m_tag = str(row[6])
#     m_tag_list = m_tag.split('/')
#     m_name = row[1]
#
#     r1 = re.findall(re.compile(r'[(（](\d{4})[)）]'), m_name)
#     r2 = re.findall(re.compile(r'(.*?)[(]\d{4}'), m_name)
#
#     m_year = r1[0] if len(r1) > 0 else '无'
#     m_name = r2[0] if len(r2) > 0 else '无'
#
#     v_year = {'m_year': m_year}
#     sql.into('movie_myear', **v_year)
#     year_id = sql.select('select id from movie_myear where m_year=%s' % m_year)
#
#     year_id = year_id[0][0]
#     jishu = row[22]
#     m_class = "剧集" if len(jishu)>0 else "电影"
#     m_class_id = 2 if len(jishu)>0 else 1
#     time_now = time.localtime()
#     m_douban_url = row[25]
#
#     v_detail = {
#         "m_name": m_name,
#         "m_other_name": row[10],
#         "m_douban_rating": -1 if row[15] == '' else float(row[15]),
#         "m_douban_voters": -1 if row[16] == '' else int(str(row[16]).replace(',', '')),
#         "m_douban_url": row[25],
#         "m_imdb_rating": -1 if row[11] == '' else float(row[11]),
#         "m_imdb_voters": -1 if row[12] == '' else int(str(row[12]).replace(',', '')),
#         "m_imdb_url": row[14],
#         "m_imdb_serial": row[13],
#         "m_poster": row[2],
#         "m_first_play": row[8],
#         "m_runtime": row[9],
#         "m_summary": row[17],
#         "m_award": row[18],
#         "m_comment_short": row[19],
#         "m_comment_rating": row[20],
#         "m_season": -1 if row[21] == '' else row[21],
#         "m_jishu": -1 if row[22] == '' else row[22],
#         "m_time_ji": -1 if row[23] == '' else row[23],
#         "m_update_douban": row[24],
#         "m_class_id": m_class_id,
#         "m_year_id": year_id,
#         "m_lan": '无',
#         "m_zimu": '无',
#         "m_file_format": '无',
#         "m_file_size": '无',
#         "m_size": '无',
#         "m_time": '无',
#         "m_download": '无',
#         "m_update": time_now
#
#     }
#
#     sql.into('movie_mdetail', **v_detail)
#     m_id = sql.select("select id from movie_mdetail where m_douban_url='%s'" % m_douban_url)
#     m_id = m_id[0][0]
#     print(m_id)
#
#     v_class = {'m_class': m_class}
#     sql.into('movie_mclass', **v_class)
#
#     for tl in m_tag_list:
#         v_tag = {'m_tag': tl}
#         sql.into('movie_mtag', **v_tag)
#         in_id = sql.select("select id from movie_mtag where m_tag= '%s'" % tl)
#
#         in_id = in_id[0][0]
#         v_mm_tag = {
#             'mdetail_id': m_id,
#             'mtag_id': in_id
#         }
#         print(v_mm_tag)
#
#         sql.into('movie_mdetail_m_tag', **v_mm_tag)
