import os, sys

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from core import src

if __name__ == '__main__':
    src.run()


'''
			模拟实现一个ATM + 购物商城程序
			额度 15000或自定义
			实现购物商城，买东西加入 购物车，调用信用卡接口结账
			可以提现，手续费5%
			支持多账户登录
			支持账户间转账
			记录日常消费流水
			提供还款接口
			ATM记录操作日志
			提供管理接口，包括添加账户、冻结账户等。。。
			用户认证用装饰器
'''

'''
	1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品

'''