# LLAPRAG: Llama-Paper for RAG

## Install

`hatch env create`

`hatch build`

## LLM

### Ollama

#### Download llama3 model

```bash
curl http://localhost:11434/api/pull -d '{
  "name": "llama3"
}'
```

#### List your models

```bash
curl http://localhost:11434/api/putags
```