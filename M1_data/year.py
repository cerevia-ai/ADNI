import pandas as pd
import os
from datetime import datetime

def parse_date(date_str):
    """Robustly parse VISDATE from multiple ADNI formats"""
    if pd.isna(date_str) or str(date_str).strip() in ['', 'None', 'NaT']:
        return pd.NaT
    for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d %H:%M:%S'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

def add_visyear_with_suffix(file_list):
    """
    Add VISYEAR column by parsing VISDATE and save as new file with '_year.csv' suffix.

    Args:
        file_list (list): List of file paths to process
    """
    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue

        print(f"\n📄 Processing: {file_path}")
        try:
            df = pd.read_csv(file_path)

            if 'VISDATE' not in df.columns:
                print(f"⚠️  No 'VISDATE' column in {file_path} — skipping")
                continue

            # Parse VISDATE
            df['VISDATE'] = df['VISDATE'].astype(str).apply(parse_date)

            # Extract VISYEAR
            df['VISYEAR'] = df['VISDATE'].dt.year

            # Create new filename: 'ADAS_M1.csv' → 'ADAS_M1_year.csv'
            dirname = os.path.dirname(file_path) if os.path.dirname(file_path) else '.'
            basename = os.path.basename(file_path)
            name, ext = os.path.splitext(basename)
            new_filename = f"{name}_year{ext}"
            output_path = os.path.join(dirname, new_filename)

            # Save to new file
            df.to_csv(output_path, index=False)
            print(f"✅ Saved with VISYEAR: {output_path}")

        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

# =============================================
# ✅ Define your files here
# =============================================

if __name__ == "__main__":
    files_to_process = [
        'DXSUM_M1.csv',
        # Add more as needed
    ]

    add_visyear_with_suffix(files_to_process)

    print("\n🎉 All files processed. New files saved with '_year.csv' suffix.")