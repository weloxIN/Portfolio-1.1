import sys
import os

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    # демо-режим для CI/CD
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()

    if not text:
        text = "Docker DevOps Ansible Terraform Kubernetes DevSecOps"
        print(f"Demo mode. Text: '{text}'")

    result = count_words(text)
    print(f"Word count: {result}")
