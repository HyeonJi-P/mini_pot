import docx
from docx.oxml.ns import qn # 한글 폰트
from docx.enum.text import WD_ALIGN_PARAGRAPH # 중앙정렬
from docx.shared import Cm, Inches # 이미지 삽입시 길이 단위

#from fpdf import FPDF
#import pandas as pd

# 0. base
'''
* 호출시 임포트
import docx
from docx.oxml.ns import qn # 한글 폰트

* 새로운 임포트 설치
pip3 install python-docx
'''

class document_make:
    # 함수종류
    ### word : docx 생성
    ### convert : docx를 pdf로 변환

    # 전체적인 구조
    ### 데이터 형식을 받아서 docx를 생성
    ### docx를 pdf로 변환해서 송신부에 전달

    @staticmethod
    def word(insert_data):
        print("START")
        doc = docx.Document()

        # ++ 다하고 변수로 다 해서 데이터 전달만 되면 바로 생성되게 만들기

        para = doc.add_paragraph()
        run = para.add_run('mini pot - title') # +본문
        run.font.size = docx.shared.Pt(30) # 폰트크기 
        run.bold = True # 볼트체 
        run.italic = True # 이텔릭체
        run.font.name = 'Cambria' # 폰트 설정
        # run._element.rPr.rFonts.set(qn('w:eastAsia'), '휴먼명조') # 한글 폰트 에러남
        last_paragraph = doc.paragraphs[-1]  # 이전 paragraph를 지정후 
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER # 중앙정렬

        # 이미지 삽입
        ### ++ 이미지의 원래 비율에 맞개 줄이는 방법을 생각해야함
        ### ++ 아니면 규격을 정해놔서 거기에 맞춰야함
        doc.add_picture("test_image.png", width = Cm(13), height = Cm(8))

        # 단락 생성
        doc.add_paragraph('첫번째 단락', style='List Bullet')
        doc.add_paragraph('첫번째 순서 단락', style='List Number')

        # https://python-docx.readthedocs.io/en/latest/
        ## 참고 후 추가
        ## ++ 헤드, 나누는선 꾸미기

        # ++ 사실상 여기에서 표를 만들면 쌩고생이기 때문에
        # 정보 가공부분에서 이미지로 가공해서 넘겨주면 여기서 그걸 사용하는게 제일 좋아보임
        # (보여주는 타입을 2개로 나누어서 일반:그래프, 고급:표 로)


        # ++파일 이름 지정
        # 년월일-시분_식물이름 ex) 210629-165300_hub
        # 나중에 가능하다면 ex) 식물애칭-time 

        doc.save("time_plant.docx") 
        print("END")

    @staticmethod
    def convert(insert_data):
        a = 1
        # docx to pdf 추후 참고
        # https://passing-story.tistory.com/228
        # https://pythonq.com/so/python/675830

# test space ----------------------------------------
''''''
document_make.word(1)
