
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """This function will return the list of requirements.
    """
    requirement_list : List[str] = []
    
    try:
        # open and read the requirements.txt file
        with open("requirements.txt","r") as file:
            # Read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        peinr("requirements.txt file not found")
        
    return requirement_list
print(get_requirements())


setup(
    name = "AI-TRAVEL-PLANNER",
    version = "0.0.1",
    author = "DARWIN ACHARYA",
    author_email = "acharyadarwin@gmail.com",
    package = find_packages(),
    install_requires = get_requirements(),
)