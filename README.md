# Skill Stella Reel

Uma skill (um "manual de instruções" para IA) que ensina o Claude e o Codex a criar reels no formato da **Stella Soragi**: o diário falado para a câmera, no estilo Yap.

Ela foi montada a partir da análise, quadro a quadro, de 32 reels da Stella: cortes, textos, fontes, posições na tela, efeitos sonoros e volumes. Com ela instalada, a IA consegue:

1. **Escrever o roteiro** de um vídeo novo no formato (gancho, episódio, provas, CTA).
2. **Montar o plano de edição** a partir dos takes gravados: onde cortar, que texto entra em cada frase, que print usar, que som tocar e em qual quadro.
3. **Revisar um vídeo pronto** e apontar o que está fora do padrão.

---

## O que vem dentro

| Arquivo | Para que serve |
|---|---|
| `stella-reel/SKILL.md` | O arquivo principal, que a IA lê primeiro |
| `stella-reel/FORMAT.md` | Todos os números medidos: câmera, cortes, textos, tamanhos, posições, sons, volumes e cor |
| `stella-reel/SCRIPT.md` | Como escrever o roteiro: tipos de vídeo, ganchos, fechamentos |
| `stella-reel/EDIT-RULES.md` | As decisões de edição frase por frase |
| `stella-reel/PLAN.md` | O modelo do plano de edição, um exemplo completo e o checklist final |
| `stella-reel/CORPUS.md` | A lista dos 32 reels analisados |
| `stella-reel/assets/style-board.jpg` | Painel com 24 quadros de referência visual |
| `stella-reel/assets/fonts/` | As 4 fontes do formato (licença livre OFL) |
| `stella-reel/assets/sfx/` | Os 6 efeitos sonoros do formato, prontos para usar |
| `stella-reel/scripts/level_sfx.py` | Script opcional que ajusta o volume dos efeitos à voz de cada vídeo |

Os arquivos de instrução estão em inglês, porque é como as IAs seguem com mais precisão. Pode conversar com a IA em português normalmente: ela responde e escreve os roteiros em português.

---

## Como instalar

Escolha onde você vai usar. Não precisa instalar nos três.

### Opção 1: Claude (site ou app claude.ai)

Funciona em qualquer plano, inclusive no gratuito.

1. Baixe o arquivo **`stella-reel.zip`** na página de [Releases](https://github.com/gabrielbuzziv/stella-reel/releases/latest). Não descompacte.
2. No Claude, abra **Configurações → Capacidades** e ative **Criação de arquivos e execução de código**.
3. Vá em **Personalizar → Skills**, clique no **+**, escolha **Criar skill** e depois **Enviar uma skill** (*Upload a skill*).
4. Selecione o `stella-reel.zip`.
5. Confira se a skill aparece na lista e está ativada.

### Opção 2: Claude Code

O jeito mais fácil é pedir para o próprio Claude Code instalar. Abra o Claude Code e cole:

```
Instale a skill do repositório https://github.com/gabrielbuzziv/stella-reel: copie a pasta stella-reel para ~/.claude/skills/stella-reel
```

Se preferir fazer à mão, rode no Terminal:

```bash
git clone https://github.com/gabrielbuzziv/stella-reel.git /tmp/stella-reel
mkdir -p ~/.claude/skills
cp -R /tmp/stella-reel/stella-reel ~/.claude/skills/
```

Feche e abra o Claude Code de novo.

### Opção 3: Codex (app do ChatGPT para computador, Codex no Terminal ou no VS Code)

Abra o Codex e cole:

```
Instale a skill do repositório https://github.com/gabrielbuzziv/stella-reel: copie a pasta stella-reel para ~/.agents/skills/stella-reel
```

Ou, à mão, no Terminal:

```bash
git clone https://github.com/gabrielbuzziv/stella-reel.git /tmp/stella-reel
mkdir -p ~/.agents/skills
cp -R /tmp/stella-reel/stella-reel ~/.agents/skills/
```

Feche e abra o Codex de novo. A skill aparece em **Skills**, na barra lateral do app.

> O ChatGPT comum (o chat no site ou no celular) ainda não aceita skills avulsas como esta. Use o Codex.

---

## Como usar

Não precisa de comando especial. Basta pedir em português e mencionar o formato. Alguns exemplos:

**Roteiro novo**
```
Quero gravar um vídeo no formato da Stella. Este mês eu vendi 120 unidades do meu curso de bolos,
sem anúncio, com 4 mil seguidores. Tenho print do painel da Hotmart. É o episódio 3 da minha série
"Como eu tô vivendo de confeitaria". Escreve o roteiro.
```

**Plano de edição**
```
Gravei os takes desse roteiro (anexo os vídeos). Monta o plano de edição no formato da Stella,
com os textos, os prints e os sons de cada frase.
```

**Revisão**
```
Revisa esse reel editado (anexo) comparando com o formato da Stella e me diz o que ajustar.
```

A IA vai pedir as informações que faltarem (números, prints, a série do vídeo) antes de escrever.

---

## Para quem edita

- **Fontes:** instale as fontes de `stella-reel/assets/fonts/` no computador ou no celular antes de editar.
- **Sons:** os arquivos de `stella-reel/assets/sfx/` já vêm com o volume certo para uma voz gravada com microfone de lapela. Importe no Edits, CapCut ou outro editor e use com volume em 100%. Se quiser o ajuste exato para a voz de um vídeo específico, peça para a IA rodar o `level_sfx.py` (precisa de `uv` e `ffmpeg`; a IA instala se você deixar).
- **Edição no Edits:** o plano de edição sai com o quadro exato de cada texto, print e som, pronto para seguir no app.

---

## Aviso

Projeto independente, sem vínculo oficial com a Stella Soragi. Os quadros e trechos de áudio de referência vêm de reels públicos dela e estão aqui apenas para estudo do formato. Use a skill para contar **a sua própria história**; não copie o conteúdo dela.

As fontes Poppins, Instrument Serif e Gochi Hand são distribuídas sob a [SIL Open Font License](stella-reel/assets/fonts/).
