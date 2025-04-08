# FolderTree

A simple Python utility to generate and visualize directory tree structures.

## Features

- Generates a tree-like representation of directory structures
- Saves the output to a text file
- Automatically opens the result in Notepad++ (if available)
- Handles complex directory hierarchies efficiently
- Provides clean, readable output format

## Usage

Edit the `folder_structure_to_txt.py` file to set your target directory and output file path:

```python
# Define the target directory and output file path
target_directory = r"C:\Your\Target\Directory"
output_file = r"C:\Path\To\Output\directory_tree.txt"
```

Then run the script:

```
python folder_structure_to_txt.py
```

## Installation

1. Clone this repository:
```
git clone https://github.com/PiotrPlachta/FolderTree.git
```

2. Navigate to the cloned directory:
```
cd FolderTree
```

3. Run the script after modifying the target directory:
```
python folder_structure_to_txt.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Example Output

├── GSM_Analyses
│   ├── GSM_1800
│   │   ├── AnalysisSpecification.xml
│   │   ├── GSM_1800_BestServerSS_GSM_M.TAB
│   │   ├── GSM_1800_BestServerSS_GSM_M.mrr
│   │   ├── GSM_1800_BestServerSS_GSM_M.txt
│   │   ├── GSM_1800_BestServerSS_GSM_M_mrr.ghx
│   │   ├── GSM_1800_BestServingSector_GSM_M.TAB
│   │   ├── GSM_1800_BestServingSector_GSM_M.mrr
│   │   ├── GSM_1800_BestServingSector_GSM_M.txt
│   │   └── Sectors.bin
│   ├── GSM_900
│   │   ├── AnalysisSpecification.xml
│   │   ├── GSM_900_BestServerSS_GSM_M.TAB
│   │   ├── GSM_900_BestServerSS_GSM_M.mrr
│   │   ├── GSM_900_BestServerSS_GSM_M.txt
│   │   ├── GSM_900_BestServerSS_GSM_M_mrr.ghx
│   │   ├── GSM_900_BestServingSector_GSM_M.TAB
│   │   ├── GSM_900_BestServingSector_GSM_M.mrr
│   │   ├── GSM_900_BestServingSector_GSM_M.txt
│   │   └── Sectors.bin
│   ├── GSM_900_GRID
│   │   ├── GSM_900_GRID_BestServerSS_GSM_M.TAB
│   │   ├── GSM_900_GRID_BestServerSS_GSM_M_Esri.TAB
│   │   ├── GSM_900_GRID_BestServingSector_GSM_M.TAB
│   │   └── GSM_900_GRID_BestServingSector_GSM_M.mrr
│   └── old folder
│       ├── GSM_900_GRID_BestServerSS_GSM_M.TAB
│       ├── GSM_900_GRID_BestServerSS_GSM_M_Esri.TAB
│       ├── GSM_900_GRID_BestServingSector_GSM_M.TAB
│       └── GSM_900_GRID_BestServingSector_GSM_M.mrr
├── LTEFDD_Analyses
│   └── old folder
├── LTETDD_Analyses
│   └── old folder
├── NR_Analyses
│   └── old folder
├── Node Project
│   ├── folder scanner.py
│   ├── index.js
│   ├── node_modules
│   │   ├── .package-lock.json
│   │   └── postgres
│   │       ├── README.md
│   │       ├── cf
│   │       │   ├── polyfills.js
│   │       │   └── src
│   │       │       ├── bytes.js
│   │       │       ├── connection.js
│   │       │       ├── errors.js
│   │       │       ├── index.js
│   │       │       ├── large.js
│   │       │       ├── query.js
│   │       │       ├── queue.js
│   │       │       ├── result.js
│   │       │       ├── subscribe.js
│   │       │       └── types.js
│   │       ├── cjs
│   │       │   ├── package.json
│   │       │   └── src
│   │       │       ├── bytes.js
│   │       │       ├── connection.js
│   │       │       ├── errors.js
│   │       │       ├── index.js
│   │       │       ├── large.js
│   │       │       ├── query.js
│   │       │       ├── queue.js
│   │       │       ├── result.js
│   │       │       ├── subscribe.js
│   │       │       └── types.js
│   │       ├── package.json
│   │       ├── src
│   │       │   ├── bytes.js
│   │       │   ├── connection.js
│   │       │   ├── errors.js
│   │       │   ├── index.js
│   │       │   ├── large.js
│   │       │   ├── query.js
│   │       │   ├── queue.js
│   │       │   ├── result.js
│   │       │   ├── subscribe.js
│   │       │   └── types.js
│   │       └── types
│   │           ├── index.d.ts
│   │           ├── package.json
│   │           └── tsconfig.json
│   ├── package-lock.json
│   └── package.json
├── WCDMA_Analyses
│   ├── WCDMA_900
│   │   ├── AnalysisSpecification.xml
│   │   ├── Carrier.params
│   │   ├── Clutter.params
│   │   ├── DebugParams.xml
│   │   ├── FER.params
│   │   ├── Hsdpa.params
│   │   ├── Hsupa.params
│   │   ├── LayerLimits.txt
│   │   ├── Repeater.params
│   │   ├── Runtime.params
│   │   ├── Sector.params
│   │   ├── Sectors.bin
│   │   ├── Site.params
│   │   ├── SubCat.params
│   │   ├── System.params
│   │   ├── Validation.txt
│   │   ├── WCDMA_900_BstCPHEc_8_SB1_1_M.TAB
│   │   ├── WCDMA_900_BstCPHEc_8_SB1_1_M.mrr
│   │   ├── WCDMA_900_BstEcSvr_8_SB1_1_M.TAB
│   │   ├── WCDMA_900_BstEcSvr_8_SB1_1_M.mrr
│   │   └── WCDMA_900_BstEcSvr_8_SB1_1_M.txt
│   └── old folder
└── tmp
