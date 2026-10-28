# API Practice

Small Python exercises on made-up data:

- Count failed requests per endpoint and sort them.
- Find where a run of successful statuses first reaches a target length.
- Combine role permissions and validate a short name.

## What you need

- Python 3 (no other packages)

## Run the tests

1. Get the code:

   ```sh
   git clone https://github.com/tony-workbench/api-practice.git
   cd api-practice
   ```

2. Run the tests:

   ```sh
   PYTHONPATH=src python3 -m unittest discover -s tests -v
   ```

## Try the functions

1. Start Python with the source folder on the path:

   ```sh
   PYTHONPATH=src python3
   ```

2. Call a function:

   ```python
   from api_practice.analysis import api_error_summary, recovery_index
   api_error_summary([("a", 200), ("b", 500), ("a", 401), ("b", 503)])  # [("b", 2), ("a", 1)]
   recovery_index([500, 200, 204, 500, 200], 2)                          # 2
   ```

Exercise notes: [LEARNING_LOG.md](LEARNING_LOG.md).
