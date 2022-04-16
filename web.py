import sys

from turtle import delay
import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *


# pywebio.input
# pywebio.output
# pywebio.session
# pywebio.platform


def show_output_examples_page():
    # https://pywebio.readthedocs.io/en/latest/output.html
    put_text("Hello world!")

    put_table([
        ['Commodity', 'Price'],
        ['Apple', '5.5'],
        ['Banana', '7'],
    ])

    put_image(open('.\IMAGES\eyes1.png', 'rb').read())
    put_html("<br>")
    url = "https://poivronjaune.com/images/poivronjaune.png"
    put_image(url)

    put_markdown('~~Strikethrough~~')
    
    popup('popup title', 'popup text content')

    toast('New message 🔔')

    put_info('Info message')
    put_success('Succes message')
    put_warning('Warning message')
    put_error('Error message')

    close_popup()



def main():
    #print(f"Hello world!")
    show_output_examples_page()
    

if __name__ == "__main__":
    # Use -s command line parameter to run as a web server rather than a one time web page execution
    if "-s" in sys.argv:
        start_server(main, port=8080, debug=True)
    else:
        main()

    