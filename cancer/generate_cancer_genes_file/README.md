
# Cancer Gene List Builder

Small utility script for generating a unified cancer gene list from:

* An **OncoKB cancer gene TSV export**
* A **customer-specific gene list**

Intended use currently is in Balsamic for the CNV report, to select prioritised genes for plotting and filtering.

The script produces a single standardized output file:

```
GENE    OCCURRENCE    SOURCE
```

---

## What the Script Does

1. Reads the OncoKB TSV file
2. Extracts:

   * `Hugo Symbol` (column 1)
   * `# of occurrence within resources (Column J-P)` (column 8)
3. Writes them as:

```
GENE    OCCURRENCE    ONCOKB
```

4. Appends entries from `customer_genes.tsv`
5. Outputs:

```
cancerGeneList.tsv
```

---

## Required Input Files

### 1. OncoKB Gene List

File example:

```
cancerGeneList_oncoKB_20260204.tsv
```

This file contains the date at which point the genelist was downloaded from OncoKB: https://www.oncokb.org/cancer-genes

Requirements:

* Tab-separated
* Column 1 = Hugo Symbol
* Column 8 = # of occurrence within resources
* Header row present (automatically skipped)

---

### 2. Customer Gene List

File:

```
customer_genes.tsv
```

Format:

```
GENE    OCCURRENCE    SOURCE
```

Example:

```
TP53    NA    cust087
RB1     NA    cust087
```

This is a list of genes provided by customers.


---

## Usage

Run:

```bash
python3 make_cancer_gene_list.py
```

Requirements:

* Python ≥ 3.9
* No external dependencies (standard library only)

---

## Output

Generated file:

```
cancerGenelist.tsv
```

Format:

```
GENE    OCCURRENCE    SOURCE
```

Example:

```
ABL1    7    ONCOKB
AKT1    7    ONCOKB
TP53    NA   cust087
```

---

## Notes

* Input files must be tab-separated.
* No duplicate filtering is performed.
* The script assumes the OncoKB column structure matches the official export.
* Designed for simple reproducible gene list generation in reporting workflows.

---

