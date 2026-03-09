#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


def main() -> None:
    onco_path = Path("cancerGeneList_oncoKB_20260204.tsv")
    cust_path = Path("customer_genes.tsv")
    out_path = Path("cancerGeneList.tsv")

    with out_path.open("w", newline="") as out_f:
        out_f.write("GENE\tOCCURRENCE\tSOURCE\n")

        # OncoKB file (tab-separated)
        with onco_path.open("r", newline="") as f:
            reader = csv.reader(f, delimiter="\t")

            # skip header
            header = next(reader, None)

            for row in reader:
                if not row:
                    continue

                gene = row[0].strip() if len(row) > 0 else ""
                occ = row[7].strip() if len(row) > 7 else ""

                if not gene:
                    continue

                out_f.write(f"{gene}\t{occ}\tONCOKB\n")

        # Append customer genes (already in desired 3-col format)
        if cust_path.exists():
            with cust_path.open("r") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if line:
                        out_f.write(line + "\n")


if __name__ == "__main__":
    main()
