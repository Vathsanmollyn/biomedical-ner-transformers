# 📁 Dataset - MTL Bioinformatics 2016

This folder is a placeholder for the **MTL-Bioinformatics-2016** datasets used for training and evaluating biomedical Named Entity Recognition (NER) models in this project.

> 📌 **Note**: Due to licensing and size constraints, the actual datasets are not included in this repository. Please follow the instructions below to download and set up the data.

---

## 📦 Dataset Source

The datasets were originally released as part of the paper:

**"Multitask learning for biomedical named entity recognition with cross-sharing structure"**  
Jingbo Shang, Jinfeng Xiao, Yanjun Ma, Xiang Ren, Yu Zhang, Jiawei Han  
[📄 Paper Link](https://www.aclweb.org/anthology/D18-1410/)  
[📂 Dataset GitHub Repo](https://github.com/cambridgeltl/MTL-Bioinformatics-2016)

---

## 📥 Download Instructions

1. Clone the official dataset repository:

```bash
git clone https://github.com/cambridgeltl/MTL-Bioinformatics-2016.git
```

2. Copy the `data/` folder into this project's `data/` directory:

```bash
cp -r MTL-Bioinformatics-2016/data ./data/
```

You should now have a structure like:

```
data/
└── 1/
    └── AnatEM-IOB/
        ├── train.tsv
        ├── devel.tsv
        └── test.tsv
...
```

---

## 🧪 Dataset Format

Each subdirectory (e.g., `AnatEM-IOB`, `BC2GM-IOBES`, etc.) contains:
- `train.tsv`: Training set
- `devel.tsv`: Development (validation) set
- `test.tsv`: Test set

Each `.tsv` file follows a token-per-line format, typically:

```
Token<TAB>Label
```

Example:
```
Tumor   B-Disease
suppressor    I-Disease
gene    O
```

---

## 📚 Supported Datasets

Some of the included datasets:
- AnatEM
- BC2GM
- BC4CHEMD
- BC5CDR (chem/disease)
- CRAFT
- GENIA
- JNLPBA
- BioNLP09/11/13
- Linnaeus
- NCBI-Disease
- Ex-PTM

Each dataset may come in multiple tag formats like **IOB** and **IOBES**.

---

## ⚠️ License

Please refer to the original [MTL-Bioinformatics-2016 LICENSE](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/blob/master/LICENSE.md) for licensing and usage restrictions.

---

## 📞 Contact

For dataset-specific issues, refer to the original repo or contact the dataset maintainers.