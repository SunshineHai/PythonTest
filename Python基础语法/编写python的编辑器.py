# 1.IPython ：是 一种加强版的 Python 解释器
# 2.Juypyter notebook 是一种基于 Web 的代码笔记本。
# 3.Pycharm.

# 4.安装 IPython 和 Jupyter
# 4.1 安装IPython
    # pip install Ipython
# 4.2 安装Jupyter :
    # 我偏向于使用最简单的方法：直接使用pip安装 ： pip install notebook
    # 打开Jupyter命令：
    # jupyter notebook
'''特点；Tab 补全，这种一般在 IDE中才有。'''
# 5.Anaconda 介绍
'''Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。
因为包含了大量的科学包，Anaconda 的下载文件比较大（约 531 MB），
如果只需要某些包，或者需要节省带宽或存储空间，也可以使用Miniconda这个较小的发行版（仅包含conda和 Python）。'''
# 6.使用 pip时，服务器在国外，下载较大的包时会因timeout而报错，改用国内豆瓣服务器下载：
# pip install 包名  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
''' 
pip install jupyterlab  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
'''
# 7.更新 pip 版本命令：
# python -m pip install -U pip

# 8.<利用python进行数据分析> 书中代码GitHub托管代码地址：http://github.com/wesm/pydata-book