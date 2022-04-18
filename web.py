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

def action_ok():
    popup('Action OK', 'Action OK text content', size=PopupSize.SMALL)

def action_cancel():
    popup('Action CANCEL', 'Action CANCEL text content', size=PopupSize.SMALL)

def show_web():
    put_grid([
        [put_markdown(r'# ... Backtesting Strategies ...')],
        [put_text('Column 1A'), put_text('Column 1B')],
        [span(put_text('Column 2A with a long string of text, will it wrap or will it go to the right. I do not kow if ths is enough text to reach the end of the line but I will try'), col=2, row=1)],
        [put_button('OK', onclick=action_ok)],
    ], cell_width="80%")

def main():
    show_web()
    

if __name__ == "__main__":
    # Use -s command line parameter to run as a web server rather than a one time web page execution
    if "-s" in sys.argv:
        start_server(main, port=8080, debug=True)
    else:
        main()

    