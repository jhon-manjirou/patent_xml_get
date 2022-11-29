from bs4 import BeautifulSoup as bs
import unicodedata

def get_soup(file): #スープ生成
  with open(file)as f:
    data = f.read()
    soup = bs(data, 'lxml')
    return soup

def get_title(soup):  #発明の名称を取得
  return soup.find('invention-title').get_text()

def get_number(soup): #特許の特開(公開番号)を取得
  return soup.find('doc-number').get_text()

def get_ipc(soup):  #特許の分類番号
  return soup.find('main-clsf').get_text()

def get_kind(soup): #文書の分類を取得
  return soup.find('kind').get_text()

def get_desc(soup): #特許の要約を取得
  return soup.find('description').get_text()

soup = get_soup(file)

print(get_title(soup))
print(get_number(soup))
print(get_ipc(soup))

unicodedata.normalize('NFKC', get_desc(soup))   #文字列の正規化