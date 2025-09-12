import sys
import re

from tabulate import tabulate
from pyfiglet import Figlet
from amino_acids import amino_acid_data

figlet = Figlet()  # Creates an object from Figlet() class.


def main() -> None:
    try:
        print(figlet.renderText("Peptide Analyser"))  # Displays title.
        print(
            "This Analyser Will Provide Information On Multiple Features Of Your Chosen Peptide.\n\n"
            "Hydrophobicity Is Measured Using The Kyte–Doolittle Hydropathy Scale.\n\n"
            "Please Type A Peptide Chain Between 1–1000 Residues Long.\n\n"
            "For Example: 'CYIQNCPLG'.\n\n"
            "Or Research The Properties Of Individual Residues Via The Residue Analyser.\n\n"
            "Disclaimer: Hydrophobicity Scores Do Not Consider The Effects Of Protein Folding."
        )  # Displays instructions.
        user_choice: str = str(
            input("\nType '1' For Peptide Analyser. Type '2' For Residue Analyser: ")
        )  # Get choice.
        while user_choice != "1" and user_choice != "2":
            print(
                "\nPlease Choose Option '1' Or '2'."
            )  # Prompts user until valid choice.
            user_choice = str(
                input("\nType '1' For Peptide Analyser. Type '2' For Residue Analyser: ")
            )  # Get choice.
        if user_choice == "1":  # Peptide chain analyser route.
            raw_chain: str = str(
                input("\nInput Chain: ").strip().upper()
            )  # Gets peptide chain input.
            chain: str = peptide_check(raw_chain)  # Validates input.
            molecular_weight: float = calculate_molecular_weight(
                chain
            )  # Calculates molecular weight.
            hydrophobicity: float = calculate_hydrophobicity(
                chain
            )  # Calculates hydrophobicity.
            percentage_composition: str = calculate_percentage_composition(
                chain
            )  # Gets percentage composition.
            table: list[tuple[str, str]] = peptide_table(
                molecular_weight, hydrophobicity
            )  # Creates peptide data table.
            print(figlet.renderText("Results"))  # Displays result title.
            print(
                f"{tabulate(table, tablefmt='double_grid')}\n\n"
                f"Average Percentage Composition:\n\n{percentage_composition}"
            )  # Displays table.
        elif user_choice == "2":  # Residue analyser route.
            raw_residue: str = str(
                input("\nResidue (For Example, Alanine): ").strip().capitalize()
            )  # Get residue.
            residue: str = residue_check(raw_residue)  # Validates residue input.
            table: list[tuple[str, str | float]] = residue_table(
                residue
            )  # Retrieves residue data.
            print(figlet.renderText("Results"))  # Displays result title.
            print(f"{tabulate(table, tablefmt='double_grid')}")  # Display table.
        else:
            raise ValueError
    except (ValueError, EOFError):
        print("Unexpected Error Occurred.")  # Handles errors.
        sys.exit(1)


def peptide_check(raw_chain: str) -> str:
    pattern = re.compile(r"^[ACDEFGHIKLMNPQRSTVWY]{1,1000}$")  # States valid residues.
    while True:
        if pattern.match(raw_chain):
            return raw_chain  # Returns valid chain.
        print(
            "\nError: Non-Existent Residue(s) or Invalid Length."
        )  # Prints error message.
        raw_chain = str(input("\nInput Chain: ")).strip().upper()  # Reprompts user.


def calculate_molecular_weight(chain: str) -> float:
    return sum(
        amino_acid_data[x]["Molecular Weight"] for x in chain
    )  # Returns molecular weight.


def calculate_hydrophobicity(chain: str) -> float:
    total_hydrophobicity: float = sum(
        amino_acid_data[x]["Estimated Average Hydrophobicity"] for x in chain
    )  # Sum hydrophobicity values.
    return total_hydrophobicity / len(chain)  # Returns average.


def calculate_percentage_composition(chain: str) -> str:
    collection: dict[str, int] = {}  # Counts each residue.
    length: int = len(chain)  # Stores chain length.
    for x in chain:
        if x in collection:
            collection[x] += 1  # Increment if exists.
        else:
            collection[x] = 1  # Initialise if first occurrence.
    result: list[str] = []  # Store formatted percentages.
    for key, value in sorted(collection.items()):
        percentage: float = (value / length) * 100  # Calculate percentage.
        result.append(f"{key} | {percentage:.2f}%")  # Format for display.
    return "\n".join(result)  # Combine for output.


def peptide_table(molecular_weight: float, hydrophobicity: float) -> list[tuple[str, str]]:
    table: list[tuple[str, str]] = [
        ("Molecular Weight", f"{molecular_weight} Da"),
        ("Estimated Hydrophobicity", f"{hydrophobicity:.2f}"),
    ]  # Prepare table.
    return table  # Returns table.


def residue_check(raw_residue: str) -> str:
    while True:
        for code, data in amino_acid_data.items():
            if re.fullmatch(data["Name"], raw_residue, re.IGNORECASE):
                return code  # Returns residue if valid.
        print("\nError: Invalid Residue.")  # Prints error message.
        raw_residue = str(
            input("\nResidue (For Example, Alanine): ")
        ).strip()  # Reprompts user.


def residue_table(residue: str) -> list[tuple[str, str | float]]:
    residue_info: dict[str, str | float] = amino_acid_data[residue]  # Get residue info.
    table: list[tuple[str, str | float]] = [
        ("Residue Name", residue_info["Name"]),
        ("1-letter Code", residue),
        ("Molecular Weight", f"{residue_info['Molecular Weight']} Da"),
        (
            "Estimated Hydrophobicity",
            residue_info["Estimated Average Hydrophobicity"],
        ),
        ("Isoelectric Point", residue_info["pI"]),
    ]  # Prepare table.
    return table


if __name__ == "__main__":
    main()  # Run main().
