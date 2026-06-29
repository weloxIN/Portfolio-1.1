import sys

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()
    
    if not text:
        print("Usage: echo 'some text' | python wordcounter.py")
        sys.exit(1)
    
    result = count_words(text)
    print(f"Word count: {result}")
