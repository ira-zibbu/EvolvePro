#!/usr/bin/env python3
"""
Accept the path to a fasta file, and generate embeddings for each single aa mutant
"""

""" imports """
import argparse

__author__ = "Ira Zibbu"
__version__ = "0.1.0"

""" Accepts args """
parser = argparse.ArgumentParser(description='Accept the path to a fasta file, and generate embeddings for each single aa mutant')
parser.add_argument('--file', help='Path to wt fasta sequence')
parser.add_argument('--output', help='Path to write out the fasta file of mutants to')


def generate_mutants_and_wildtype_fasta(file,output):

    """
    Write a fasta file for all single aa mutants
    Args:
        file: path to the wt fasta file
        output: path to the output fasta file to write to
    Returns:
        None
    Raises:
        None
    """
    from evolvepro.src.process import generate_single_aa_mutants
    generate_single_aa_mutants(file, output_file=output)

def main(file,output):

    generate_mutants_and_wildtype_fasta(file,output)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.file, args.output)
