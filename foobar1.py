import string

def solution(x: str) -> str:
    '''
    Decrypt encrypted string
    input: str
    return: str
    '''
    result = ''
    for char in x:
      if 'a' <= char <= 'z':
        result += chr(122-ord(char)+97)
      else:
        result += char
    

    return result

print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))

