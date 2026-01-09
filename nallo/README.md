# Nallo

| File Path                                                              | Source                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nallo/annotation/grch38_clinvar_rename_chromosomes_-v1.0-.txt`        | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/annotation/grch38_reduced_penetrance_-v1.0-.tsv`                | Modified from [reduced_penetrance.tsv](https://raw.githubusercontent.com/nf-core/test-datasets/raredisease/reference/reduced_penetrance.tsv) to hg38 coordinates                                                                                                                              |
| `nallo/annotation/grch38_strdrop_training_set_260108.json`             | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/annotation/grch38_trgt_pathogenic_repeats_-v1.0-.txt`           | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/annotation/grch38_variant_consequences_-v1.0-.txt`              | Same as [variant_consequences_snv_-v1.0-.txt](https://raw.githubusercontent.com/Clinical-Genomics/reference-files/8175d0a023b70351b3a78fc59f3b3ef4ba86653c/rare-disease/vep_variant_consequences/variant_consequences_snv_-v1.0-.txt)                                                         |
| `nallo/annotation/grch38_vep_112_loftool_scores_-v1.0-.txt`            | Downloaded from [LoFtool_scores.txt](https://github.com/Ensembl/VEP_plugins/raw/refs/heads/release/112/LoFtool_scores.txt)                                                                                                                                                                    |
| `nallo/annotation/grch38_vep_112_pli_values_-v1.0-.txt`                | Downloaded from [pLI_values.txt](https://github.com/Ensembl/VEP_plugins/raw/refs/heads/release/112/pLI_values.txt)                                                                                                                                                                            |
| `nallo/annotation/grch38_vep_resources_stage_-v1.0-.csv`               | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/annotation/sites.hg38.vcf.gz`                                   | Downloaded from [sites.hg38.vcf.gz](https://github.com/brentp/somalier/files/3412456/sites.hg38.vcf.gz), same as [hg38.somalier.sites.vcf.gz](https://github.com/Clinical-Genomics/reference-files/raw/838416c14c689babf55399d7b67a018ccbc58497/cancer/references/hg38.somalier.sites.vcf.gz) |
| `nallo/rank_model/grch38_rank_model_snvs_-v1.0-.ini`                   | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/rank_model/grch38_rank_model_svs_-v1.0-.ini`                    | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/region/grch38_chromosomes_split_at_centromeres_-v1.0-.bed`      | Manually created                                                                                                                                                                                                                                                                              |
| `nallo/region/grch38_hificnv_excluded_regions_common_50_-v1.0-.bed.gz` | Downloaded from [cnv.excluded_regions.common_50.hg38.bed.gz](https://github.com/PacificBiosciences/HiFiCNV/raw/bbaab8115c21a0845ebe517a44a7f55ce3a8b64a/data/excluded_regions/cnv.excluded_regions.common_50.hg38.bed.gz)                                                                     |
| `nallo/region/grch38_hificnv_expected_copynumer_xx_-v1.0-.bed`         | Downloaded from [expected_cn.hg38.XX.bed](https://github.com/PacificBiosciences/HiFiCNV/raw/7b0622788cbfbf571c34fff55924991b6c688893/data/expected_cn/expected_cn.hg38.XX.bed)                                                                                                                |
| `nallo/region/grch38_hificnv_expected_copynumer_xy_-v1.0-.bed`         | Downloaded from [expected_cn.hg38.XY.bed](https://raw.githubusercontent.com/PacificBiosciences/HiFiCNV/7b0622788cbfbf571c34fff55924991b6c688893/data/expected_cn/expected_cn.hg38.XY.bed)                                                                                                      |
| `nallo/region/grch38_par_-v1.0-.bed`                                   | Downloaded from [GRCh38_PAR.bed](https://storage.googleapis.com/deepvariant/case-study-testdata/GRCh38_PAR.bed)                                                                                                                                                                               |

## strdrop archive

`nallo/annotation/grch38_strdrop_training_set_260108.json` was created by running strdrop 0.3.1 on TRGT 5.0.0 VCFs run with `grch38_trgt_pathogenic_repeats.bed` commit [0cd376caa80dd25d4af6ee52155044aeb0aeeee1](https://raw.githubusercontent.com/Clinical-Genomics/reference-files/0cd376caa80dd25d4af6ee52155044aeb0aeeee1/nallo/annotation/grch38_trgt_pathogenic_repeats.bed), from 463 cases sequenced at CG and processed by Nallo:

```
export IMG=/home/proj/stage/workflows/nallo/singularity_cache/depot.galaxyproject.org-singularity-trgt-5.0.0--h9ee0642_0.img
export GENOME=../GRCh38_GIABv3_no_alt_analysis_set_maskedGRC_decoys_MAP2K3_KMT2C_KCNJ18.fasta
export REPEATS=/home/proj/production/workflows/nallo/references/v0.4.0/grch38_trgt_pathogenic_repeats.bed

cd trgt

parallel -j 36 --colsep '\t' \
  singularity exec -B /home/proj/production "$IMG" trgt genotype \
    --sample-name {1} \
    --genome "$GENOME" \
    --reads ../data/{1}_haplotagged.bam \
    --repeats "$REPEATS" \
    --karyotype {2} \
    --threads 1 \
    --output-prefix {1} \
  :::: ../samples_sequenced_at_cg_not_cust000_with_known_sex.tsv

cd ../strdrop
singularity pull https://community-cr-prod.seqera.io/docker/registry/v2/blobs/sha256/f8/f860e6cdc0d4222f89145d5e5f6aba15368eefc50b65bc78890613d976344a7f/data

cd ../
singularity exec strdrop/data strdrop build --training-set trgt/ grch38_strdrop_training_set_260108.json
```
