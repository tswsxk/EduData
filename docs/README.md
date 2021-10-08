EduNLP document and tutorial folder
===================================

Requirements
------------
See the requirements `docs_deps` in `setup.py`:
```sh
pip install -e .[doc]
```


Build documents
---------------
First, clean up existing files:
```
make clean
```

Then build:
```
make html
```

Render locally
--------------
```
cd build/html
python3 -m http.server 8000
```
