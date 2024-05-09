import xml.etree.ElementTree as ET
'''
ElementTree: 전체 xml 문서를 트리로 표현
ET.parse('example.xml'): 'example.xml' 파일을 parsing
'''
import os

data_dir = r'C:\Users\원종복\Desktop\paper_list\acl\acl-anthology\data\xml'
year = 2023
conference_type = 'acl'

# dataframe 형식으로 반환
def load_paper_info(data_dir, year, conference_type):
    filename = f'{year}.{conference_type}.xml'
    filepath = os.path.join(data_dir, filename)
    
    tree = ET.parse(filepath)
    root = tree.getroot()
            
    title_info = [root.findtext('.//title')]
    abstract_info = [root.findtext('.//abstract')]
    
    return title_info, abstract_info
    
title_info, abstract_info = load_paper_info(data_dir=data_dir, year=year, conference_type=conference_type)
print(f'title_info:\n{title_info}')
print()
print(f'abstract_info:\n{abstract_info}')