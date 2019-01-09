
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import base64
import pyqrcode
import qrcode

class SsrPipeline(object):
    def process_item(self, item, spider):
        ip = item['ip']
        password = item['password']
        port = item['port']
        method = item['passType']

        str1 = method + ':' + password + '@' + ip + ':' + port

        str2 = base64.b64encode(str1.encode())
        
        qr = qrcode.make('ss://'.encode()+str2)
        qr.save('t1.png')

        # img = pyqrcode.create('ss://'+str2.decode(), error='L', version=27, mode='binary')
        #
        # img.png('code.png', scale=3, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        #
        # img.show()

        return item
