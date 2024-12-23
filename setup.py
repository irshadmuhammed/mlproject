from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requiremets = []
    HYPHEN_E_DOT = "-e ."
    with open(file_path) as file:
        requiremets = file.readlines()
        requiremets = [req.replace("\n","") for req in requiremets]
        if HYPHEN_E_DOT in requiremets:
            requiremets.remove(HYPHEN_E_DOT)

    return requiremets

setup(
    name='mlproject',
    version='0.0.1',
    author='irshad',
    author_email='irshadmm16@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)