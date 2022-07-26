
import markdownify
import re

SPACES = re.compile(r'\s+')
PARAGRAPHS = re.compile(r'<p>(.+?)</p>')
def html2markdown(html):
    if '</p><p>' not in html:
        h = markdownify.markdownify(html)
        h = SPACES.sub(r' ', h)
        return h        
 
    else:      
        html=html.split('</p><p>')
        
        if len(html)>1:
            h=''
            for i in range(len(html)):
                par=markdownify.markdownify(html[i])
                par= SPACES.sub(r' ', par)
                h=h+par+'\n\n'
        return h[:-2]   

