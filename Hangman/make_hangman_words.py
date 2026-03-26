import requests

# 1. google 10000 단어 리스트 다운로드 (욕설 제외 버전)
url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt"
response = requests.get(url)
words = response.text.lower().splitlines()

# 2. 제외할 기능어 리스트 (더 많이 추가해서 깨끗하게 만들었어요)
function_words = {
    'the', 'a', 'an', 'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'up', 'about', 'into',
    'and', 'or', 'but', 'so', 'if', 'then', 'than', 'as', 'like', 'because', 'while', 'when', 'where',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his',
    'its', 'our', 'their', 'this', 'that', 'these', 'those', 'be', 'is', 'are', 'was', 'were', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'shall', 'should',
    'may', 'might', 'must', 'not', 'no', 'yes', 'all', 'some', 'any', 'one', 'two', 'three', 'there',
    'here', 'what', 'which', 'who', 'how', 'out', 'over', 'under', 'through', 'after', 'before',
    'between', 'among', 'again', 'just', 'very', 'too', 'now', 'also', 'only', 'even', 'still'
    # 더 필요하면 여기에 추가하세요
}

# 3. 기능어 제외 + 알파벳만 + 3글자 이상
filtered_words = []
for word in words:
    if (word not in function_words and 
        len(word) >= 3 and 
        word.isalpha()):
        filtered_words.append(word)

# 4. 여기서 길이 제한 적용! (4글자 이상 ~ 10글자 이하)
filtered_words = [w for w in filtered_words if 4 <= len(w) <= 10]

# 중복 제거 + 알파벳 순 정렬
filtered_words = sorted(set(filtered_words))

print(f"원본 단어 수: {len(words)}")
print(f"필터링 후 단어 수 (4~10글자): {len(filtered_words)}")

# 파일로 저장
with open("hangman_words.txt", "w", encoding="utf-8") as f:
    for word in filtered_words:
        f.write(word + "\n")

print("hangman_words.txt 파일이 생성되었습니다!")
print("행맨 게임에 사용하기 좋은 단어들이 준비됐어요~")