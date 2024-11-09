"""
Functions

simple:
def simple_function():
    #Do this
    #Then do this
    #Finally do this

simple_function()

with inputs:
def simple_function(something):
    #Do this with something
    #Then do this
    #Finally do this

simple_function(123)

with outputs:
def simple_function(something):
    return 1 + 1

output = simple_function()

"""

# tasks


def format_name(f_name: str, l_name: str) -> str:
    f_name = f_name.title()
    l_name = l_name.title()

    return f"{f_name} {l_name}"


formated_strig_result = format_name("wIlLiaN", "sAntOS")
print(formated_strig_result)

