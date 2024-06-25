# 星巴克店铺数据分析

> 本项目是杭州电子科技大学`Python程序设计`的课程期末作业。

本项目旨在对星巴克全球店铺数据进行分析，包括数据导入、清洗、探索和可视化。

## 文件结构

```shell
.
├── LICENCE
├── README.md
├── analyzer.py
├── config_manager.py
├── config_template.json
├── data_processor.py
├── main.py
├── requirements.txt
└── visualizer.py
```

## 安装

您需要一个能工作的`Python 3`执行环境。

1. 克隆仓库：

   ```shell
   git clone https://github.com/HChaZZY/starbucks-analysis.git
   cd starbucks-analysis
   ```

2. 安装依赖：

   ```shell
   pip install -r requirements.txt
   ```

## 使用方法

1. 复制 `config_template.json` 并重命名为 `config.json`。
2. 在 `config.json` 中填写必要的配置信息。
3. 运行主程序：

   ```shell
   python main.py
   ```

## 配置

在 `config.json` 中，您可以设置以下参数：

- 输入文件(csv)路径
- 输出文件(csv)路径，包括清洗输出和中国店铺输出

具体配置选项请参考 `config_template.json`。

## 许可证

本项目基于 AGPL（GNU Affero General Public License）协议开源。详情请参阅 [LICENCE](LICENCE) 文件。

## 贡献

欢迎于 `Github Issues` 提交问题和拉取请求。

## 致谢

本项目使用了以下开源库，在此对这些优秀工具的开发者们表示衷心的感谢：

- pandas
- matplotlib
- seaborn

我们深深感谢开源社区的贡献，是这些贡献使得这样的项目成为可能。

## 联系方式

如有任何问题或建议，请联系[电子邮件](mailto:i@hcha.top)
