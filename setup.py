import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(setup_requires=['wheel'],
      name="seesawloss",
      version="0.1.2",
      description="pytorch implementation of seesaw loss",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/jahongir7174/SeesawLoss",
      author="Jahongir Yunusov",
      author_email="jahongir7174@gmail.com",
      license="MIT",
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.8"],
      packages=["seesawloss"],
      install_requires=["torch"])
