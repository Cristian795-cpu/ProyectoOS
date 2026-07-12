from html.parser import HTMLParser
from pathlib import Path
html = Path('stephany.html').read_text(encoding='utf-8')
class TagCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:
            return
        self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append(f'extra closing </{tag}>')
            return
        last = self.stack.pop()
        if last != tag:
            self.errors.append(f'mismatched </{tag}> expected </{last}>')
parser = TagCounter()
parser.feed(html)
print('errors:', parser.errors)
print('remaining stack top 10:', parser.stack[-10:])
