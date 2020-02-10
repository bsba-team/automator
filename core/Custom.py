# If you want to print something customized in your terminal
# Use my custom color and fonts styles in order to print wyw
# Refer to it with this kind of formation and formulation:
# Example:
# customization.color.BOLD + "String" + customization.color.END
class Colors:

    # String to purple color
    PURPLE = '\033[95m'

    # String to cyan color
    CYAN = '\033[96m'

    # String to darkcyan color
    DARKCYAN = '\033[36m'

    # String to blue color
    BLUE = '\033[94m'

    # String to green color
    GREEN = '\033[92m'

    # String to yellow color
    YELLOW = '\033[93m'

    # String to red color
    RED = '\033[91m'

    # Make string bold
    BOLD = '\033[1m'

    # Underline string
    UNDERLINE = '\033[4m'

    # Erase all formation
    END = '\033[0m'
