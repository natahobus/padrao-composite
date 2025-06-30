
# 🧩 Padrão de Projeto: Composite

Este projeto tem como objetivo demonstrar o funcionamento do padrão de projeto **Composite**, utilizando como exemplo um **sistema de arquivos** com pastas e arquivos. A ideia é comparar uma solução sem o uso do padrão com uma solução utilizando o padrão Composite.


## 🎯 Objetivo

- Estudar o padrão Composite (GoF)
- Comparar uma implementação **sem** o padrão e **com** o padrão
- Entender os benefícios e limitações de cada abordagem

## 📁 Estrutura do Projeto

```
projeto/
├── sem_composite/
│   └── sem_composite.py
├── composite/
│   └── composite.py
└── README.md
```



## 📂 Sem o Padrão Composite

### ✔️ Funcionamento

- Possui duas classes: `Arquivo` e `Pasta`
- A classe `Pasta` armazena apenas **instâncias de Arquivo**
- É necessário verificar o tipo dos objetos com `isinstance`
- Não é possível adicionar pastas dentro de pastas de forma funcional

### ⚠️ Limitações

- Estrutura rígida
- Sem suporte para hierarquia real
- Código difícil de escalar
- Uso de verificações manuais

---

## ✅ Com o Padrão Composite

### ✔️ Funcionamento

- Cria uma **interface comum** (`ItemSistema`) para arquivos e pastas
- Ambas as classes (`Arquivo` e `Pasta`) implementam essa interface
- A `Pasta` pode conter outros `ItemSistema`, inclusive outras pastas
- A exibição é recursiva e não exige verificações de tipo

### 🌳 Benefícios

- Suporte completo a hierarquias
- Uso de polimorfismo
- Código mais limpo, reutilizável e escalável


## 🧠 Conclusão

O padrão Composite é ideal para representar estruturas de dados **hierárquicas**, como sistemas de arquivos, árvores de componentes visuais, menus aninhados, entre outros. Ele permite tratar objetos simples e compostos de maneira uniforme, facilitando a manutenção e a extensibilidade do sistema.

---

## 🎬 Apresentação em Vídeo
https://youtu.be/Dbvga3hsBBo



---

## 📚 Referências

- [Refactoring Guru - Composite](https://refactoring.guru/pt-br/design-patterns/composite)
- Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John. *Design Patterns: Elements of Reusable Object-Oriented Software.*
