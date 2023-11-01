# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')





# markdown 연습하기
st.header('Header: 데이터 분석 표현')
st.subheader('Subheader: 스트림릿')
st.text('Text: this is the steamlit')
st.caption('Caption: streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹 애플리케이션이다') 
st.write('# Markdown 1st')
st.write('## Markdown 2nd')
st.write('### Markdown 3rd')
st.write('**_Markdown 진하고 기울임_**')
st.write('- Markdown 글머리 기호')



# Latex & Code 연습하기
st.code('x=1234')
st.markdown('## Code & Latex')
st.latex(r''' a+ar+ar^2+ae^3''')



# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame({'이름':['홍길동', '김사랑', '일지매', '이루리'], '수준':['금', '동', '은', '은']} )
st.write(df, '스트림릿의 write 함수로 표현')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py
# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')





# markdown 연습하기
st.header('Header: 데이터 분석 표현')
st.subheader('Subheader: 스트림릿')
st.text('Text: this is the steamlit')
st.caption('Caption: streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹 애플리케이션이다') 
st.write('# Markdown 1st')
st.write('## Markdown 2nd')
st.write('### Markdown 3rd')
st.write('**_Markdown 진하고 기울임_**')
st.write('- Markdown 글머리 기호')



# Latex & Code 연습하기
st.code('x=1234')
st.markdown('## Code & Latex')
st.latex(r''' a+ar+ar^2+ae^3''')

st.markdown("지도 2")

html = """<!DOCTYPE html>
<html>
<head>

<title>네이버 기본지도</title>

</body>
</html> """
