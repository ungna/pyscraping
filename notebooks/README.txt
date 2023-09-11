[jupyter notebook]: 

Anaconda Powershell Prompt을 이용해 local로 열기

# YSIT23으로 environment 바꿈
conda activate YSIT23

# jupyter에서 원하는 파일 경로 넣어서 바로 열기
jupyter notebook --notebook-dir="D:\projAi_2023_ysh\books\pyscraping\notebooks"


주피터에서 ipynb파일 전체 파이썬확장자로 변경하기
1. pip install nbconvert  설치 
2. conda activate YSIT23 
3. (YSIT23) PS C:\Users\kimjy> d:
4. cd D:\Jworkspace\DataAnalysis\hg-da2 (주피터 파일 경로)
5. jupyter nbconvert *.ipynb --to script 
