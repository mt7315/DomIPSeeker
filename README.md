# DomIPSeeker

DomIPSeeker is a security reconnaissance tool that leverage CriminalIP API to look for domains and hosts with the same Organization field in the SSL certificate.

## Installation And Setup

1. Clone the project:
```
git clone https://github.com/mt7315/DomIPSeeker.git
```

2. Prepare and activate the virtual environment :
```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

3. Install requirements :
```
(myenv) $ pip install -r requirements.txt
```

In order to utilize the tool effectively, it is necessary to obtain an API key from CriminalIP . Once you have acquired the key, simply assign the API key to the "api_key" variable located in the domipseeker.py file. This step ensures smooth authentication and seamless access to the CriminalIP API.
```
api_key = "******YOUR_API_KEY_HERE*******"
```

## Usage
```


    __                  __                           __
.--|  |.-----.--------.|__|.-----.-----.-----.-----.|  |--.-----.----.
|  _  ||  _  |        ||  ||  _  |__ --|  -__|  -__||    <|  -__|   _|
|_____||_____|__|__|__||__||   __|_____|_____|_____||__|__|_____|__|
                           |__|

     coded by : KamilDogo
     Powered By CriminalIP
     https://www.criminalip.io/

usage: domipseeker.py [-h] [-i] [-o ORGNAME] [-d] [-s OFFSET] [-a]

Tool to search domain/ip given an orgname

optional arguments:
  -h, --help            show this help message and exit
  -i, --ips             extract ips adresses
  -o ORGNAME, --orgname ORGNAME
                        organization name
  -d, --domains         extract subject's common name
  -s OFFSET, --offset OFFSET
                        Starting position in the dataset(entering in
                        increments of 10)
  -a, --san             extract san domains
```


### Get domains :
```
python3 domipseeker.py -o "Oath Holdings Inc" -d


    __                  __                           __
.--|  |.-----.--------.|__|.-----.-----.-----.-----.|  |--.-----.----.
|  _  ||  _  |        ||  ||  _  |__ --|  -__|  -__||    <|  -__|   _|
|_____||_____|__|__|__||__||   __|_____|_____|_____||__|__|_____|__|
                           |__|

     coded by : KamilDogo
     Powered By CriminalIP
     https://www.criminalip.io/

*.api.aol.com
*.api.ssp.yahooinc.com
*.comet.aol.com
*.comms-notifications-prod.aws.oath.cloud
*.cp.yahoo.com
*.csc.adserver.yahoo.com
*.fc.yahoo.com
*.lexity.com
*.pubgw.yahoo.com
*.ryot-dev.aws.oath.cloud
*.ryot.aws.oath.cloud
...
```

### Get ips :
```
$ python3 domipseeker.py -o "Oath Holdings Inc" -i -s 100


    __                  __                           __
.--|  |.-----.--------.|__|.-----.-----.-----.-----.|  |--.-----.----.
|  _  ||  _  |        ||  ||  _  |__ --|  -__|  -__||    <|  -__|   _|
|_____||_____|__|__|__||__||   __|_____|_____|_____||__|__|_____|__|
                           |__|

     Powered By CriminalIP
     https://www.criminalip.io/

13.212.145.146
13.251.36.157
13.52.36.255
13.56.86.216
....
```

### Get SANs :
```
$ python3 domipseeker.py -o "Oath Holdings Inc" -a


    __                  __                           __
.--|  |.-----.--------.|__|.-----.-----.-----.-----.|  |--.-----.----.
|  _  ||  _  |        ||  ||  _  |__ --|  -__|  -__||    <|  -__|   _|
|_____||_____|__|__|__||__||   __|_____|_____|_____||__|__|_____|__|
                           |__|

     Powered By CriminalIP
     https://www.criminalip.io/

...
ssp.yahoo.com
ssp.yahoo.com
ssp.yahoo.com
adaptv.advertising.com
adaptv.advertising.com
adap.tv
crl3.digicert.com
sha2-ha-server-g6.crl
crl4.digicert.com
sha2-ha-server-g6.crl
....
```


### Notes

the tool may retrieve assets that do not belong to the target orgname . It is crucial to ensure that you are within the intended scope while conducting your testing to avoid unauthorized access


## Disclaimer

Tool has been made for educational purposes only. I'm not responsible for any damage caused.

## Note
For optimal tool performance, the functionality depends on CriminalIP. If errors occur during execution, it could indicate exceeding the query limit tied to your API key. Visit the CriminalIP website for further information and detailed guidance : [CriminalIP Pricing](https://www.criminalip.io/en/pricing)


