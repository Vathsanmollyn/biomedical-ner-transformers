# 🧠 Pretrained Models for Biomedical NER

This directory contains references to the **pretrained transformer models** used for fine-tuning and evaluation in our Biomedical Named Entity Recognition (NER) tasks.

> ⚠️ **Note**: Due to large file sizes and licensing, the pretrained models are not stored in this repository. Instead, please download them directly from the Hugging Face Model Hub using the instructions below.

---

## 🤗 Pretrained Models Used

We rely on three state-of-the-art transformer-based models specifically pretrained on biomedical and scientific corpora:

---

### 🔬 BioBERT (v1.2)
- **Model ID**: [`dmis-lab/biobert-base-cased-v1.2`](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2)
- **Base Architecture**: BERT (base, cased)
- **Domain**: PubMed abstracts + PMC full-text articles
- **License**: Apache 2.0

#### Load via Transformers:
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")
model = AutoModel.from_pretrained("dmis-lab/biobert-base-cased-v1.2")
```

---

### 🧬 PubMedBERT
- **Model ID**: [`microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract`](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract)
- **Base Architecture**: BERT (base, uncased)
- **Domain**: PubMed abstracts (trained from scratch)
- **License**: MIT

#### Load via Transformers:
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract")
model = AutoModel.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract")
```

---

### 🧠 SciBERT
- **Model ID**: [`allenai/scibert_scivocab_uncased`](https://huggingface.co/allenai/scibert_scivocab_uncased)
- **Base Architecture**: BERT (base, uncased)
- **Domain**: Scientific publications (Semantic Scholar)
- **License**: Apache 2.0

#### Load via Transformers:
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
model = AutoModel.from_pretrained("allenai/scibert_scivocab_uncased")
```

---

## 💾 Output Directory Structure

After fine-tuning, the model checkpoints are saved in the following structure:

```
models/
├── biobert-finetuned-batch1/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── vocab.txt
│   └── ...
├── pubmedbert-finetuned-mtl/
├── scibert-finetuned-batch1/
└── ...
```

Each folder typically includes:
- `config.json`: Model architecture config
- `model.safetensors` or `pytorch_model.bin`: Model weights
- `tokenizer_config.json`, `tokenizer.json`, `vocab.txt`: Tokenizer files
- `special_tokens_map.json`: Special token mappings

---

## 📚 Citations

If you use these models in your work, please cite the corresponding papers:

### BioBERT
```bibtex
@article{lee2020biobert,
  title={BioBERT: a pre-trained biomedical language representation model for biomedical text mining},
  author={Lee, Jinhyuk and Yoon, Wonjin and Kim, Sungdong and Kim, Donghyeon and So, Chan Ho and Kang, Jaewoo},
  journal={Bioinformatics},
  year={2020},
  publisher={Oxford University Press}
}
```

### PubMedBERT
```bibtex
@article{gu2021domain,
  title={Domain-specific language model pretraining for biomedical natural language processing},
  author={Gu, Yu and Tinn, Raymond and Cheng, Hao and Lucas, Michael and Usuyama, Naoto and Liu, Xiaodong and Naumann, Tristan and Gao, Jianfeng and Poon, Hoifung},
  journal={ACM Transactions on Computing for Healthcare (HEALTH)},
  year={2021},
  publisher={ACM}
}
```

### SciBERT
```bibtex
@inproceedings{beltagy2019scibert,
  title={SciBERT: A pretrained language model for scientific text},
  author={Beltagy, Iz and Lo, Kyle and Cohan, Arman},
  booktitle={EMNLP},
  year={2019}
}
```

---

## 🙋‍♀️ Questions?

Feel free to raise an issue or discussion in the main GitHub repository if you encounter problems loading or using these models.