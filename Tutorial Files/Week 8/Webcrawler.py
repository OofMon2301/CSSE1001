from html.parser import HTMLParser
import urllib, urllib.request


# Write the LinkParser class here
class LinkParser(HTMLParser):
    def __init__(self):
        # Create a list so it can be accessed outside of the class
        self.links = []
        # Call the __init__ method of the parent class
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    print(value)

    def get_urls(self, tag, attrs):
        # puts all www. and http:// links into a list
        for link in self.links:
            if link.startswith("www.") or link.startswith("http://"):
                self.links.append(link)
        return self.links


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
    # return the hrefs as a list
    return parser.get_urls("a", "href")


find_links("https://www.google.com.au")
