from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='zombie_dice',
      version='0.5',
      description='Zombie Dice',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['zombie_dice'],
      author="Jacques Coetzee",
      author_email="j.coetzee0@gmail.com",
      zip_safe=False,
      url="https://github.com/feeblefruits/zombiedice",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6')
