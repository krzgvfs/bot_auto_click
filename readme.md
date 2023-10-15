## Bot to Auto Click

Exemplo de algoritimo para automatização de tarefas baseado em reconhecimento de imagens.

![Imagem de apresentação do software](src/Screenshot_1.png)


### Instalação

**Windows**

Abra o PowerShell, navegue até a pasta do projeto e digite os comandos a seguir.

```powershell
py -m venv app_env                      \
.\app_env\Scripts\Activate.ps1          \
py -m pip install -r requeriments.txt   
```

<br>

**Linux**

Abra um terminal, navegue até na pasta do projeto e digite os comandos a seguir.

```bash
python3 -m venv app_env                      \
chmod +x /app_env/Scripts/activate           \
source /app_env/Scripts/activate             \
python3 -m pip install -r requeriments.txt   
```

## Configuração

Configure sua imagem alvo na pasta do projeto, os formatos aceitos são ```.png``` e ```.jpg``` e realizei a substituição do caminho para a mesma na variavel a seguir no arquivo ```main.py```.

```python
coordenadas = ScreenManager.get_all_matches_by_image("caminho-para-a-sua-imagem.png")
```

## Licença

MIT License

Copyright (c) 2023 Marcos André

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
