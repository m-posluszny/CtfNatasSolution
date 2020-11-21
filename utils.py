from IPython.core.display import display, HTML

"""
    Here are some utils created to make coding easier
    printHTML - shows pretty html in jupyter notebook
    printDICT - easy way to print dictionary
"""

def printHTML(text):
    display(HTML(text))
    
def printDICT(diction):
    if not isinstance(diction,dict):
        diction = diction.__dict__
    for key,value in diction.items():
        print(f"{key} - {value}")