# Run the formatter
format:
    uv run ruff check --select I --fix

run:
    uv run ./src/main.py -f ./src/data/test2.xlsx

