from setuptools import setup, find_packages

setup(
    name="clashroyaleapi",
    version="0.1.0",
    packages=find_packages(),
    author="Tung-Yueh Lin",
    author_email="tungyuehlin@gmail.com",
    description='Command-line interface of Clash Royale API',
    install_requires=[
        'requests',
    ],
    extras_require={
        'travis': ['pycodestyle', 'pylint']
    }
)