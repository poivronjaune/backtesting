from datetime import datetime, timedelta, date
import backtrader as bt

class PlacedTradesLogger():
  """  
  PlacedTradesLogger: Class to log all placed trades to CSV file using subfolder PLACED
  
  Args:
    strategyid(str) : Id appended to CSV filename P_log_01.csv default='01'
  
  Notes:
    Produces a CSV file delimted with semi colon ;
    The file csv_header.txt contains the column headers for the csv file generated

  """

  def __init__(self, strategyid='01', params=None):
    self.seperator = ';'
    self.log_path  = 'PLACED'
    self.log_name  = f'P-log_{strategyid}'
    self.log_file  = self.create_log_file()
    self.params    = params
    self.log_strategy_parameters()

  def create_log_file(self):
    """
    create_log_file: method to create an empty timestamped log file using csv_header.txt as column headers
    
    Return:
      File handle opened and ready to read/write

    """
    # Read CSV header string
    with open(f"{self.log_path}\csv_header.txt","r") as f:
      log_header = f.read()
      f.close()

    # Build time-stamped log filename
    filename = f"{self.log_path}\{self.log_name}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"      
    # Create log file and insert header line (semi-colon value seperator from self.seperator)
    try:
      log_file = open(f"{filename}","w")
      log_file.write(f"{log_header}\n")
    except Exception as e:
      log_file = None
    
    return log_file

  def log_strategy_parameters(self):
    """
      log_strategy_parameters: create log file containing all the strategy parameters used.  _params will be appended to the logfile name.
    """
    if self.params is not None:
      log_header = ""  
      log_values = ""    
      for key_value in self.params._getitems():
        log_header += f"{key_value[0]}{self.seperator}"
        log_values += f"{key_value[1]}{self.seperator}"
    else:
      log_header = "#No parameters found...."
      log_values = "#No parameters found...."

    params_filename = f"{self.log_path}\{self.logname}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_params.csv"
    # Create log file and insert header line (semi-colon value seperator from self.seperator)
    try:
      log_file = open(f"{params_filename}","w")
      log_file.write(f"{log_header}\n")
      log_file.write(f"{log_values}\n")
    except Exception as e:
      log_file = None
      