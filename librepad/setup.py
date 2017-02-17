from distutils.core import setup

setup(
    name='librepad',
    version='1.0',
    author='Rishav Kundu',
    author_email='rishav.kundu98@gmail.com',
    url='https://rishav.js.org/librepad',
    license='MIT',
    description='Server code for librepad',
    py_modules=['librepad'],
    install_requires=[
          "Flask>=0.12",
      ],
)
