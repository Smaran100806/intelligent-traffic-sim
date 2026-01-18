# config.py
# Configuration constants for priority calculation and signal timing

# Priority weights
ALPHA = 3   # Vehicle count weight
BETA = 2    # Waiting time weight
GAMMA = 1   # Red cycle penalty weight

# Signal timing (for later use / extension)
BASE_GREEN_TIME = 10
MAX_GREEN_TIME = 60
