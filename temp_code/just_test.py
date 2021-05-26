import pymysql
import time
import json

# 결과 저장소 : 지금은 dict 마지막에 전달할때만 json
result_data = {'time' : '1111-22-33 44:55:66'}
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
result_data['time'] = now_time

result_data['plant'] = 'test_plant2'
result_data['temperature'] = 23
result_data['humidity'] = 24
result_data['illuminance'] = 25.2

# 시간 입력 제대로 됬는지 확인
if result_data['time'] == '1111-22-33 44:55:66':
    print("현제시간 dict입력 실패!")

print(result_data)

# 전달을 위해 dict => json 으로 형 변환
json_insert_data = json.dumps(result_data)
print(result_data)

