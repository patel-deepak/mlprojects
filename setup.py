from setuptools import find_packages,setup
from typing import List

hypen_e = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This Function will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments =file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if hypen_e in requirments:
            requirments.remove(hypen_e)
    return requirments


setup(
name='mlproject',
version='0.0.1',
author='Deepak',
author_email='deepakpatel01071983@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirments.txt')
)

