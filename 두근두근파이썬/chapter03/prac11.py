import time

# 현재 시간을 가져옵니다.
current_time = time.time()

# 현재 시각과 분을 구합니다.
current_hour = int((current_time // 3600) % 24)  # 시
current_minute = int((current_time // 60) % 60)  # 분

# 결과를 출력합니다.
print("현재 시각:", current_hour, "시", current_minute, "분")
