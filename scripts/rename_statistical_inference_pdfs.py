from __future__ import annotations

import argparse
from pathlib import Path


FILE_RENAMES = {
    "ExamMarch2023.pdf": "140323_aila_sarkka.pdf",
    "ExamJune2023.pdf": "080623_aila_sarkka.pdf",
    "ExamAugust2023.pdf": "150823_aila_sarkka.pdf",
    "mve155_msg200_240312_sols.pdf": "120324_tony_johansson.pdf",
    "MVE155MSG200_August2024.pdf": "270824_aila_sarkka.pdf",
    "ExamMarch2025.pdf": "180325_aila_sarkka.pdf",
    "MVE155MSG200WithSolutionsAugust2025.pdf": "280825_aila_sarkka.pdf",
    "MVE155MSG200March2026WithSolutions.pdf": "200326_aila_sarkka.pdf",
    "statinf_2002-05-28_TL.pdf": "280502_serik_sagitov.pdf",
    "statinf_2003-05-28_TL.pdf": "280503_serik_sagitov.pdf",
    "statinf_2004-05-25_TL.pdf": "250504_serik_sagitov.pdf",
    "statinf_2005-05-23_TL.pdf": "230505_serik_sagitov.pdf",
    "statinf_2006-05-22_TL.pdf": "220506_serik_sagitov.pdf",
    "statinf_2007-05-29_TL.pdf": "290507_serik_sagitov.pdf",
    "statinf_2008-03-14_TL.pdf": "140308_serik_sagitov.pdf",
    "statinf_2009-03-13_TL.pdf": "130309_serik_sagitov.pdf",
    "statinf_2010-03-12_TL.pdf": "120310_serik_sagitov.pdf",
    "statinf_2011-03-18_TL.pdf": "180311_serik_sagitov.pdf",
    "statinf_2012-03-09_TL.pdf": "090312_serik_sagitov.pdf",
    "statinf_2013-03-12_TL.pdf": "120313_serik_sagitov.pdf",
    "statinf_2014-03-11_TL.pdf": "110314_serik_sagitov.pdf",
    "statinf_2015-03-17_TL.pdf": "170315_serik_sagitov.pdf",
    "statinf_2016-03-15_TL.pdf": "150316_serik_sagitov.pdf",
    "statinf_2017-03-14_TL.pdf": "140317_serik_sagitov.pdf",
    "statinf_2017-06-07_T.pdf": "070617_serik_sagitov.pdf",
    "statinf_2017-08-21_T.pdf": "210817_serik_sagitov.pdf",
    "statinf_2018-03-13_TL.pdf": "130318_serik_sagitov.pdf",
    "statinf_2019-03-19_TL.pdf": "190319_serik_sagitov.pdf",
    "statinf_2019-06-11_TL.pdf": "110619_serik_sagitov.pdf",
    "statinf_2019-08-29_TL.pdf": "290819_serik_sagitov.pdf",
    "statinf_2020-03-17_TL.pdf": "170320_serik_sagitov.pdf",
    "statinf_2020-06-09_TL.pdf": "090620_serik_sagitov.pdf",
    "statinf_2020-08-27_TL.pdf": "270820_serik_sagitov.pdf",
}


def rename_pdfs(source_dir: Path, apply_changes: bool) -> None:
    for original_name, target_name in FILE_RENAMES.items():
        original_path = source_dir / original_name
        target_path = source_dir / target_name

        if target_path.exists() and not original_path.exists():
            print(f"already-renamed {target_name}")
            continue

        if not original_path.exists():
            print(f"missing {original_name}")
            continue

        if target_path.exists():
            raise FileExistsError(f"Target already exists: {target_path}")

        if apply_changes:
            original_path.rename(target_path)
            print(f"renamed {original_name} -> {target_name}")
        else:
            print(f"dry-run {original_name} -> {target_name}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Rename statistical inference PDFs to ddmmyy_examiner.pdf.")
    parser.add_argument("--source-dir", type=Path, required=True, help="Directory containing the source PDFs")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Perform the rename in place. Without this flag, the script only prints the plan.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    rename_pdfs(args.source_dir.expanduser().resolve(), args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
