# numeral-to-int

Convert Roman numerals to an integer.

I wrote this as a simple coding excercise and to practice TDD.

## How to use

### Shell

```sh
uv run parse IX
# 9
```

### Python

```python
from numeral_to_int.parser import parse

print(parse("IX"))
# 9
```

## Developer

### Run tests
```sh
uv run -- pytest
```