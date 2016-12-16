'''
This file contains the solution I was getting at in the beginning, where I 
would have stripped the text of its tags, split everything, and converted
the strings to ints. I mentioned requests.text, but I actually confused
requests.text with BeautifulSoup.get_text() (which rarely behaves the way
its documentation claims it does). Anyway, here's a solution. Wouldn't be 
realistic in most production cases though, considering modern webpages.
'''
from bs4 import BeautifulSoup


def main():
    html = BeautifulSoup(open('index.html'), 'lxml')
    text = html.get_text()
    lines = text.split('\n')
    nums = [int(line) for line in lines if line]
    print(nums)
    print(sum(nums))

if __name__ == '__main__':
    main()
    