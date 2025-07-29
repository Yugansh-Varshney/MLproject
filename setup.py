from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts]

        if HYPHEN_E_DOT in requiremnts:
            requiremnts.remove(HYPHEN_E_DOT)

    return requiremnts


setup(
    name='MLproject',
    version='0.0.1',
    author='Yugansh',
    author_email='yuganshvarshney@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)