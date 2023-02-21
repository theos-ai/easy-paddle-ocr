import setuptools

def load_requirements():
    with open('./requirements.txt') as f:
        return f.read()

def load_readme():
    with open('./README.md') as f:
        return f.read()

PACKAGE_VERSION = '0.0.1'

setuptools.setup(
    name = 'easy-paddle-ocr',
    packages = setuptools.find_packages(),
    package_data = {
      'easy_paddle_ocr.algorithm.weights': ['*']
    },
    version=PACKAGE_VERSION,
    license='Other/Proprietary License',
    description='This a clean and easy-to-use implementation of Paddle OCR. Made with ❤️ by Theos AI.',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    author = 'Theos AI',
    author_email = 'contact@theos.ai',
    url = 'https://theos.ai',
    keywords = ['theos'],
    install_requires=load_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3'
    ]
)