import pandas
from basic_python import make_df


def test_my_df():
	df = make_df()
	assert len(df) == 3
