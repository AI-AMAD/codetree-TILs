day, hour, minute = map(int, input().split())

start_time = 11*60+11
end_time = 0

day = (day-11)*60*24

hour = hour*60

end_time = day+hour+minute

if start_time > end_time:
    result = -1
else:
    result = end_time-start_time

print(result)