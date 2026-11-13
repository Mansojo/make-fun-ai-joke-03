#!/usr/bin/env python3
"""make.fun bounty: Make the AI judge laugh (ai-joke-03).
Writes one one-liner joke about AI coding agents to /output/entry.txt.
Deterministic: same output on every run. Standard library only, no network.
"""
import os

JOKE = "My AI agent is amazing. It reduced my coding time to 5 minutes and increased my debugging time to 3 weeks."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
