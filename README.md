# COMP-5370

## Reading File from the command line

### Usage


```bash
python3 nosjParser.py <filename>
```

### Python implementation

```python
def main():
    if len(sys.argv) != 2:
        print_error("Usage: python main.py input.nosj")

    input_file = sys.argv[1]
    file = open(input_file, "r")
    potentialNosjObject = file.read()
    process_nosj(potentialNosjObject)
```

### Questions 
- What should be printed if an empty map is encountered? Should it be begin-map\n -- --\n end-map\n or begin-map\n end-map\n