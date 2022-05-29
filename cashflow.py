import datetime
import pandas as pd
import csv
import os


class CashFlow(object):

    def __init__(self, name='cashflow'):
        self.name = name
        self.columns = ['date_of_activity', 'description', 'amount']
        self.series = pd.DataFrame(columns=self.columns)

    def generate_series(self, description, amount, frequency='MS',
                        start=datetime.date(datetime.date.today().year, 1, 1),
                        end=datetime.date(datetime.date.today().year, 12, 31)):
        """Generate a new data series and append it to the existing data"""
        data = [(date_of_activity, description, amount) for date_of_activity in pd.date_range(start, end, freq=frequency)]
        self.series = pd.concat([self.series, pd.DataFrame(data, columns=self.columns)])

    def add_event(self, description, amount, date_of_activity):
        """Add a single event"""
        self.generate_series(description, amount, frequency='D', start=date_of_activity, end=date_of_activity),
        
    def export_to_csv(self, dirpath, filename):
        """Export the data to a csv file"""

        Sort data by 1) date_of_activity ascending and 2) amount ascending before the export.
        path = os.path.join(dirpath, filename)
        with open(path, 'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(self.columns)
            self.series.sort_values(by=['date_of_activity', 'amount'], ascending=[True, True], inplace=True)
            for index, record in self.series.iterrows():
                csv_writer.writerow(record)
