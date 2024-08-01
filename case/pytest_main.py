import pytest
#
# if __name__ == '__main__':
#     pytest.main(['-vs', 'DriverTools.py'])


# 添加命令行参数 --html=report.html 和 --html=report.html --self-contained-html
if __name__ == "__main__":
    pytest.main(["DriverTools.py",   # 测试用例
                 "--html=../report/report.html",   # 生成测试报告 生成assert存放的css文件和html文件
                 "--self-contained-html",  # 把css样式合并到html里 仅生成html文件
                 ])