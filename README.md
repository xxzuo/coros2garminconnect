# coros2garminconnect
下载高驰.fit数据,上传到garmin connect(国内) 
## 项目说明
由于 garmin 导入活动,只能通过 [garmin connect 网页端](https://connect.garmin.cn/) 

会提示 您可以导入：
- Garmin 活动文件（.tcx .fit .gpx 格式）
- Fitbit® 生理数据或活动数据（.xls、.xlsx 或 .csv 格式）

想要将 coros 数据导入到 garmin 就需要 先在 coros 的 [training hub](https://t.coros.com/) 上把活动数据导出成 .fit 文件
再通过 [garmin connect 网页端](https://connect.garmin.cn/) 上传

## 使用教程

### 依赖安装
```
# 安装playwright库
pip install playwright

# 安装浏览器驱动文件（安装过程稍微有点慢）
python3 -m playwright install

# 或者（如果上面命令报错）
playwright install
```