import pandas as pd

def collect_data():
    # Example data collection: Genomic sequences
    data = {
        'sequence_id': [1, 2, 3, 4, 5],
        'sequence': [
            'ATCGTACGATCG',
            'CGTACGTAGCTA',
            'TACGATCGTAGC',
            'GATCGTACGTAG',
            'CTAGCTAGCTAG'
        ],
        'disorder': ['disorder1', 'disorder2', 'disorder1', 'disorder3', 'disorder2']
    }
    df = pd.DataFrame(data)
    return df

# Example usage
df = collect_data()
print(df)
