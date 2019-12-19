from appium import webdriver
desired_caps = {}
# 测试平台
desired_caps["platformName"] = "Android"
# 测试版本
desired_caps["platformVersion"] = "5.1"
# 驱动名称：华为（随意取）
desired_caps["deviceName"] = "华为"
# 启动包名
desired_caps["addPackage"] = "com.android.settings"
# 启动那个应用
desired_caps["addActivity"] = ".setting"

# 声明手机驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)