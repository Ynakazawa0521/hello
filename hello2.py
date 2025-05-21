from datetime import datetime

now = datetime.now()
print("現在の時刻は:", now.strftime("%H:%M:%S"))

if now.hour < 12:
    print("おはようございます！")
else:
    print("こんにちは！")