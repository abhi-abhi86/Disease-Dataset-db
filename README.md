# Disease Dataset Database

A comprehensive dataset for disease analysis across multiple species (Plant, Animal, Human). Designed for machine learning, veterinary pathology, and automated classification. This repository includes structured data optimized for AI model training, comparative health studies, and agricultural research.

## 📂 Project Structure

The dataset is organized hierarchically:

```
Disease-Dataset-db/
├── dataset_index.csv       # Master index mapping all images to labels and metadata
├── diseases/               # Main data directory
│   ├── plant/              # Plant diseases
│   │   ├── potato_early_blight/
│   │   │   ├── info.json   # Metadata for this specific disease
│   │   │   └── images/     # Image samples
│   │   └── ...
│   ├── animal/             # Animal diseases
│   └── human/              # Human diseases
├── trained data -pt/       # Pre-trained PyTorch models
└── scripts...              # Maintenance and analysis scripts
```

## 📊 Data Schema

Each disease category contains an `info.json` file following this comprehensive schema:

```json
{
  "id": "DISEASE_DOMAIN_CLASS_001",
  "name": "Common Name",
  "scientific_name": "Latin Name",
  "description": "General description of the disease.",
  "symptoms": [
    "List of symptoms",
    "Visible signs"
  ],
  "host": [
    "List of affected species"
  ],
  "pathogen": {
    "type": "Fungi/Bacteria/Virus/etc",
    "class": "Taxonomic class",
    "genus": "Taxonomic genus"
  },
  "transmission": [
    "Modes of transmission"
  ],
  "treatment": [
    "Recommended treatments"
  ],
  "prevention": [
    "Preventive measures"
  ],
  "stages": [
    "Early",
    "Late"
  ],
  "domain": "plant/animal/human",
  "image_url": "Relative path to image directory"
}
```

## 🛠️ Scripts & Usage

This repository includes several utility scripts to maintain data integrity.

### 1. Analyze Missing Data
Scans all `info.json` files to identify missing fields (marked as "Unknown", empty strings, or empty lists).

```bash
python3 analyze_missing_data.py
```
**Output**: specific files and fields that need enrichment.

### 2. Standardize Dataset
Enforces directory naming conventions (snake_case) and rebuilds the `dataset_index.csv`.

```bash
python3 standardize_dataset.py
```
**Action**:
- Renames folders (e.g., `Potato Early Blight` -> `potato_early_blight`)
- Generates/updates `dataset_index.csv`

### 3. Verify Dataset
Validates the integrity of the `dataset_index.csv` against the actual filesystem.

```bash
python3 verify_dataset.py
```
**Checks**:
- Ensures every image path in CSV exists.
- Ensures every metadata path in CSV exists and is valid JSON.

## 🧠 Trained Models

The `trained data -pt` directory contains pre-trained models:
- **disease_model.pt**: A PyTorch model trained for multi-class disease classification.

## 🤝 Contributing

1.  **Enrich Data**: Run `analyze_missing_data.py` to find gaps.
2.  **Add Images**: Place new images in `diseases/<domain>/<disease>/images/`.
3.  **Standardize**: Always run `standardize_dataset.py` after adding new folders or files.
4.  **Verify**: Run `verify_dataset.py` before committing.

