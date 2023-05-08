import sys
import os
import pandas as pd
import re

class ReadFile:
    def __init__(self, filename=None):
        self._filename = filename
        self._path = None
        self._df = None
        self._pattern = None

    @property
    def filename(self):
        return self._filename

    @property
    def pathFinder(self):
        print('*self._path is ', self._path)
        if self._path is None:
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                # the following code looks highly dubious
                path_actual = os.getcwd()
                path_main_folder = path_actual[:-4]
                self._path = path_main_folder + self.filename
                print('frozen path: ', os.path.normpath(self._path))
                self._path=os.path.normpath(self._path)
            else:
                self._path = self.filename
        print('PATH is: ',self._path)
        return self._path


    def pathLooker(self,filenameP):
        self._path = None
        print('+self._path is ', self._path)
        if self._path is None:
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                # the following code looks highly dubious
                path_actual = os.getcwd()
                path_main_folder = path_actual[:-4]
                self._path = path_main_folder + filenameP
                print('frozen path: ', os.path.normpath(self._path))
                self._path=os.path.normpath(self._path)
            else:
                self._path = filenameP
        print('PATH is: ',self._path)
        return self._path

    @property
    def df(self):
        if self._df is None:
            self._df = pd.read_json(self.path)
        return self._df

    @property
    def pattern(self):
        if self._pattern is None:
            self._pattern = re.compile(r"^(?:/.|[^//])*/((?:\\.|[^/\\])*)/")
        return self._pattern

    def read_keys_dropdown(self):
        # the following code looks highly dubious
        lst_dropdown_keys = list(self.df.to_dict().keys())
        lst_dropdown_keys.pop(0)
        lst_dropdown_keys.pop(-1)
        return lst_dropdown_keys

    def read_url(self):
        if m := self.pattern.match(self.df.values[0][0]):
            return m.group(1)

    def read_email_as_key(self):
        if os.path.isfile(self.pathLooker(self.filename)):
            df=pd.read_json(self.pathLooker(self.filename))
            return df['email'][0]

    def read_passw_as_value(self):
        if os.path.isfile(self.pathLooker(self.filename)):
            df=pd.read_json(self.pathLooker(self.filename))
            return df['password'][0]

    def read_csv(self):
        if os.path.isfile(self.pathLooker('./OutputFiles/output_links.csv')):
            df=pd.read_csv(self.pathLooker('./OutputFiles/output_links.csv'))
            return df

