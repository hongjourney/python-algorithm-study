def digits_to_words(input_string):
    """
    인풋으로 받는 스트링에서 숫자만 추출하여 영어 단어로 변환하여 단어들이 연결된 스트링을 반환함
    아래의 요건들을 충족시켜야함
    * 반환하는 단어들은 영어 소문자여야함
    * 단어들 사이에는 띄어쓰기 한칸이 있음
    * 만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환함
        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
            ex - "Zip Code: 19104"
        Returns:
            digit_string (string): 위 요건을 충족시킨 숫자만 영어단어로 추출된 string
            ex - 'one nine one zero four'
        Examples:
            >>> import text_processing2 as tp2
            >>> digits_str1 = "Zip Code: 19104"
            >>> tp2.digits_to_words(digits_str1)
            'one nine one zero four'
            >>> digits_str2 = "Pi is 3.1415..."
            >>> tp2.digits_to_words(digits_str2)
            'three one four one five'
    """
    digit_string = None
    string_to_iter = iter(input_string)
    num_to_string  = []
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(input_string)):
        word = next(string_to_iter)
        if word.isdigit():
            num_to_string.append(num[int(word)])
    digit_string = ' '.join(num_to_string)
    
    return digit_string
