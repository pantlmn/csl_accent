# csl_accent

This is a tool for putting stress marks in Church Slavonic texts in grazhdanitsa encoding

### Installation
```
pip install git+https://github.com/pantlmn/csl_accent.git@main
```
### Usage example

To put stress marks in text
```
>>> from csl_accent import accent_line
>>> accent_line('Это инструмент для разметки ударений')
Э'то инструме'нт для разме'тки ударе'ний
```

To put stress marks in files
```
>>> csl_accent.write_file(['my_file_1.txt'])
```

This will return new file called 
"my_file.accented.txt" with the same text 
where stress marks are put