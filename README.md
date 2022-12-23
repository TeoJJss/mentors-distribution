First, you should install the dependencies in virtual environment: 
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If you would like to run the web server: 
```
flask run --reload
```
and you may upload files. 

--- 

If you would like to run the engine only: 
```
python engine.py
```
Before this, please place all input files in input folder. 
Generated output will be in the output folder