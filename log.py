#!/usr/bin/python3

"""
2022-05-04
python Script created by eddie
인자 
1 : date - format('yyyy-MM-dd') - 파일 명으로 사용
2 : date - format('yyyy-MM-dd HH:mm:ss') - 해당 내용 실행 일시로 사용
3 : TAG - ([INFO], [WARN], [ERROR], [SQL] 등 편한대로 구성하여 넘겨줌) - TAG로 사용 
4 : MESSAGE - 실행 쿼리나 log남길 내용  - 해당 중요 내용 남김

Log 출력 예시 
[INFO][2022-05-03 15:28:22] - AI downSampling
[SQL][2022-05-03 15:28:22] - SELECT * FROM mysql.patient
"""

import sys 
import os

#들어온 내용 argument 정리 
today = str(sys.argv[1])
todayWithSecond = str(sys.argv[2])
tag = str(sys.argv[3])
message = str(sys.argv[4])

print(today+todayWithSecond+tag+message)

# 파일 경로 생성
pwd = os.getcwd()
fileDir = pwd + "/scripts/LOG/"
fileName = today + ".txt"
fileFullName = fileDir + fileName

# 디렉토리 있는지 체크
if not os.path.exists(fileDir):
    os.makedirs(fileDir)

# 파일 생성되었는지 체크
writeType = "w"
if not os.path.isfile(fileFullName):   
    writeType = "w"
else:
    writeType = "a"

# 파일 생성 및 어펜드
f = open(fileFullName , writeType)
f.write("["+ tag + "]" + "["+ todayWithSecond + "]" + "-" + message + "\n")
print(  "["+ tag + "]" + "["+ todayWithSecond + "]" + "-" + message)
f.close


