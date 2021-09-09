def solution(s):
    Answer = []
    temporary_string = ""
    for letter in s:
        temporary_string += letter
        if len(temporary_string) > 1:
            Answer.append(temporary_string)
            temporary_string = ""
    if len(s) % 2 == 1:
        Answer.append(s[-1]+"_")

if __name__ == "__main__":
    solution("abcdefg")
