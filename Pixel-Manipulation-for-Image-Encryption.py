from pyfiglet import figlet_format
from termcolor import colored

# Print the title of the program
title = "Pixel Manipulation"
title_ascii = figlet_format(title, font="shadow", width=1000)
title_colored = colored(title_ascii, color="green")
print(title_colored)

# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="yellow")
print(creator_colored)

