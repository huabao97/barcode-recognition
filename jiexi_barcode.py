import barcode
from barcode.writer import ImageWriter
#支持的编码
"""
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',
 u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']
"""
def barcode_to_png(barcode_type,text_str,filename):
    EAN = barcode.get_barcode_class(barcode_type)
    ean = EAN(text_str, writer=ImageWriter())
    ean.save(filename)

if __name__=="__main__":
    barcode_to_png('code128',"M13OSA100210012000",'文件位置')