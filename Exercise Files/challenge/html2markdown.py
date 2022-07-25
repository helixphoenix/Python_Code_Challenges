
import markdownify

def html2markdown(html):

    h = markdownify.markdownify(html)
    
    return print(h)


html2markdown("<strong>This text is important!</strong>")