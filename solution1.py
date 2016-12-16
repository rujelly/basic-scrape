'''
This file finishes the solution we started that used findChildren
'''
from bs4 import BeautifulSoup


def main():
    soup = BeautifulSoup(open('index.html'), 'lxml')
    ul = soup.find(id='root')
    li = ul.findChildren('li')
    nums = []
    for element in li:
        if 'ul' in str(element):
            continue
        nums.append(int(element.get_text()))
    print(nums)
    print(sum(nums))
    
if __name__ == '__main__':
    main()