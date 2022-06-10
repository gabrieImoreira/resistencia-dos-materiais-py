# resistencia-dos-materiais-py - Projeto para o curso de Engenharia Elétrica da Universidade São Judas Tadeu

Esse projeto utiliza a lib PyQT5 para a interface gráfica e a lib Matplotlib para a criação dos gráficos.

Para rodar o programa é necessário instalar o python na máquina, através dos links:

Linux/Mac - https://python-guide-pt-br.readthedocs.io/pt_BR/latest/starting/install3/linux.html

Windows - https://www.python.org/downloads/

Após o download, é necessário instalar um editor de texto a sua escolha. 
Esse projeto inclui algumas bibliotecas e para instalá-las é necessário ir no seu bash ou Power Shell(Windows) e realizar 
a instalação das bibliotecas através do gerenciador de pacotes pip:

```
>$ pip install matplotlib
>$ pip install pyqt5
```
Feito isso, digitar no terminal o comando para executar o programa:

```
>$ python3 main.py
```

### Estrutura do código

```
├── venv
├── layouts
|   └── guindaste.png
│   └── layout.py
├── application.py
├── main.py
```

onde:

- `venv`: Ambiente virtual do python
- `layouts/`: Pasta contendo a imagem utilizada do programa e o arquivo .py de interface gráfica
- `application.py`: Arquivo contendo as classes e funções de cálculo do programa
- `main.py`: arquivo executável


### Imagens do programa:
![Text](https://github.com/gabrieImoreira/resistencia-dos-materiais-py/blob/main/layouts/calculos-programa.jpg)
![Text](https://github.com/gabrieImoreira/resistencia-dos-materiais-py/blob/main/layouts/graficos-programa.jpg)
