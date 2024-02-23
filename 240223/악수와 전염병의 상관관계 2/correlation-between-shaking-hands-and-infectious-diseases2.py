developer_count, possible_infection, first_corona_developer, handshake_count = map(int, input().split())
informations = [ 
  [0] * 0 for i in range(251)
]

for _ in range(handshake_count):
  temp = tuple(map(int, input().split()))
  informations[temp[0]] = temp



developer_list = ["none"]
for _ in range(developer_count):
  developer_list.append(0)

developer_list[first_corona_developer] = 1

infected_developer = {}
infected_developer[str(first_corona_developer)] = possible_infection

for information in informations:
  if not information:
    continue
  x = str(information[1])
  y = str(information[2])
  # x, y 가 map에 존재하지 않을 시 continue
  if not x in infected_developer and not y in infected_developer:
    continue
  # x, y 둘중 하나라도 map에 존재시 존재하는 키는 값을 -1 해주고 존재하지 않는 키는 맵에 추가 해주며 값은 possible_infection으로 초기화
  # 맵에 존재하는 키 값에 해당하는 인덱스로 developer_list에 1 할당
  if x in infected_developer or y in infected_developer:
    # x 만 존재하는 경우
    if x in infected_developer and not y in infected_developer:
      if infected_developer[x] > 0:
        infected_developer[x] -= 1
        infected_developer[y] = possible_infection
        developer_list[int(y)] = 1
    # Y 만 존재하는 경우
    elif y in infected_developer and not x in infected_developer:
      if infected_developer[y] > 0:
        infected_developer[y] -= 1
        infected_developer[x] = possible_infection
        developer_list[int(x)] = 1
    # x,y 둘다 존재하는 경우
    elif x in infected_developer and y in infected_developer:
      infected_developer[x] -= 1
      infected_developer[y] -= 1

del developer_list[0]
print(''.join(map(str, developer_list)))