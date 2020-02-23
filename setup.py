from setuptools import find_packages
from setuptools import setup

setup(name='mathematic',
      version='0.0.0',
      description='tests',
      author='MathewRGB',
      install_requires=['numpy>=1.9.1',
                        'pytest',
                        'scikit-image',
                        'sk-video',
                        'imageio',
                        'GitPython',
                        'click',
                        'pytube',
                        'scipy',
                        'tqdm',
                        'pandas',
                        'pytest',
                        'pydoc-markdown',
                        'pycodestyle',
                        'argparse'],
      packages=find_packages())
