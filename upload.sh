#! /bin/sh
rm -fr dist
V=`tr . _ < version.txt`
for D in libs/*
do rm -fr build *.egg-info
   mkdir -p build/lib/MeCab
   cp $D/* build/lib/MeCab
   python3 setup.py bdist_wheel
   cd dist
   F=`ls -1t *.whl | head -1`
   case $F in
   mecab_cygwin-*.whl) B=`expr $F : '\(mecab_cygwin-[^-]*-\)'` ;;
   *) exit 1 ;;
   esac
   echo mv $F $B`basename $D | sed s/V/$V/`.whl | sh -x
   cd ..
done
git status
twine upload --repository pypi dist/*
exit 0
