from html.parser import HTMLParser
import urllib
import urllib.request


# Write the LinkParser class here
class LinkParser(HTMLParser):
    
    def __init__(self):



def find_links(url):
    """Return a list of links from the given Web page.
    Return:
    (list[str]): List of all links found at the given URL.
    """
    # Open the Web page and read the HTML text
    fd = urllib.request.urlopen(url)
    text = fd.read()
    fd.close()
    
    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(str(text))  # Need to convert text to a str as read gives a
    # bytes type which feed cannot process
    # Write a return statement here
    return 
