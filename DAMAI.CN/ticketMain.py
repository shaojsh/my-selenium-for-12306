import daiMai_1
import inputdata
import multiprocessing

# 告知数据源的路径
path = "C://Users//86176//Desktop//inputData.xlsx"
# 实例化对象
inputData = inputdata.ReadExcel(path)

ListNum = inputData.dict_data()
intList1 = int(ListNum[0][0])
# 对象实例化
daiMai_1 = daiMai_1.daiMai_1()
if __name__ == '__main__':
    if ListNum[1][0] != '':
        intList2 = int(ListNum[1][0])
        intPool = intList2 - intList1
        # 开连接线程池的个数
        p = multiprocessing.Pool(5)
        p.map(daiMai_1.buyDaiMaiTicket, [int(intList1)-1, intList2-1])
    else:
        daiMai_1.buyDaiMaiTicket(int(intList1)-1)
