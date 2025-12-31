# A가 영어 단어를 1개 생각한다.
word = "man"
word = word.upper()
print(word)

# 단어의 글자 수 만큼 밑줄을 긋는다.
word_show = "_"*len(word)
print(word_show)

try_num = 0
ok_list = []
no_list = []

while True:
    # B가 단어에 포함될 것 같은 알파벳을 1개씩 제시한다.
    ans = input().upper()
    print(ans)

    # 알파벳이 단에에 포함된다면 밑줄에 알파벳을 채워 놓고
    # 포함되지 않는다면 사람을 1획 씩 그린다.
    result = word.find(ans)
    print(result)
    if result == -1: # 없음
        print("단어에 포함되지 않습니다.")
        try_num += 1
        no_list.append(ans)
    else: # 있음
        print("단어에 포함됩니다.")
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i+1:]
                
        print(word_show)

    # 사람이 먼저 완성됨녀 출제자 A가 승리하고
    if try_num == 7 : break
    
    # 단어가 먼저 완성되면 단어를 맞힌 B가 승리한다.
    if word_show.find("_") == -1 : break