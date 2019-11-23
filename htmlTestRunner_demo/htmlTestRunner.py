import HtmlTestRunner
import unittest
import time


class UserTestCase(unittest.TestCase):
    # 开始数据
    def setUp(self):
        self.name = '小D课堂'
        print('====setup====')

    # 内容（需要以test开头）
    def test_name1(self):
        self.assertEqual(self.name, '小D课堂', msg='名字不对')
        print('======test_name1=======')

    def test_name3(self):
        self.assertEqual(self.name, '小D课堂', msg='名字不对')
        print('======test_name3=======')

    def test_name2(self):
        self.assertEqual(self.name, '小D课堂', msg='名字不对')
        print('======test_name2=======')

    # 对数据进行清理
    def tearDown(self):
        print('====tearDown=====')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase('test_name1'))
    suite.addTest(UserTestCase('test_name2'))
    suite.addTest(UserTestCase('test_name3'))

    # verbosity 可以控制执行结果输出   0 是简单报告  1 是一般报告  2 是详细报告
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    file_prefix = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fp = open('./' + file_prefix + '_result.html', "wb")
    HtmlTestRunner.HTMLTestRunner(stream=fp, title='html测试报告', descriptions=u'测试用例执行报告')
    fp.c
