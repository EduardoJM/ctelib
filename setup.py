from setuptools import setup, find_packages

setup(
    name='ctelib',
    version='0.1',
    author='Eduardo Oliveira',
    author_email='eduardo_y05@outlook.com',
    url='https://github.com/EduardoJM/ctelib',
    description='ctelib: Conhecimento de Transporte Eletrônico library for Brazil',
    long_description=open('README.md').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'lxml',
        'six',
    ],
    keywords='CT-e',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    zip_safe=False,
)
