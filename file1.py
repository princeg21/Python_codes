from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))
room_count = Counter(rooms)
for room,count in room_count.items():
    if count == 1:
        print(room)
        break
