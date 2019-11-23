import unittest


class UserTestCase(unittest.TestCase):
    # 开始数据
    def setUp(self):
        self.name = '小D课堂'
        print('====setup====')

    # 内容（需要以test开头）
    def test_name(self):
        self.assertEqual(self.name, '小D课堂', msg='名字不对')
        print('======test_name=======')

    # 对数据进行清理
    def tearDown(self):
        print('====tearDown=====')


if __name__ == '__main__':
    unittest.main()
