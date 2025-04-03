# 🧬 Biomedical Named Entity Recognition with Transformers

This repository provides a unified pipeline to fine-tune multiple transformer-based models on biomedical Named Entity Recognition (NER) tasks using datasets from the [MTL-Bioinformatics-2016](https://github.com/cambridgeltl/MTL-Bioinformatics-2016) benchmark.

---

## 🚀 Models Used

The following pretrained models from [HuggingFace](https://huggingface.co) were used:
- **BioBERT** [`dmis-lab/biobert-base-cased-v1.2`](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2)
- **PubMedBERT** [`microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract`](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract)
- **SciBERT** [`allenai/scibert_scivocab_uncased`](https://huggingface.co/allenai/scibert_scivocab_uncased)

---

## 🧾 Project Structure

```
biomedical-ner-transformers/
├── data/              # Contains dataset folders and README
├── models/            # Stores fine-tuned model checkpoints and README
├── notebooks/         # Jupyter notebooks for training, prep, and exploration
├── Plots/             # Tag distribution and analysis plots
├── scripts/           # Automation and inference scripts
├── .gitignore
├── LICENSE
└── README.md          # (You're here!)
```

---

## 📦 Dataset

The dataset is not included directly here. Please download it from the original repo:

```bash
git clone https://github.com/cambridgeltl/MTL-Bioinformatics-2016.git
cp -r MTL-Bioinformatics-2016/data ./data/
```

Refer to [`data/README.md`](data/README.md) for dataset details.

---

## 📓 Fine-tuning Notebooks

Notebooks are available in the [`notebooks/`](notebooks/) directory for:
- Individual model fine-tuning (BioBERT, PubMedBERT, SciBERT)
- Hybrid transformer + BiLSTM + CRF training
- Data batching and preparation for MTL

---

## 📊 Visualization

The [`Plots/`](Plots/) folder contains per-dataset tag distribution plots, total tokens/sentences/entities, and label distributions.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Citation

If you use this repository, please cite the following models:

### BioBERT
```bibtex
@article{lee2020biobert,
  title={BioBERT: a pre-trained biomedical language representation model for biomedical text mining},
  author={Lee, Jinhyuk and Yoon, Wonjin and Kim, Sungdong and Kim, Donghyeon and So, Chan Ho and Kang, Jaewoo},
  journal={Bioinformatics},
  year={2020}
}
```

### PubMedBERT
```bibtex
@article{gu2021domain,
  title={Domain-specific language model pretraining for biomedical natural language processing},
  author={Gu, Yu and Tinn, Raymond and Cheng, Hao and et al.},
  journal={ACM Transactions on Computing for Healthcare (HEALTH)},
  year={2021}
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

## 💬 Contact

Feel free to open an issue or reach out if you have questions or would like to collaborate!
