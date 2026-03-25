"""
State configuration for this WisconsinDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "WI"
STATE_NAME = "Wisconsin"
APP_NAME = "WisconsinDischargeWatch"
APP_TAGLINE = "Wisconsin Discharge Monitoring"
DOMAIN = "wisconsindischargewatch.org"
DATA_FILE = "wi_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@wisconsindischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 5
