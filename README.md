# Multi-Armed Bandit Algorithms: Implementation & Analysis

A comprehensive implementation and analysis of state-of-the-art multi-armed bandit algorithms, exploring the fundamental exploration-exploitation tradeoff in reinforcement learning.

## Overview

This project implements and analyzes three fundamental bandit algorithms with rigorous theoretical foundations, demonstrating sublinear regret bounds and optimal convergence properties. The implementation extends beyond classical settings to handle faulty observations and multi-instance bandit problems.

## Theoretical Foundations

### Implemented Algorithms

#### 1. Upper Confidence Bound (UCB)
Achieves \(O(\log T)\) regret bound through optimistic exploration. The selection criterion balances exploration bonus with empirical mean estimation:

\[UCB_t(a) = \hat{p}_a + \sqrt{\frac{2\ln t}{n_a}}\]

#### 2. Kullback-Leibler UCB (KL-UCB)
Provides tighter regret bounds using KL-divergence. The selection criterion maximizes over possible reward distributions while respecting information-theoretic constraints:

\[\max_q \left\{ q : KL(\hat{p}_a, q) \leq \frac{\ln t + c\ln\ln t}{n_a} \right\}\]

This approach is computationally intensive but delivers superior performance in practice through binary search implementation for efficient UCB computation.

#### 3. Thompson Sampling
Bayesian approach using Beta distribution posteriors: \(Beta(\alpha = s_t(a) + 1, \beta = f_t(a) + 1)\). This method naturally balances exploration and exploitation through probabilistic sampling and demonstrates robustness to faulty observations.

## Project Structure

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
bash create_venv.sh
source venv/bin/activate

Install required packages
pip install -r requirements.txt

text

## Running the Code

### Test Individual Algorithms (Task 1)

Test UCB algorithm
python autograder.py --task 1 --algo ucb

Test KL-UCB algorithm
python autograder.py --task 1 --algo klucb

Test Thompson Sampling
python autograder.py --task 1 --algo thompson

Test all Task 1 algorithms
python autograder.py --task 1 --algo all

### Test Faulty Bandit Algorithm (Task 3)

python autograder.py --task 3

text

### Test Multi-Bandit Algorithm (Task 4)

python autograder.py --task 4

text

### Run All Tests

python autograder.py --task all

Please refer to report.pdf for further inputs on the analysis based on the graphs.

