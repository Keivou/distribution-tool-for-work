# Run the formatter
format:
    uv run ruff check --select I --fix

run:
    uv run main.py -f .src/data/test2.xlsx

