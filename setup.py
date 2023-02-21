import setuptools

def load_requirements(file_list=None):
    if file_list is None:
        file_list = ['requirements.txt']
    if isinstance(file_list,str):
        file_list = [file_list]
    requirements = []
    for file in file_list:
        with open(file, encoding='utf-8-sig') as f:
            requirements.extend(f.readlines())
    return requirements

def readme():
    with open('README.md', encoding='utf-8-sig') as f:
        README = f.read()
    return README

PACKAGE_VERSION = '0.0.1'

setuptools.setup(
    name = 'easy-paddle-ocr',
    packages = setuptools.find_packages(),
    package_data = {
      'easy_paddle_ocr.algorithm.weights': ['*']
    },
    version = PACKAGE_VERSION,
    license='Other/Proprietary License',
    description = 'Theos AI',
    author = 'Theos AI',
    author_email = 'contact@theos.ai',
    url = 'https://theos.ai',
    keywords = ['theos'],
    install_requires=load_requirements(['requirements.txt']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3'
    ]
)