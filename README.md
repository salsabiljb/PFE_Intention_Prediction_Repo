# Hand Gesture Intention Prediction

This project focuses on predicting **hand movement intentions** using multimodal **EEG & EMG** signals.  
By analyzing brain-muscle interactions, we aim to improve future works focusing on **assistive technologies, prosthetics, and human-computer interaction**.

## **Project Structure**
```
├── data/                # EEG & EMG datasets
│   ├── raw/             # Original .mat files
│   ├── processed/       # Cleaned & preprocessed data
│   └── interim/         # Intermediate transformations
│
├── notebooks/           # Jupyter notebooks for EDA, preprocessing, training
│
├── src/                 # Source code for processing & modeling
│   ├── data/            # Scripts for handling datasets
│   │   ├── convert_mat_to_numpy.py  # Converts .mat files to usable formats
│   │   └── make_dataset.py          # Dataset loading & transformation pipeline
│   │
│   ├── features/        # Feature extraction scripts
│   │   └── build_features.py
│   │
│   ├── models/          # Model training & inference scripts
│   │   ├── train_model.py
│   │   ├── predict_model.py
│   │
│   ├── visualization/   # Data visualization scripts
│   │   └── visualize.py
│
├── models/              # Saved trained models
├── reports/             # Generated analysis & results
├── docs/                # Documentation
└── README.md            # Overview of the project
```

## **Setup Instructions**

1. **Clone the repository**  
   ```bash
   git clone https://github.com/salsabiljb/PFE_Intention_Prediction_Repo.git
   cd PFE_Intention_Prediction_Repo
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

   ```

