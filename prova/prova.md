### NAMED TUPLE

```
Acao = namedtuple('Acao', ['simbolo', 'atual', 'menor', 'maior'])
return Acao(simbolo=simbolo, atual=atual, menor=menor, maior=maior)
```

### MAKE DATACLASS

```
Acao = make_dataclass("Acao", [("simbolo", str), ("atual", float), ("menor", float), ("maior", float)])
return Acao(simbolo=simbolo, atual=atual, menor=menor, maior=maior)
```

### DATACLASS

```
@dataclass
class Acao:
  simbolo: str
  atual: float
  menor: float
  maior: float
return Acao(simbolo,atual,menor,maior)
```

### SEM NADA

```
return {'simbolo': simbolo, 'atual': atual, 'menor': menor, 'maior': maior}
```
