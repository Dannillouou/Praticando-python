### venv
criar python venv: python -m venv .venv
ativar python venv's: .\.venv\Scripts\activate

### Sphinx
sphinx é um gerador de documentação para python que te permite criar htmls facilmente para documentar seu código python. usamos o sphinx dentro de uma pasta docs no projeto, e é importante lembrar de configurá-lo para acessar a pasta onde os códigos estão salvos

### Mypy
mypy é um checador de código estático que analisa o código para erros que poderiam acontecer em tempo de interpretação.
Quando rodamos o mypy, ele percorre o código sem tentar interpretá-lo (no sentido de transformar em linguagem de máquina para ser rodado) e por isso consegue encontrar erros que aconteceriam enquanto o código estivesse sendo rodado sem que precisemos rodar o código
rodamos o mypy como se rodassemos um arquivo python com python