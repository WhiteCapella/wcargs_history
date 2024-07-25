from wcargs_history.db.utils import read_data
import pandas as pd

def test_read_data():
    m = read_data()
    assert isinstance(r, pd.DataFrame)
