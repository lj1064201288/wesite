from django.contrib.admin import AdminSite

# 设置自定义后台的显示
class CustomSite(AdminSite):
    site_header = "小熊猫博客"
    site_title = "小熊猫管理后台"
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')