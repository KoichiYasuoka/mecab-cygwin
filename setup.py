import setuptools

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/mecab-cygwin"

setuptools.setup(
  name="mecab-cygwin",
  version="0.5.0",
  description="MeCab Python for Cygwin",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="GPL",
  keywords="mecab nlp",
  packages=setuptools.find_packages(),
  install_requires=[],
  python_requires=">=3.6",
  package_data={
    "MeCab":["./mecabrc.in","./dic/*"],
  },
  classifiers=[
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Programming Language :: Python :: 3",
    "Operating System :: POSIX :: Other",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing :: Linguistic",
  ],
  project_urls={
    "mecab-python3":"https://pypi.org/projects/mecab-python3/",
    "source":URL,
    "Tracker":URL+"/issues",
  }
)
