# COMP-5370

## Reading File from the command line

### Usage


```bash
python3 nosjParser.py <filename>
```

### Python implementation

```python
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No file specified")

    fileToRead = sys.argv[1]
    print("Reading file: " + fileToRead)
    with open(fileToRead, 'r') as file:
        for line in file:
            print(line)
```

### Output

Link: [This video](https://www.youtube.com/watch?v=iiADhChRriM)