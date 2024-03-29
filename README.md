# MAIR-G8

## Intent detection

This project consists of the following baseline systems for intent detection:

- A baseline system that, regardless of the content of the utterance, always assigns the majority class of the data. (`baseline_majority.py`)
- A baseline rule-based system based on keyword matching. (`baseline_keyword_matcher.py`)

As well as three different machine learning classifiers for intent detection:

- kNN (`ml_knn.py`)
- Logistic regression (`ml_logreg.py`)
- Linear SVC (`ml_lsvc.py`)

The table below shows the accuracy value of each of these models:

|                    | **Baseline (majority)** | **Baseline rule-based system** | **kNN model** | **Logistic regression** | **Linear SVC** |
|--------------------|-------------------------|--------------------------------|---------------|-------------------------|----------------|
| **Test accuracy**  |                   0,400 |                          0,903 |         0,962 |                   0,983 |          0,958 |
| **Train accuracy** |                   0,398 |                                |         0,968 |                   0,987 |          0,962 |

## Dialog Management

The Dialog Management System can be found in `dialogstate.py`. The user can have a conversation in the CLI with the system by running the `main.py` file. An example conversation can be executed by running the `dialogstate.py` file. The file `dialogstate_tests.py` contains test cases for all 16 provided examples. Please see the installation instructions to download the required PyPi packages (a `requirements.txt` file is included in this repo). The configuration of the Dialog Manager can be altered with the `.env` file in the root of this repository. Please note that not all options are implemented yet.

To add random antecedents to the `restaurant_info.csv` file, run the `add_columns.py` script. To add the consequents to the antecedents file, run the `add_consequents.py` script.

## State Transition Diagram

![State Transition Diagram](./images/MAIR_task_1b.png)

## Configurability

The system currently supports five configurability options:

- Printing the system utterances in all-caps
    `output_in_caps=False` (True or False)
- Maximum Levenshtein distance for filling in the slots
    `max_lev_distance=3` (integer 1 or higher)
- Insert artificial errors in preference extraction
    `insert_errors=False` (True or False)
- Use formal or informal phrases in system utterances
    `formal=False` (True or False)
- Introduce a delay before showing system responses
    `delay=0` (in milliseconds)
- Enable or disable printing of system information such as the current intent and state
    `print_info=False` (True or False)
- Whether the system utterances have a coloured output or not
    `coloured_output=True` (True or False)

These options can be altered in the `.env` file at the root of this repository.

---

The following parameters are used for the data analysis of the experiments and do not affect the system's behaviour:

- The name of the researcher conducting the experiment
    `researcher_name="Albert"` (any from: {"Albert", "Lisa", "Ruben", "Thijs"})
- The age of the participant
    `participant_age=18`  (integer, 18 and higher)

## Installation

Place the required data files in the `./data/` folder. The file `restaurant_info.csv` can be downloaded from BlackBoard. This file can be converted to `restaurant_data.csv` with the `add_columns.py` script. The `restaurant_data.csv` file is the input for the `add_consequents.py` file to add consequences, this results in the `restaurant_data_consequents.csv` file which is the input for the Dialog State program.

Install the following packages on Python 3.8+:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Development

Install the following for the correct linter and formatter:

```bash
pip install autopep8 flake8 flake8-import-order flake8-blind-except flake8-builtins flake8-docstrings flake8-rst-docstrings flake8-logging-format
python -m flake8
```

Flake8 automatically uses the arguments provided in the `tox.ini` file to check the coding style.

## Limitations

- Dontcares only work if said after states 2, 3, or 4. Preferably, the system automatically figures out to what slot dontcares belong to
- A minimal example for text-to-speech can be found in `tts.py`, this is sadly not yet implemented
- Asking the user if they would like a place with or without assigned seating is not yet implemented
- Not all options in the configuration file are implemented yet
