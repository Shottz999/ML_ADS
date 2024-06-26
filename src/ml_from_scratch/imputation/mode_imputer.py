from typing import Union

import numpy as np
import pandas as pd

from ml_from_scratch.transformation import Transformer


class ModeImputer(Transformer):
    """
    Impute missing values with the mode of the column.

    Attributes
    ----------
    modes : pd.Series
        The modes of the columns.

    Example usage:
    ```python
    # Example usage
    X = pd.DataFrame({'a': [np.nan, 2, 3, 4, 5, 5], 'b': [1, np.nan, 3, 4, 5, 4], 'c': [1, 2, np.nan, 4, 5, 3]})
    imputer = ModeImputer()
    X = imputer.fit_transform(X)
    ```
    """
    modes = None

    def _fit(self, X: pd.DataFrame, y: Union[pd.DataFrame, pd.Series] = None) -> 'ModeImputer':
        """
        Fit the imputer to the data.

        Parameters
        ----------
        X : pd.DataFrame
            The data to impute.
        y : pd.DataFrame or pd.Series, optional
            Ignored.
        """
        self.modes = X.mode().iloc[0]
        return self

    def _transform(self, X: pd.DataFrame, y: Union[pd.DataFrame, pd.Series] = None) -> pd.DataFrame:
        """
        Impute the data.

        Parameters
        ----------
        X : pd.DataFrame
            The data to impute.
        y : pd.DataFrame or pd.Series, optional
            Ignored.

        Returns
        -------
        pd.DataFrame
            The imputed data.
        """
        return X.fillna(self.modes)


if __name__ == '__main__':
    # Example usage
    X = pd.DataFrame({'a': [np.nan, 2, 3, 4, 5, 5], 'b': [1, np.nan, 3, 4, 5, 4], 'c': [1, 2, np.nan, 4, 5, 3]})
    print(X)
    imputer = ModeImputer()
    imputer.fit(X)
    print(imputer.modes)
    X = imputer.transform(X)
    print(X)
