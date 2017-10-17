from django.db import models

class UserApply(models.Model):
    uid = models.ForeignKey()
    name = models.CharField('申请者姓名', max_length=20, default='')
    sex = models.CharField('性别', max_length=2, default='')
    idcard = models.CharField('身份证号', max_length=20, default='')
    org = models.CharField('单位', max_length=40, default='')
    data = models.CharField('申请数据年份', max_length=10, default='')
    subject = models.CharField('专业', max_length=20, default='')
    zhicheng = models.CharField('职称', max_length=20, default='')
    goal = models.CharField('申请目的', max_length=1000, default='')
    result_list = (
        ('审核中', '审核中'),
        ('审核通过', '审核通过'),
        ('审核未通过', '审核未通过')
    )
    result = models.CharField('申请结果', max_length=10, choices=result_list)
    tele = models.CharField('电话号码', max_length=10, default='')
    email = models.CharField('邮箱', max_length=30, default='')
    adress = models.CharField('地址', max_length=40, default='')
    apply_date = models.DateTimeField('申请时间', auto_now=True)

    


