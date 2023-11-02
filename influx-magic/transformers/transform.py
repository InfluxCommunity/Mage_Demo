from slugify import slugify
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):

    df['unique_id'] = df.apply(lambda row: f"{slugify(row.provider)}-{row.machineid}", axis=1)

    df['ds'] = pd.to_datetime(df['_time'], unit='us')
    df['power'] = df._power
    # .astype(int)
    print(df.machineid.unique())
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
