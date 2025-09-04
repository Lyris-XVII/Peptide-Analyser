## Peptide Analyser
#### Video Demo: https://youtu.be/dNPWmFx69lU?si=9fpWfir0Nrt_R7Bj

## Overview
Peptide Analyser is a Python program that makes exploring peptides and amino acids easy
and interactive. Whether you're a student, researcher, or just curious about biochemistry,
this tool helps you understand peptide properties without any hassle.

You can choose between two main modes: analysing a full peptide chain or looking at a single
amino acid. The program guides you with a simple menu and clear instructions at every step.
If you enter something wrong, it’ll gently prompt you to try again.

To make things a bit more fun, it shows ASCII art titles using `pyfiglet` and displays all
results in neat tables with `tabulate`. It’s simple, clear, and even a little visually
pleasing.

## Peptide Chain Analysis
In peptide mode, you enter a sequence of amino acids, from just one residue up to 1000.
The program checks your input and only accepts standard amino acids, letting you correct
any mistakes.

Once your sequence is valid, Peptide Analyser calculates a few key properties:

- **Molecular Weight** – gives an idea of how heavy the peptide is in Daltons.
- **Hydrophobicity** – shows how water-repellent the peptide is, using the Kyte–Doolittle scale.
- **Residue Composition** – the percentage of each amino acid in the chain, which helps you
  understand its makeup.

Everything is shown in a clean table, so you can easily read it, compare values, or copy
the data somewhere else for further analysis.

## Residue Analysis
If you just want info about a single amino acid, residue mode has you covered. Enter the full
name, and the program will give you:

- **One-letter Code**
- **Molecular Weight**
- **Estimated Hydrophobicity**
- **Isoelectric Point**

It’s great for students learning about amino acids or researchers who need quick info without
analysing a whole peptide.

## Features
- Choose between peptide chain or residue analysis
- Handles all input carefully to avoid errors
- Calculates molecular weight, hydrophobicity, and residue composition
- Fun ASCII art titles with `pyfiglet`
- Clean tables with `tabulate`
- Works with chains up to 1000 residues
- Friendly error handling to keep things smooth

## Requirements
- Python 3
- `tabulate` library
- `pyfiglet` library

## Usage
Run the program from the terminal:

## Purpose
Peptide Analyser shows how Python can be used in biochemistry. It’s both practical and
educational, helping you calculate important peptide properties quickly and easily.

It’s perfect for students, teachers, and researchers. By exploring peptides and amino acids,
you’ll get a better understanding of biochemistry, and see how programming can make science
more approachable.

