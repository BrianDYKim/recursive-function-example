# 단방향으로 쌓이는 재귀함수 예시
def recursive(number_list):
    if len(number_list) == 5:
        return

    for i in range(5):
        if i not in number_list:
            number_list.append(i)
            print(number_list)
            recursive(number_list)


recursive([])