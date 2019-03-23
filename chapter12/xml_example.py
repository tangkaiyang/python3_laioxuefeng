from xml.parsers.expat import ParserCreate


# ����SAX����XML�ĵ�ǣ�浽��������: ���������¼�������
# �����������ȡXML�ĵ��������¼������������¼�����Ԫ�ؿ�ʼ��Ԫ�ؽ����¼���
# ���¼�������������¼�������Ӧ���Դ��ݵ�XML���ݽ��д���

class DefualtSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_elment: %s,attrs: %s' % (name, str(attrs)))
        # name��ʾ�ڵ����ƣ�attrs��ʾ�ڵ����ԣ��ֵ䣩

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)
        # text��ʾ�ڵ�����


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

# ������ʵ��
handler = DefualtSaxHandler()
# ������ʵ��
parser = ParserCreate()

# ����3Ϊ�����������Զ���Ļص�����
# �ص������ĸ��������֪������1.9K�޵Ĵ�
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
# ��ʼ����XML
parser.Parse(xml)
# Ȼ����ǵȴ�expat������
# һ��expat����������xml�� Ԫ�ؿ�ʼ��Ԫ�ؽ�����Ԫ��ֵ �¼�ʱ
# ��طֱ����start_element, end_element, char_data����

# ����XMLParser Objects�ķ���������
# ���python�ĵ���xml.parsers.expat
# xmlparser.StartElementHandler(name, attributes)
# ����XML��ʼ��ǩʱ���ã�name�Ǳ�ǩ�����֣�attrs�Ǳ�ǩ������ֵ�ֵ�
# xmlparser.EndElementHandler(name)
# ����XML������ǩʱ���á�
# xmlparser.CharacterDataHandler(data)
# ����ʱ����
# ���п�ʼ��������ǩ֮ǰ�������ַ���content ��ֵΪ��Щ�ַ�����
# ��һ����ǩ��������һ����ǩ֮ǰ�� �����ַ���content ��ֵΪ��Щ�ַ�����
# ��һ����ǩ�������н�����֮ǰ�������ַ���content ��ֵΪ��Щ�ַ�����
# ��ǩ�����ǿ�ʼ��ǩ��Ҳ�����ǽ�����ǩ��

# Ϊ�˷�����⣬���Ѿ������滹ԭ���������̣�
# �����ʱ���ã��ֱ���S����ʾ��ʼ��E����ʾ������D����ʾdata
"""
����������ף�����Ͻű�������һ��
S<ol>C
C   S<li>S<a href="/python">CPython</a>E</li>EC
C   S<li>S<a href="/ruby">CRuby</a>E</li>EC
S</ol>E
"""
