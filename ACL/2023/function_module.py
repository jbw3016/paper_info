# load paper data from xml file
import xml.etree.ElementTree as ET
import os
import pandas as pd

def load_paper_info(data_dir, year, conference_type, target_volume_id):
    filename = f'{year}.{conference_type}.xml'
    filepath = os.path.join(data_dir, filename)    
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    paper_info ={
        'paper_id' : [],
        'paper_title' : [],
        'paper_abstract' : []
    }
    
    # select which volume should crawling
    target_volume = root.find(f'.//volume[@id="{target_volume_id}"]')
    if target_volume is not None:
        for paper_element in target_volume.findall('.//paper'):
            paper_info['paper_id'].append(paper_element.attrib['id'])
            paper_info['paper_title'].append(''.join(paper_element.find('title').itertext()).strip())
            paper_info['paper_abstract'].append(''.join(paper_element.find('abstract').itertext()).strip())
    else: print(f'Volume with id "{target_volume_id}" is not found')    
    
    paper_info = pd.DataFrame(paper_info)
    paper_info.set_index('paper_id', inplace=True)
    
    return paper_info