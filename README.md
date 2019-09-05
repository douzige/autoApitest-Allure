# autoApitest-Allure
pytest,allure
学习使用   python +pytest +allure  测试接口项目
  1. 环境 python 3.6 win10


安装依赖包：
       pip install pytest  
       pip install pytest-allure-adaptor  ( allure  依赖)
执行命令：       
      pytest -s --alluredir=./report   执行测试命令,测试数据输出到report 目录
      allure generate ./report -o report/allure_report --clean  生成allure的报告      
