# Disease-Dataset-db
A comprehensive dataset for disease analysis across multiple species. Designed for machine learning, veterinary pathology, and automated classification. Includes structured data optimized for AI model training, comparative health studies, and agricultural research using TensorFlow or PyTorch

## Dataset Contents

The dataset is organized into three main categories:

### 1. Plant Diseases
A wide variety of crops and conditions, including:
*   **Tomato**: Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, Tomato Yellow Leaf Curl Virus, Tomato mosaic virus, and Healthy samples.
*   **Potato**: Early blight, Late blight, Healthy.
*   **Pepper (Bell)**: Bacterial spot, Healthy.
*   **Others**: Areca nut, Citrus canker, Powdery mildew, Rose black spot.

### 2. Animal Diseases
*   Lumpy Skin Disease
*   Sarcoptic Mange
*   Sheep Pox
*   Swine Erysipelas

### 3. Human Diseases
*   Acne Vulgaris
*   AIDS
*   Eczema
*   Smoker's Lung
*   Vitiligo

## Recent Updates
- **2026-01-19**: Large-scale dataset expansion merged into `main` via Pull Request #1. Included handling of large image datasets through batched commits.


## Trained Models

The repository includes a `trained data -pt` directory which houses the pre-trained models:

- **disease_model.pt**: A serialized PyTorch model containing weights and architecture for disease classification. This model can be loaded to make predictions using the dataset.

## Future Plans
We are actively working on collecting and labeling more disease data. Expect updates with additional disease categories and samples in the upcoming days.
