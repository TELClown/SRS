# 人机交互技术实验四

## 程序环境

   本程序的实验环境为win10，基于python3开发
   
## Dependencies

   安装speech
   
   pip install speech
   
   安装pypiwin32
   
   pip install pypiwin32
   
## 注意事项
   
   安装完成后的speech需要修改以下配置
   
   1.需要将speech.py中的
   
      import thread
   
   改为：
      
      try:
          import thread
      except ImportError:
          import _thread as thread
          
   2.需要将speech.py中的
   
      print prompt
   
   改为：
   
      print (prompt)
      
## 使用说明

    安装完speech 和 pypiwin32后运行spe.py运行程序，
    
    运行方式：python spe.py
    
    大声说明带有“开”，“电风扇”字眼的词即可得到反馈，
    
    大声说明带有“关”，“电风扇”字眼的词即可得到反馈，
    
    该实验的反馈为当检测到关键字眼时会启动draw.py中的函数开始画图。
   
   
    
           

   
   
