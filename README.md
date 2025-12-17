# Multi-Armed Bandit Algorithms: Implementation & Analysis

A comprehensive implementation and analysis of state-of-the-art multi-armed bandit algorithms, exploring the fundamental exploration-exploitation tradeoff in reinforcement learning.

Please refer to report.pdf for understanding the theory behing the algorithms and analysis based on the graphs. 

## Project Structure
```
.
├── task1.py # Core algorithm implementations (UCB, KL-UCB, Thompson)
├── task3.py # Faulty bandit algorithm
├── task4.py # Multi-bandit algorithm
├── bernoulli_bandit.py # Bernoulli bandit environment
├── faulty_bandit.py # Faulty observation environment
├── multi_bandit.py # Multi-instance bandit environment
├── autograder.py # Automated testing and evaluation
├── simulator.py # Simulation framework
├── requirements.txt # Python dependencies
├── create_venv.sh # Virtual environment setup
├── report.pdf # Detailed theoretical analysis
└── reference.txt # Academic references
```

## Key Features

### Classical Bandit Problems

- **Regret Analysis**: Empirical validation of \(O(\log T)\) regret bounds across 250,000+ timesteps
- **Mean Sensitivity**: Analysis of regret as a function of arm mean differences
- **Comparative Studies**: Head-to-head algorithm performance evaluation

### Advanced Settings

- **Faulty Bandits**: Handles environments with probabilistic observation noise
- **Multi-Bandits**: Optimizes over multiple bandit instances with random selection
- **Robust Design**: Thompson Sampling demonstrates natural immunity to fault conditions

### Empirical Validation

- Automated test suite with multiple test cases per task
- Visualization of regret curves and convergence behavior
- Pass/fail grading system for algorithm correctness

## Installation & Setup

### Prerequisites

- Python 3.7+
- NumPy
- Matplotlib

### Quick Start

Create virtual environment and install dependencies
```bash create_venv.sh```
```source venv/bin/activate```

Install required packages



```pip install -r requirements.txt```

text

## Running the Code

### Test Individual Algorithms (Task 1)

Test UCB algorithm
```python autograder.py --task 1 --algo ucb```

Test KL-UCB algorithm
```python autograder.py --task 1 --algo klucb```

Test Thompson Sampling
```python autograder.py --task 1 --algo thompson```

Test all Task 1 algorithms
```python autograder.py --task 1 --algo all```

### Test Faulty Bandit Algorithm (Task 3)

```python autograder.py --task 3```


### Test Multi-Bandit Algorithm (Task 4)

```python autograder.py --task 4```


### Run All Tests

```python autograder.py --task all```



