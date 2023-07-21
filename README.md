# Projetos do primeiro curso de IA da Alura
Os projetos estão separados em branches e a branch main espelha o estado final dos projetos à conclusão do curso.

## Preparando o ambiente

1. Clone esse repositório:
```
git clone git@github.com:BrunoDivino/3260-projetos-curso-IA.git
```
ou
```
git clone https://github.com/BrunoDivino/3260-projetos-curso-IA.git
```

2. Crie um Ambinete Virtual em Python

No Linux:
```
python3 -m venv .venv
```

No Windows:
```
python -m venv .venv
```

3. Ative o ambiente virtual

No Linux:
```
source .venv/bin/activate
```
No Windows:
```
.venv\Scripts\Activate
```

4. Instale todas as bibliotecas prerequisitos
```
pip install -r requirements.txt
```

5. Crie um arquivo `.env` para armazenar a sua key da OpenAI. Siga o seguinte o padrão:
```
OPEN_AI_API_KEY={sua key aqui}
```
