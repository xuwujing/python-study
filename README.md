# python-study

  python-study是本人在学习python的一些练习代码汇总的项目。
  
  
  
## 生成环境配置文件requirements.txt

方法一：整个环境下的安装包都保存到requirements.txt中

pip freeze > requirements.txt

方法二：只生成单个项目中的使用到的安装包
#### 设置编码和覆盖

pip install pipreqs
pipreqs ./ --encoding=utf8  --force 
